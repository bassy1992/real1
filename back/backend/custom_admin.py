"""
Custom admin login that bypasses CSRF completely
"""
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["GET", "POST"])
def custom_admin_login(request):
    """Custom admin login view that bypasses CSRF"""
    
    error = None
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/admin/')
        else:
            error = 'Invalid username or password'
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Administration</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                background: #f8f9fa;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .login-container {
                background: white;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                width: 100%;
                max-width: 400px;
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 30px;
                font-size: 24px;
            }
            .form-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 8px;
                color: #333;
                font-weight: 500;
            }
            input[type="text"],
            input[type="password"] {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
                box-sizing: border-box;
            }
            input[type="text"]:focus,
            input[type="password"]:focus {
                outline: none;
                border-color: #417690;
                box-shadow: 0 0 0 3px rgba(65, 118, 144, 0.1);
            }
            button {
                width: 100%;
                padding: 10px;
                background: #417690;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 14px;
                font-weight: 500;
                cursor: pointer;
                margin-top: 10px;
            }
            button:hover {
                background: #2e5266;
            }
            .error {
                background: #f8d7da;
                color: #721c24;
                padding: 12px;
                border-radius: 4px;
                margin-bottom: 20px;
                border: 1px solid #f5c6cb;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h1>Django Administration</h1>
            """ + (f'<div class="error">{error}</div>' if error else '') + """
            <form method="post">
                <div class="form-group">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username" required autofocus>
                </div>
                <div class="form-group">
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <button type="submit">Log in</button>
            </form>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)
