import os
import requests
from ..exceptions import *
from django.http import Http404
from rest_framework import status
from .abstract_github_service import AbstractGithubService

# Service class that retrieves repositories belonging to a user
class GithubRepositoriesService(AbstractGithubService):
    __BASE_GITHUB_URL = 'https://api.github.com/'
    __GITHUB_TOKEN = os.environ.get('GITHUB_API_TOKEN')

    def _get_headers(self, etag=None):
        # Included authorization token from env variables
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {self.__GITHUB_TOKEN}'
        }
        if etag:
            headers['If-None-Match'] = etag
        return headers

    def _build_url(self, endpoint, page):
        return f"{self.__BASE_GITHUB_URL}/{endpoint}?page={page}&per_page=10&sort=created"

    def call_github_api(self, endpoint, page, etag=None):
        # Main method that calls Github endpoint
        url = self._build_url(endpoint, page)
        headers = self._get_headers(etag)
        response = requests.get(url, headers=headers)
        self._handle_github_response_errors(response)

        return response

    def _handle_github_response_errors(self, response):
        # Handle possible response codes received from github API call
        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise Http404("GitHub user not found.")
        elif response.status_code in (status.HTTP_403_FORBIDDEN, status.HTTP_429_TOO_MANY_REQUESTS):
            raise RateLimitExceeded("Too many requests to GitHub API. Please try again later.")
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            raise UnauthorizedAccess("Unauthorized access to GitHub API. Check your GitHub token.")
        elif 400 <= response.status_code < 500:
            raise Exception(f"Client error ({response.status_code}): {response.text}")
        elif 500 <= response.status_code < 600:
            raise Exception(f"GitHub server error ({response.status_code}). Try again later.")