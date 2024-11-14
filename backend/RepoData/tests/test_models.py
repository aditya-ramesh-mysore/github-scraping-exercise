from django.test import TestCase
from ..models import User, Repository

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up a User instance used by all test methods
        User.objects.create(username='testuser')

    def test_username_label(self):
        user = User.objects.get(username='testuser')
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_username_max_length(self):
        user = User.objects.get(username='testuser')
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 50)

    def test_username_is_unique(self):
        user = User.objects.get(username='testuser')
        unique = user._meta.get_field('username').unique
        self.assertTrue(unique)

    def test_object_name_is_username(self):
        user = User.objects.get(username='testuser')
        expected_object_name = str(user.username)
        self.assertEqual(str(user), expected_object_name)

    def test_created_at_auto_now_add(self):
        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user.created_at)

    def test_updated_at_auto_now(self):
        user = User.objects.get(username='testuser')
        old_updated_at = user.updated_at
        user.username = 'updateduser'
        user.save()
        self.assertNotEqual(user.updated_at, old_updated_at)



class RepositoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up a User and a Repository instance used by all test methods
        user = User.objects.create(username='testuser')
        Repository.objects.create(
            user=user,
            repository_name='testrepo',
            description='A test repository',
            page_number=1,
            etag='etag123',
            stars=10,
            forks=5
        )

    def test_repository_name_label(self):
        repository = Repository.objects.get(id=1)
        field_label = repository._meta.get_field('repository_name').verbose_name
        self.assertEqual(field_label, 'repository name')

    def test_repository_name_max_length(self):
        repository = Repository.objects.get(id=1)
        max_length = repository._meta.get_field('repository_name').max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        repository = Repository.objects.get(id=1)
        max_length = repository._meta.get_field('description').max_length
        self.assertEqual(max_length, 400)

    def test_page_number_default_value(self):
        repository = Repository.objects.get(id=1)
        self.assertEqual(repository.page_number, 1)

    def test_etag_max_length(self):
        repository = Repository.objects.get(id=1)
        max_length = repository._meta.get_field('etag').max_length
        self.assertEqual(max_length, 100)

    def test_stars_default_value(self):
        repository = Repository.objects.get(id=1)
        self.assertEqual(repository.stars, 10)

    def test_forks_default_value(self):
        repository = Repository.objects.get(id=1)
        self.assertEqual(repository.forks, 5)

    def test_object_name_is_repository_name_and_user(self):
        repository = Repository.objects.get(id=1)
        expected_object_name = f"{repository.repository_name} belonging to {repository.user}"
        self.assertEqual(str(repository), expected_object_name)

    def test_unique_user_repository_constraint(self):
        user = User.objects.get(id=1)
        with self.assertRaises(Exception):
            Repository.objects.create(
                user=user,
                repository_name='testrepo'
            )
