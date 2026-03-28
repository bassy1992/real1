"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from backend.custom_admin import custom_admin_login
from backend.admin_views import admin_dashboard, admin_logout
from backend.reset_views import reset_admin_password


@csrf_exempt
def admin_redirect(request):
    """Redirect to dashboard if authenticated, otherwise to login"""
    if request.user.is_authenticated:
        return HttpResponseRedirect('/admin/dashboard/')
    return HttpResponseRedirect('/admin/login/')


urlpatterns = [
    path('admin/login/', custom_admin_login, name='admin_login'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    path('admin/reset-password/', reset_admin_password, name='reset_admin_password'),
    path('admin/', admin_redirect, name='admin_redirect'),
    path('api/', include('properties.urls')),
    path('api/investments/', include('investment_opportunities.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



