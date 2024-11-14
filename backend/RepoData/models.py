from django.db import models


# Base model for all the models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# User model to store github username and etag associated to data received from Github API
class User(BaseModel):
    username = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return str(self.username)


# Repository model which stores all the repositories related to different users in the User table
class Repository(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repository_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)
    page_number = models.IntegerField(default=1)
    etag = models.CharField(max_length=100, default="")
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'repository_name'], name='unique_user_repository')
        ]

    def __str__(self):
        return str(self.repository_name) + " belonging to " + str(self.user)
