"""
Custom admin dashboard views
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/admin/login/')
def admin_dashboard(request):
    """Simple admin dashboard"""
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin Dashboard</title>
        <style>
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                background: #f8f9fa;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                border-radius: 8px;
                padding: 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #333;
                margin-top: 0;
            }}
            .user-info {{
                background: #f0f4f8;
                padding: 15px;
                border-radius: 6px;
                margin-bottom: 30px;
            }}
            .user-info p {{
                margin: 5px 0;
                color: #555;
            }}
            .logout-btn {{
                background: #dc3545;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
            }}
            .logout-btn:hover {{
                background: #c82333;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Admin Dashboard</h1>
            <div class="user-info">
                <p><strong>Logged in as:</strong> {request.user.username}</p>
                <p><strong>Email:</strong> {request.user.email}</p>
                <p><strong>Staff:</strong> {'Yes' if request.user.is_staff else 'No'}</p>
                <p><strong>Superuser:</strong> {'Yes' if request.user.is_superuser else 'No'}</p>
            </div>
            <form method="post" action="/admin/logout/">
                <button type="submit" class="logout-btn">Logout</button>
            </form>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)


@csrf_exempt
def admin_logout(request):
    """Logout view"""
    from django.contrib.auth import logout
    logout(request)
    return HttpResponseRedirect('/admin/login/')
