"""
Custom admin login that bypasses CSRF completely
"""
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["GET", "POST"])
def custom_admin_login(request):
    """Custom admin login view that bypasses CSRF"""
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/admin/')
        else:
            error = 'Invalid username or password'
            return TemplateResponse(request, 'admin/login.html', {'error': error})
    
    return TemplateResponse(request, 'admin/login.html', {})
