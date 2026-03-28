"""
CSRF fix middleware for Django admin on Railway
"""
from django.middleware.csrf import CsrfViewMiddleware
from django.utils.decorators import decorator_from_middleware_with_args


class CsrfFixMiddleware(CsrfViewMiddleware):
    """
    Custom CSRF middleware that ensures the CSRF cookie is always set
    """
    def process_request(self, request):
        # Always ensure CSRF cookie is set for GET requests
        if request.method == 'GET':
            # This will set the CSRF cookie
            request.META['CSRF_COOKIE_NEEDS_UPDATE'] = True
        return super().process_request(request)

    def process_response(self, request, response):
        # Ensure CSRF cookie is set in response
        response = super().process_response(request, response)
        
        # Force set CSRF cookie for admin pages
        if '/admin' in request.path:
            from django.middleware.csrf import get_token
            get_token(request)
        
        return response
