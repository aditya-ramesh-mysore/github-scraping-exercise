from ..models import User

# UserService interacts with user repository
class UserService:
    __USERS_PER_PAGE = 10

    def get_recent_users(self, recent=10, page=1):
        '''
        :param recent: Integer, default 10
        :param page: Integer, default 1
        :return: List of User objects
        '''
        most_recent_users = User.objects.all().order_by('-created_at')[:recent]
        # Calculating lower limit and upper limit for paginated responses
        if page > 1:
            lower_limit = (page - 1) * self.__USERS_PER_PAGE
            upper_limit = lower_limit + self.__USERS_PER_PAGE
            most_recent_users = most_recent_users[lower_limit:upper_limit]
        else:
            most_recent_users = most_recent_users[:self.__USERS_PER_PAGE]
        return most_recent_users