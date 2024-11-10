from django.shortcuts import render
from rest_framework.views import APIView

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
        pass
