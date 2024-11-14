from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..serializers import RepositoryDetailSerializer
from ..services import RepositoryService, GithubRepositoriesService
from ..exceptions import *


class UserRepositoryView(APIView):

    # users/{username}/repositories
    def get(self, request, *args, **kwargs):
        # Get repositories belonging to a particular user, takes username (part of URL); page, refresh as query parameters
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
            return Response({'error': "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)