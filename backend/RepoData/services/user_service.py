from ..models import User

class UserService:

    def get_recent_users(self, recent=10):
        try:
            most_recent_users = User.objects.all().order_by('-created_at')[:recent]
            return most_recent_users
        except Exception as e:
            raise e