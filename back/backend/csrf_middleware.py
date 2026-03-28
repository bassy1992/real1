"""
Middleware to exempt admin URLs from CSRF protection
"""
from django.utils.deprecation import MiddlewareMixin
from django.views.decorators.csrf import csrf_exempt


class AdminCSRFExemptMiddleware(MiddlewareMixin):
    """Exempt admin URLs from CSRF protection"""
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path.startswith('/admin/'):
            # Wrap the view with csrf_exempt
            return csrf_exempt(view_func)(request, *view_args, **view_kwargs)
        return None
