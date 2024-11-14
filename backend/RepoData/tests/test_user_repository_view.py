from django.test import TestCase, Client
from ..models import *
from rest_framework import status
from django.urls import reverse
from ..exceptions import *
from unittest.mock import patch


# Testing UserRepositoryView
class UserRepositoryViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up a User and Repository instances used by all test methods
        cls.user = User.objects.create(username='testuser')
        Repository.objects.create(user=cls.user, repository_name='repo1', stars=100)

    def setUp(self):
        self.client = Client()
        self.url = reverse("user_repositories", kwargs={"username": self.user.username})

    def test_get_user_repositories_success(self):
        response = self.client.get(self.url, {'page': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['repository_name'], 'repo1')

    def test_get_user_repositories_user_not_found(self):
        url = reverse('user_repositories', kwargs={'username': 'sdfhjbfwesdfcrwfdsc'})
        response = self.client.get(url, {'page': 1})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'User not found.')

    def test_get_user_repositories_rate_limit_exceeded(self):
        with patch('RepoData.services.RepositoryService.get_user_repositories', side_effect=RateLimitExceeded("Too many requests.")):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_get_user_repositories_unauthorized_access(self):
        with patch('RepoData.services.RepositoryService.get_user_repositories', side_effect=UnauthorizedAccess("Unauthorized access to GitHub API. Check your GitHub token.")):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_unexpected_error_handling(self):
        with patch('RepoData.services.RepositoryService.get_user_repositories', side_effect=Exception("Unexpected error")):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertEqual(response.data['error'], "An unexpected error occurred.")