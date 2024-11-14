from rest_framework import serializers

from .models import User, Repository

# Wrote different serializer classes to serialize an deserialize objects

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'created_at']
        read_only_fields = ['id']


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'
        read_only_fields = ['id']

class RepositoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = ['repository_name', 'description', 'stars', 'forks', 'page_number']