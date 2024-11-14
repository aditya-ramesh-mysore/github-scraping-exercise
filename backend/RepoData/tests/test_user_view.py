from django.test import TestCase, Client
from ..models import *
from rest_framework import status


# Testing UserView
class UserViewTest(TestCase):


    def setUp(self):
        User.objects.create(username='testuser1')
        User.objects.create(username='testuser2')
        User.objects.create(username='testuser3')
        self.client = Client()
        self.url = "http://127.0.0.1:8000/v1/users/"

    def test_get_recent_users_success(self):
        response = self.client.get(self.url, {'recent': 2, 'page': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        data = response.data
        self.assertEqual(data[0]['username'], 'testuser3')
        self.assertEqual(data[1]['username'], 'testuser2')

    def test_get_recent_users_default(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_recent_users_success_pagination(self):
        for i in range(4, 14):
            User.objects.create(username='testuser' + str(i))

        response = self.client.get(self.url, {'recent': 13, 'page': 2})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        data = response.data
        self.assertEqual(data[0]['username'], 'testuser3')
        self.assertEqual(data[1]['username'], 'testuser2')
        self.assertEqual(data[2]['username'], 'testuser1')

    def test_get_recent_users_invalid_parameters(self):
        response = self.client.get(self.url, {'recent': 'invalid', 'page': 'invalid'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid parameters')

    def test_get_recent_users_no_users(self):
        User.objects.all().delete()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_unexpected_error_handling(self):
        # Simulate an unexpected error by patching the get_recent_users method
        with self.assertRaises(Exception):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
            self.assertEqual(response.data['error'], "An unexpected error occurred.")