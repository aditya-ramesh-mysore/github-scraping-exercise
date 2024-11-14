from django.test import TestCase, Client
from rest_framework import status

from ..models import Repository, User


# Testing RepositoryView
class RepositoryViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        Repository.objects.create(user=self.user, repository_name='repo1', stars=100)
        Repository.objects.create(user=self.user, repository_name='repo2', stars=50)
        Repository.objects.create(user=self.user, repository_name='repo3', stars=150)
        self.client = Client()
        self.url = 'http://127.0.0.1:8000/v1/repositories/'

    def test_get_most_starred_repositories_success(self):
        response = self.client.get(self.url, {'recent': 2, 'page': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_most_starred_repositories_default(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_most_starred_repositories_success_pagination(self):
        for i in range(4, 14):
            Repository.objects.create(user=self.user, repository_name='repo' + str(i), stars=10)

        response = self.client.get(self.url, {'recent': 13, 'page': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        data = response.data
        self.assertEqual(len(data), 3)

    def test_get_most_starred_repositories_invalid_parameters(self):
        response = self.client.get(self.url, {'recent': 'invalid', 'page': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid parameters')

    def test_get_most_starred_repositories_no_repositories(self):
        Repository.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_unexpected_error_handling(self):
        # Simulate an unexpected error by patching the get_most_starred_repositories method
        with self.assertRaises(Exception):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertEqual(response.data['error'], "An unexpected error occurred.")