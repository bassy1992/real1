"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from backend.debug_views import check_admin_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug/admin-user/', check_admin_user),
    path('api/', include('properties.urls')),
    path('api/investments/', include('investment_opportunities.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




