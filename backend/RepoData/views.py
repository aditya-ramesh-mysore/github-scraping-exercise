from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .serializers import RepositoryDetailSerializer
from .services.repository_service import RepositoryService

# Create your views here.
class RepositoryView(APIView):

    # repositories/
    def get(self, request, *args, **kwargs):
        pass


class UserView(APIView):

    # users/
    def get(self, request, *args, **kwargs):
        pass



class UserRepositoryView(APIView):

    # users/{username}/repositories
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username', None)
        if not username:
            return Response({'error': 'Username is required.'}, status=status.HTTP_400_BAD_REQUEST)

        service = RepositoryService()
        try:
            result = service.get_user_repositories(username, request.GET)
            serializer = RepositoryDetailSerializer(result, many=True)
            return Response(serializer.data)

        except Http404:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)