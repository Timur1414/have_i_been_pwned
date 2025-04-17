"""
Middleware to log the request and response.
"""
import logging

logger = logging.getLogger('custom_django')


class LoggingMiddleware:
    """
    Middleware to log the request and response.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        logger.info('Request(%s): %s %s    user=%s', request.method, request.method, request.path, user)
        response = self.get_response(request)
        if response.status_code == 200:
            logger.info('Response: %s', response.status_code)
        else:
            logger.error('Response: %s', response.status_code)
        return response
