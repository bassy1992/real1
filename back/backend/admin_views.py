"""
Custom admin dashboard views
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from properties.models import Property, PropertyImage
from investment_opportunities.models import InvestmentOpportunity, Investor, Investment
from users.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required(login_url='/admin/login/')
def admin_dashboard(request):
    """Admin dashboard with management options"""
    
    # Get statistics
    properties_count = Property.objects.count()
    property_images_count = PropertyImage.objects.count()
    opportunities_count = InvestmentOpportunity.objects.count()
    investors_count = Investor.objects.count()
    investments_count = Investment.objects.count()
    users_count = User.objects.count()
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin Dashboard</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                background: #f8f9fa;
                padding: 20px;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
            }}
            .header {{
                background: white;
                padding: 30px;
                border-radius: 8px;
                margin-bottom: 30px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}
            .header h1 {{
                color: #333;
                font-size: 28px;
            }}
            .user-info {{
                text-align: right;
                color: #666;
            }}
            .user-info p {{
                margin: 5px 0;
                font-size: 14px;
            }}
            .logout-btn {{
                background: #dc3545;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
                margin-top: 10px;
            }}
            .logout-btn:hover {{
                background: #c82333;
            }}
            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}
            .stat-card {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                text-align: center;
            }}
            .stat-card h3 {{
                color: #666;
                font-size: 14px;
                margin-bottom: 10px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }}
            .stat-card .number {{
                font-size: 32px;
                font-weight: bold;
                color: #417690;
            }}
            .management-section {{
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .management-section h2 {{
                color: #333;
                margin-bottom: 20px;
                font-size: 20px;
            }}
            .management-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
            }}
            .management-btn {{
                background: #417690;
                color: white;
                padding: 15px;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 14px;
                font-weight: 500;
                transition: background 0.3s;
            }}
            .management-btn:hover {{
                background: #2e5266;
            }}
            .management-btn.secondary {{
                background: #6c757d;
            }}
            .management-btn.secondary:hover {{
                background: #5a6268;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div>
                    <h1>Admin Dashboard</h1>
                </div>
                <div class="user-info">
                    <p><strong>{request.user.get_full_name() or request.user.username}</strong></p>
                    <p>{request.user.email}</p>
                    <form method="post" action="/admin/logout/" style="display: inline;">
                        <button type="submit" class="logout-btn">Logout</button>
                    </form>
                </div>
            </div>
            
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Properties</h3>
                    <div class="number">{properties_count}</div>
                </div>
                <div class="stat-card">
                    <h3>Property Images</h3>
                    <div class="number">{property_images_count}</div>
                </div>
                <div class="stat-card">
                    <h3>Investment Opportunities</h3>
                    <div class="number">{opportunities_count}</div>
                </div>
                <div class="stat-card">
                    <h3>Investors</h3>
                    <div class="number">{investors_count}</div>
                </div>
                <div class="stat-card">
                    <h3>Investments</h3>
                    <div class="number">{investments_count}</div>
                </div>
                <div class="stat-card">
                    <h3>Users</h3>
                    <div class="number">{users_count}</div>
                </div>
            </div>
            
            <div class="management-section">
                <h2>Management</h2>
                <div class="management-grid">
                    <button class="management-btn" onclick="alert('Property management coming soon')">Manage Properties</button>
                    <button class="management-btn" onclick="alert('Property images management coming soon')">Manage Images</button>
                    <button class="management-btn" onclick="alert('Investment opportunities management coming soon')">Manage Opportunities</button>
                    <button class="management-btn" onclick="alert('Investors management coming soon')">Manage Investors</button>
                    <button class="management-btn" onclick="alert('Investments management coming soon')">Manage Investments</button>
                    <button class="management-btn secondary" onclick="alert('Users management coming soon')">Manage Users</button>
                </div>
            </div>
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

