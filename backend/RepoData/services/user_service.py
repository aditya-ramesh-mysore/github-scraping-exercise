from ..models import User

# UserService interacts with user repository
class UserService:
    __USERS_PER_PAGE = 10

    def get_recent_users(self, recent=10, page=1):
        # Get most recent users, according to created_at field, saved in the database
        try:
            most_recent_users = User.objects.all().order_by('-created_at')[:recent]
            # Calculating lower limit and upper limit for paginated responses
            if page > 1:
                lower_limit = (page - 1) * self.__USERS_PER_PAGE
                upper_limit = lower_limit + self.__USERS_PER_PAGE
                most_recent_users = most_recent_users[lower_limit:upper_limit]
            else:
                most_recent_users = most_recent_users[:self.__USERS_PER_PAGE]
            return most_recent_users
        except Exception as e:
            raise e