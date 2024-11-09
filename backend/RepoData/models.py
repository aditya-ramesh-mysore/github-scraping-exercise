from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    etag = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repository_name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.repository_name) + " belonging to " + str(self.user)
