"""
Management views for admin dashboard
"""
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from properties.models import Property, PropertyImage
from investment_opportunities.models import InvestmentOpportunity, Investor, Investment
from django.contrib.auth import get_user_model

User = get_user_model()


def render_list_page(title, items, columns, back_url):
    """Generic list page renderer"""
    
    rows = ""
    for item in items:
        row_data = []
        for col in columns:
            value = getattr(item, col, '')
            if isinstance(value, (int, float)):
                row_data.append(f"<td>{value:,}</td>")
            else:
                row_data.append(f"<td>{value}</td>")
        rows += f"<tr>{''.join(row_data)}</tr>"
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
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
                max-width: 1400px;
                margin: 0 auto;
            }}
            .header {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 20px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .back-link {{
                color: #417690;
                text-decoration: none;
                font-size: 14px;
                margin-bottom: 10px;
                display: inline-block;
            }}
            h1 {{
                color: #333;
                font-size: 24px;
                margin-top: 10px;
            }}
            .table-container {{
                background: white;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            th {{
                background: #f8f9fa;
                padding: 15px;
                text-align: left;
                font-weight: 600;
                color: #333;
                border-bottom: 2px solid #dee2e6;
                text-transform: capitalize;
            }}
            td {{
                padding: 15px;
                border-bottom: 1px solid #dee2e6;
                color: #555;
            }}
            tr:hover {{
                background: #f8f9fa;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <a href="{back_url}" class="back-link">← Back</a>
                <h1>{title}</h1>
            </div>
            
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            {''.join([f'<th>{col}</th>' for col in columns])}
                        </tr>
                    </thead>
                    <tbody>
                        {rows if rows else '<tr><td colspan="100" style="text-align: center; padding: 40px;">No items found</td></tr>'}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)


@login_required(login_url='/admin/login/')
def images_list(request):
    """List all property images"""
    images = PropertyImage.objects.all().order_by('-created_at')
    return render_list_page(
        'Property Images',
        images,
        ['id', 'property', 'caption', 'order', 'created_at'],
        '/admin/dashboard/'
    )


@login_required(login_url='/admin/login/')
def opportunities_list(request):
    """List all investment opportunities"""
    opportunities = InvestmentOpportunity.objects.all().order_by('-created_at')
    return render_list_page(
        'Investment Opportunities',
        opportunities,
        ['id', 'title', 'investment_type', 'status', 'risk_level', 'total_investment_needed', 'current_funding'],
        '/admin/dashboard/'
    )


@login_required(login_url='/admin/login/')
def investors_list(request):
    """List all investors"""
    investors = Investor.objects.all().order_by('-created_at')
    return render_list_page(
        'Investors',
        investors,
        ['id', 'name', 'email', 'phone', 'accredited', 'total_invested'],
        '/admin/dashboard/'
    )


@login_required(login_url='/admin/login/')
def investments_list(request):
    """List all investments"""
    investments = Investment.objects.all().order_by('-investment_date')
    return render_list_page(
        'Investments',
        investments,
        ['id', 'investor', 'opportunity', 'amount', 'ownership_percentage', 'status'],
        '/admin/dashboard/'
    )


@login_required(login_url='/admin/login/')
def users_list(request):
    """List all users"""
    users = User.objects.all().order_by('-date_joined')
    return render_list_page(
        'Users',
        users,
        ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser'],
        '/admin/dashboard/'
    )
