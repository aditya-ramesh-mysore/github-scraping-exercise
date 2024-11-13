from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import RepositoryDetailSerializer
from .services.repository_service import RepositoryService
from .exceptions import *
from .services.github_repositories_service import GithubRepositoriesService
from .services.user_service import UserService
from .serializers import UserSerializer
from django.db import DatabaseError, OperationalError
from django.db import connection


# Create your views here.
class RepositoryView(APIView):

    # repositories/
    def get(self, request, *args, **kwargs):
        try:
            recent = int(request.GET.get('recent', 10))
            service = RepositoryService()
            most_starred_repositories = service.get_most_starred_repositories(recent)
            serializer = RepositoryDetailSerializer(most_starred_repositories, many=True)
            return Response(serializer.data)

        except ValueError:
            return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):

    # users/
    def get(self, request, *args, **kwargs):
        try:
            recent = int(request.GET.get('recent', 10))
            page = int(request.GET.get('page', 1))
            service = UserService()
            most_recent_users = service.get_recent_users(recent, page)
            serializer = UserSerializer(most_recent_users, many=True)
            return Response(serializer.data)

        except ValueError:
            return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)


class UserRepositoryView(APIView):

    # users/{username}/repositories
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username', None)
        if not username:
            return Response({'error': 'Username is required.'}, status=status.HTTP_400_BAD_REQUEST)

        service = RepositoryService(GithubRepositoriesService())
        try:
            result = service.get_user_repositories(username, request.GET)
            serializer = RepositoryDetailSerializer(result, many=True)
            return Response(serializer.data)

        except Http404:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        except RateLimitExceeded as e:
            return Response({'error': str(e)}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        except UnauthorizedAccess as e:
            return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class HealthCheckView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            connection.ensure_connection()
            return Response(status=status.HTTP_200_OK)
        except (OperationalError, DatabaseError) as db_error:
            return Response(
                {"error": "Database is currently unavailable. Please try again later."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )