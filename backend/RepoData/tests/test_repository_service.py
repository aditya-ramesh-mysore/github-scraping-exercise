from django.test import TestCase
from unittest.mock import MagicMock, patch
from ..models import Repository, User
from ..services.repository_service import RepositoryService

class RepositoryServiceTest(TestCase):
    def setUp(self):
        self.github_service = MagicMock()
        self.repository_service = RepositoryService(github_service=self.github_service)

    def test_get_most_starred_repositories(self):
        user = User.objects.create(username="test_user")
        Repository.objects.create(user=user, repository_name="Repo1", stars=5)
        Repository.objects.create(user=user, repository_name="Repo2", stars=10)
        Repository.objects.create(user=user, repository_name="Repo3", stars=7)

        result = self.repository_service.get_most_starred_repositories(most_starred=2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].repository_name, "Repo2")
        self.assertEqual(result[1].repository_name, "Repo3")

    def test_get_user_repositories_from_db(self):
        user = User.objects.create(username="test_user")
        Repository.objects.create(user=user, repository_name="Repo1", page_number=1)
        query_params = {'page': 1}

        result = self.repository_service.get_user_repositories("test_user", query_params)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].repository_name, "Repo1")

    @patch.object(RepositoryService, '_fetch_repos_from_github')
    def test_get_user_repositories_from_github(self, mock_fetch_repos):
        mock_fetch_repos.return_value = ["mock_repo"]
        query_params = {'page': 1, 'refresh': 'true'}

        result = self.repository_service.get_user_repositories("nonexistent_user", query_params)

        mock_fetch_repos.assert_called_once()
        self.assertEqual(result, ["mock_repo"])

    def test_should_fetch_from_github(self):
        query_params = {'refresh': 'true'}
        result = self.repository_service._should_fetch_from_github(query_params)

        self.assertTrue(result)

        query_params = {}
        result = self.repository_service._should_fetch_from_github(query_params)

        self.assertFalse(result)

    def test_get_etag_existing_user(self):
        # Setup
        user = User.objects.create(username="test_user")
        Repository.objects.create(user=user, repository_name="Repo1", page_number=1, etag="test_etag")

        result = self.repository_service._get_etag(user, page=1)

        self.assertEqual(result, "test_etag")

    def test_get_etag_nonexistent_user(self):
        result = self.repository_service._get_etag(None, page=1)

        self.assertIsNone(result)


    def test_save_repositories(self):
        user = User.objects.create(username="test_user")
        data = [
            {
                'name': 'Repo1',
                'description': 'A test repo',
                'stargazers_count': 10,
                'forks_count': 2
            }
        ]
        page = 1
        etag = "test_etag"

        self.repository_service._save_repositories(data, user, page, etag)

        saved_repo = Repository.objects.get(user=user, repository_name='Repo1')
        self.assertEqual(saved_repo.description, 'A test repo')
        self.assertEqual(saved_repo.stars, 10)
        self.assertEqual(saved_repo.forks, 2)
        self.assertEqual(saved_repo.etag, "test_etag")
