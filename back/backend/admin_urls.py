from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# Wrap admin site to exempt from CSRF temporarily
admin.site.login = csrf_exempt(admin.site.login)

urlpatterns = [
    path('', admin.site.urls),
]
