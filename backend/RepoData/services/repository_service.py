import os
from ..models import Repository, User
from dotenv import load_dotenv
from rest_framework import status

load_dotenv()

class RepositoryService:
    __BASE_GITHUB_URL = 'https://api.github.com/'
    __GITHUB_TOKEN = os.environ.get('GITHUB_API_TOKEN')

    def __init__(self, github_service=None):
        self.github_service = github_service

    def get_most_starred_repositories(self, recent=10):
        try:
            most_starred_repositories = Repository.objects.all().order_by('-stars')[:recent]
            return most_starred_repositories
        except Exception as e:
            raise e

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

    def _get_etag(self, user_obj, page):
        if not user_obj:
            return None
        user_repo = Repository.objects.filter(user=user_obj, page_number=page).first()
        return user_repo.etag if user_repo else None

    def _fetch_repos_from_github(self, user_obj, username, page):
        etag = self._get_etag(user_obj, page)
        response = self.github_service.call_github_api(f'users/{username}/repos', page, etag)

        if response.status_code == status.HTTP_304_NOT_MODIFIED and user_obj:
            return Repository.objects.filter(user=user_obj, page_number=page)

        if response.status_code == status.HTTP_200_OK:
            user_obj, created = User.objects.get_or_create(username=username)
            saved_repository_list = self._save_repositories(response.json(), user_obj, page, response.headers.get('ETag'))
            return saved_repository_list

        raise Exception(f"Unexpected GitHub API response: {response.status_code} - {response.text}")

    def _save_repositories(self, data, user_obj, page, etag):
        if not data:
            return []
        try:
            Repository.objects.filter(user=user_obj, page_number=page).delete()
            print("Deleted Repositories object")

            for repo_data in data:
                object_data = {
                    'etag': etag,
                    'page_number': page,
                    'description': repo_data.get('description'),
                    'stars': repo_data['stargazers_count'],
                    'forks': repo_data['forks_count'],
                }

                repository, created = Repository.objects.update_or_create(
                    user=user_obj,
                    repository_name=repo_data['name'],
                    defaults=object_data
                )

        except Exception as e:
            print(e)

        return Repository.objects.filter(user=user_obj, page_number=page)
