"""
Debug views to check admin user status
"""
from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()


def check_admin_user(request):
    """Check admin user status"""
    try:
        admin_user = User.objects.get(username='admin')
        return JsonResponse({
            'username': admin_user.username,
            'email': admin_user.email,
            'is_staff': admin_user.is_staff,
            'is_superuser': admin_user.is_superuser,
            'is_active': admin_user.is_active,
            'has_module_perms_admin': admin_user.has_module_perms('admin'),
            'has_module_perms_properties': admin_user.has_module_perms('properties'),
        })
    except User.DoesNotExist:
        return JsonResponse({'error': 'Admin user not found'}, status=404)
