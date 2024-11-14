from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ..serializers import RepositoryDetailSerializer
from ..services import RepositoryService


# Repository view
class RepositoryView(APIView):

    # repositories/
    def get(self, request, *args, **kwargs):
        # View for getting Repository resources, takes most_starred, page as GET parameters
        try:
            most_starred = int(request.GET.get('most_starred', 10))
            page = int(request.GET.get('page', 1))
            service = RepositoryService()
            most_starred_repositories = service.get_most_starred_repositories(most_starred, page)
            serializer = RepositoryDetailSerializer(most_starred_repositories, many=True)
            return Response(serializer.data)

        except ValueError:
            return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({'error': "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)