from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect

@ensure_csrf_cookie
def admin_login_wrapper(request):
    """Ensure CSRF cookie is set before admin login"""
    return redirect('/admin/')
