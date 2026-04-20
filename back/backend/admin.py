from django.contrib import admin
from django.contrib.admin import AdminSite
from django.views.decorators.csrf import csrf_exempt


class CSRFExemptAdminSite(AdminSite):
    """Custom admin site that exempts login from CSRF"""
    
    def login(self, request, extra_context=None):
        # Wrap the login view with csrf_exempt
        view = super().login
        return csrf_exempt(view)(request, extra_context)
    
    def has_permission(self, request):
        """
        Return True if the user is active and is a staff member.
        """
        return request.user.is_active and request.user.is_staff


# Replace the default admin site
admin.site = CSRFExemptAdminSite()
admin.site._registry = admin.site._registry.copy()
