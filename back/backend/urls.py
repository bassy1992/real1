"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from backend.custom_admin import custom_admin_login
from backend.reset_views import reset_admin_password

# Import custom admin to apply CSRF exemption
import backend.admin


@csrf_exempt
def admin_redirect(request):
    """Redirect to login if not authenticated"""
    if request.user.is_authenticated:
        return HttpResponseRedirect('/admin/dashboard/')
    return HttpResponseRedirect('/admin/login/')


urlpatterns = [
    path('admin/login/', custom_admin_login, name='admin_login'),
    path('admin/reset-password/', reset_admin_password, name='reset_admin_password'),
    path('admin/', admin_redirect, name='admin_redirect'),
    path('admin/', admin.site.urls),
    path('api/', include('properties.urls')),
    path('api/investments/', include('investment_opportunities.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

