from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import UserService
from ..serializers import UserSerializer

class UserView(APIView):

    # users/
    def get(self, request, *args, **kwargs):
        # View for getting users: Accepts recent, page as query parameters
        try:
            recent = int(request.GET.get('recent', 10))
            page = int(request.GET.get('page', 1))
            service = UserService()
            most_recent_users = service.get_recent_users(recent, page)
            serializer = UserSerializer(most_recent_users, many=True)
            return Response(serializer.data)

        except ValueError:
            return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'error': "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)