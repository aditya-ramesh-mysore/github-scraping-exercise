from django.db import DatabaseError, OperationalError
from django.db import connection
from django.http import JsonResponse

# Middleware the checks connection to database for every request
class DatabaseExceptionMiddleware:
    '''
    Middleware to handle database exceptions, return 503 if database connection fails.
    '''
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
