from django.db import DatabaseError, OperationalError
from django.db import connection
from django.http import JsonResponse
class DatabaseExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            connection.ensure_connection()
            response = self.get_response(request)
            return response
        except OperationalError as db_error:
            return JsonResponse(
                {"error": "Database is currently unavailable. Please try again later."},
                status=503
            )
