from backend.RepoData.models import User

class UserService:

    def save_user(self, user_obj):
        user = User(user_obj)
        user.save()
        return user