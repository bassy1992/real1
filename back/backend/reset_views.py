"""
Emergency password reset endpoint
"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

User = get_user_model()


@csrf_exempt
@require_http_methods(["POST"])
def reset_admin_password(request):
    """Emergency endpoint to reset admin password"""
    
    # Security: Only allow from localhost or specific IPs in production
    # For now, just reset it
    
    try:
        user = User.objects.get(username='admin')
        user.set_password('logan123@')
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        
        return JsonResponse({
            'status': 'success',
            'message': 'Admin password reset to logan123@'
        })
    except User.DoesNotExist:
        user = User.objects.create_superuser('admin', 'admin@bellrockholdings.org', 'logan123@')
        return JsonResponse({
            'status': 'success',
            'message': 'Admin user created with password logan123@'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
