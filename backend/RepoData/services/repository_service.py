import os
from django.utils import timezone
from django.http import Http404
from ..models import Repository, User
import requests
from dotenv import load_dotenv
from ..serializers import RepositorySerializer
from rest_framework import status

load_dotenv()

class RepositoryService:
    __BASE_GITHUB_URL = 'https://api.github.com/'
    __GITHUB_TOKEN = os.environ.get('GITHUB_API_TOKEN')

    def get_user_repositories(self, username, query_params):
        page = query_params.get('page', 1)
        fetch_from_github = self._should_fetch_from_github(query_params)
        try:
            user_obj = User.objects.get(username=username)
            stored_repositories = Repository.objects.filter(user=user_obj, page_number=page)
            if not fetch_from_github and stored_repositories.exists():
                return stored_repositories

        except User.DoesNotExist:
            user_obj = None

        return self._fetch_repos_from_github(user_obj, username, page)

    def _should_fetch_from_github(self, query_params):
        return query_params.get('refresh', 'false').lower() == 'true'

    def _get_headers(self, etag=None):
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {self.__GITHUB_TOKEN}'
        }
        if etag:
            headers['If-None-Match'] = etag
        return headers

    def _call_github_api(self, username, page, etag=None):
        url = f'{self.__BASE_GITHUB_URL}/users/{username}/repos?page={page}&per_page=10&sort=created'
        headers = self._get_headers(etag)
        return requests.get(url, headers=headers)

    def _get_etag(self, user_obj, page):
        if not user_obj:
            return None
        user_repo = Repository.objects.filter(user=user_obj, page_number=page).first()
        return user_repo.etag if user_repo else None

    def _fetch_repos_from_github(self, user_obj, username, page):

        etag = self._get_etag(user_obj, page)
        response = self._call_github_api(username, page, etag)

        print(response)
        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise Http404('Not Found')

        if not user_obj:
            user_obj = User.objects.create(username=username)

        if response.status_code == status.HTTP_304_NOT_MODIFIED and user_obj:
            return Repository.objects.filter(user=user_obj, page_number=page)

        if response.status_code == status.HTTP_200_OK:
            if not user_obj:
                user_obj = User.objects.create(username=username)
            saved_repository_list = self._save_repositories(response.json(), user_obj, page, response.headers.get('ETag'))
            return saved_repository_list


    def _save_repositories(self, data, user_obj, page, etag):
        if not data:
            return []

        Repository.objects.filter(user=user_obj, page_number=page).delete()
        saved_repository_list = []

        for repo_data in data:
            object_to_be_created = {
                'user': user_obj.id,
                'etag': etag,
                'page_number': page,
                'repository_name': repo_data['name'],
                'description': repo_data.get('description'),
                'stars': repo_data['stargazers_count'],
                'forks': repo_data['forks_count'],
            }

            serializer_obj = RepositorySerializer(data=object_to_be_created)
            if serializer_obj.is_valid(raise_exception=True):
                saved_repository_list.append(serializer_obj.save())


        return saved_repository_list
