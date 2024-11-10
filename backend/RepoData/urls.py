from django.contrib import admin
from django.urls import path
from .views import UserView, UserRepositoryView, RepositoryView

urlpatterns = [
    path('users/<slug:username>/repositories', UserRepositoryView.as_view(), name='user_repositories'),
    path('users/', UserView.as_view(), name='users'),
    path('repositories/', RepositoryView.as_view(), name='repositories'),
]