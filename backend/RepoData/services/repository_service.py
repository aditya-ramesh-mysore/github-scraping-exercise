import os
from ..models import Repository, User
from dotenv import load_dotenv
from rest_framework import status

load_dotenv()

# Service that interacts with Repository table of the database
class RepositoryService:
    __REPOSITORIES_PER_PAGE = 10

    def __init__(self, github_service=None):
        self.github_service = github_service

    def get_most_starred_repositories(self, most_starred=10, page=1):
        '''
        :param most_starred: Integer
        :param page: Integer
        :return: List of most starred repositories
        '''
        try:
            most_starred_repositories = Repository.objects.all().order_by('-stars')[:most_starred]
            # calculating lower and upper limit for sending paginated responses, default number of repositories is 10
            if page > 1:
                lower_limit = (page - 1) * self.__REPOSITORIES_PER_PAGE
                upper_limit = lower_limit + self.__REPOSITORIES_PER_PAGE
                most_starred_repositories = most_starred_repositories[lower_limit:upper_limit]
            else:
                most_starred_repositories = most_starred_repositories[:self.__REPOSITORIES_PER_PAGE]
            return most_starred_repositories
        except Exception as e:
            raise e

    def get_user_repositories(self, username, query_params):
        '''
        :param username: string
        :param query_params: dictionary
        :return: list of Repository objects, If the repositories are in the database, return them
        if not, query the GitHub API through github_service class, Optionally takes a
        refresh parameter: if true, query Github API for latest data
        '''
        page = query_params.get('page', 1)
        fetch_from_github = self._should_fetch_from_github(query_params)
        try:
            user_obj = User.objects.get(username=username)
            stored_repositories = Repository.objects.filter(user=user_obj, page_number=page)
            # Determine if we need to fetch from github, or from database
            if not fetch_from_github and stored_repositories.exists():
                return stored_repositories

        except User.DoesNotExist:
            user_obj = None

        return self._fetch_repos_from_github(user_obj, username, page)

    def _should_fetch_from_github(self, query_params):
        '''
        :param query_params: dictionary with query parameters
        :return: boolean indicating if repository should be fetched from github
        '''
        return query_params.get('refresh', 'false').lower() == 'true'

    def _get_etag(self, user_obj, page):
        '''
        :param user_obj: User object
        :param page: Integer
        :return: etag (string) or None
        '''
        if not user_obj:
            return None
        user_repo = Repository.objects.filter(user=user_obj, page_number=page).first()
        return user_repo.etag if user_repo else None

    def _fetch_repos_from_github(self, user_obj, username, page):
        '''
        :param user_obj: User object or None
        :param username: String username
        :param page: Integer page number
        :return: List of Repository objects or Exception raised
        '''
        etag = self._get_etag(user_obj, page)
        response = self.github_service.call_github_api(f'users/{username}/repos', page, etag)

        # If Github API responds with 304, return objects stored in the database as data for this page has not changed
        if response.status_code == status.HTTP_304_NOT_MODIFIED and user_obj:
            return Repository.objects.filter(user=user_obj, page_number=page)

        # If the data has changed or data is not present in the database, save the repo data received from Github API
        if response.status_code == status.HTTP_200_OK:
            user_obj, created = User.objects.get_or_create(username=username)
            saved_repository_list = self._save_repositories(response.json(), user_obj, page, response.headers.get('ETag'))
            return saved_repository_list

        raise Exception(f"Unexpected GitHub API response: {response.status_code} - {response.text}")

    def _save_repositories(self, data, user_obj, page, etag):
        '''
        :param data: List of Repository objects
        :param user_obj: User object
        :param page: Integer
        :param etag: String
        :return: List of saved Repository objects
        Delete stale data and replace it with updated data OR create new data if not present
        '''
        if not data:
            return []
        Repository.objects.filter(user=user_obj, page_number=page).delete()

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

        return Repository.objects.filter(user=user_obj, page_number=page)
