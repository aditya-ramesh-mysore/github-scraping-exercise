from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError, OperationalError
from django.db import connection

# HealthCheck view to ensure connection to database
class HealthCheckView(APIView):

    def get(self, request, *args, **kwargs):
        '''
        :param request: Request object
        :param args:
        :param kwargs:
        :return: Response 200 if connection established or 503
        '''
        try:
            connection.ensure_connection()
            return Response(status=status.HTTP_200_OK)
        except (OperationalError, DatabaseError) as db_error:
            return Response(
                {"error": "Database is currently unavailable. Please try again later."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )