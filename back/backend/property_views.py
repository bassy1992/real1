"""
Property management views
"""
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from properties.models import Property, PropertyImage
import json


@login_required(login_url='/admin/login/')
def properties_list(request):
    """List all properties"""
    
    properties = Property.objects.all().order_by('-created_at')
    
    rows = ""
    for prop in properties:
        rows += f"""
        <tr>
            <td>{prop.id}</td>
            <td>{prop.title}</td>
            <td>{prop.location}</td>
            <td>${prop.price:,.0f}</td>
            <td>{prop.property_type}</td>
            <td>{prop.status}</td>
            <td>{prop.beds}/{prop.baths}</td>
            <td>
                <a href="/admin/properties/{prop.id}/edit/" class="btn btn-sm btn-primary">Edit</a>
                <a href="/admin/properties/{prop.id}/delete/" class="btn btn-sm btn-danger" onclick="return confirm('Are you sure?')">Delete</a>
            </td>
        </tr>
        """
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Property Management</title>
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
                display: flex;
                justify-content: space-between;
                align-items: center;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .header h1 {{
                color: #333;
                font-size: 24px;
            }}
            .btn {{
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
                text-decoration: none;
                display: inline-block;
                margin-right: 5px;
            }}
            .btn-primary {{
                background: #417690;
                color: white;
            }}
            .btn-primary:hover {{
                background: #2e5266;
            }}
            .btn-danger {{
                background: #dc3545;
                color: white;
            }}
            .btn-danger:hover {{
                background: #c82333;
            }}
            .btn-secondary {{
                background: #6c757d;
                color: white;
            }}
            .btn-secondary:hover {{
                background: #5a6268;
            }}
            .btn-sm {{
                padding: 5px 10px;
                font-size: 12px;
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
            }}
            td {{
                padding: 15px;
                border-bottom: 1px solid #dee2e6;
                color: #555;
            }}
            tr:hover {{
                background: #f8f9fa;
            }}
            .back-link {{
                color: #417690;
                text-decoration: none;
                font-size: 14px;
            }}
            .back-link:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div>
                    <a href="/admin/dashboard/" class="back-link">← Back to Dashboard</a>
                    <h1>Property Management</h1>
                </div>
                <a href="/admin/properties/create/" class="btn btn-primary">+ Add Property</a>
            </div>
            
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Title</th>
                            <th>Location</th>
                            <th>Price</th>
                            <th>Type</th>
                            <th>Status</th>
                            <th>Beds/Baths</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows if rows else '<tr><td colspan="8" style="text-align: center; padding: 40px;">No properties found</td></tr>'}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)


@login_required(login_url='/admin/login/')
def property_detail(request, property_id):
    """View property details"""
    
    try:
        prop = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        return HttpResponse("Property not found", status=404)
    
    images = prop.uploaded_images.all()
    images_html = ""
    for img in images:
        images_html += f"""
        <div style="margin-bottom: 10px;">
            <img src="{img.get_image_url()}" style="max-width: 200px; max-height: 150px; border-radius: 4px;">
            <p style="margin: 5px 0; font-size: 12px; color: #666;">{img.caption}</p>
        </div>
        """
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{prop.title} - Property Details</title>
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
                max-width: 1000px;
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
                font-size: 28px;
                margin-top: 10px;
            }}
            .details {{
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .detail-row {{
                display: grid;
                grid-template-columns: 200px 1fr;
                margin-bottom: 20px;
                padding-bottom: 20px;
                border-bottom: 1px solid #eee;
            }}
            .detail-row:last-child {{
                border-bottom: none;
            }}
            .detail-label {{
                font-weight: 600;
                color: #333;
            }}
            .detail-value {{
                color: #555;
            }}
            .images-section {{
                margin-top: 30px;
                padding-top: 30px;
                border-top: 2px solid #eee;
            }}
            .images-section h3 {{
                color: #333;
                margin-bottom: 15px;
            }}
            .btn {{
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 14px;
                text-decoration: none;
                display: inline-block;
                margin-right: 5px;
                margin-top: 20px;
            }}
            .btn-primary {{
                background: #417690;
                color: white;
            }}
            .btn-primary:hover {{
                background: #2e5266;
            }}
            .btn-danger {{
                background: #dc3545;
                color: white;
            }}
            .btn-danger:hover {{
                background: #c82333;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <a href="/admin/properties/" class="back-link">← Back to Properties</a>
                <h1>{prop.title}</h1>
            </div>
            
            <div class="details">
                <div class="detail-row">
                    <div class="detail-label">Location</div>
                    <div class="detail-value">{prop.location}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label">Price</div>
                    <div class="detail-value">${prop.price:,.0f}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label">Type</div>
                    <div class="detail-value">{prop.property_type}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label">Status</div>
                    <div class="detail-value">{prop.status}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label">Bedrooms</div>
                    <div class="detail-value">{prop.beds}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label">Bathrooms</div>
                    <div class="detail-value">{prop.baths}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label">Square Feet</div>
                    <div class="detail-value">{prop.sqft:,}</div>
                </div>
                <div class="detail-row">
                    <div class="detail-label">Description</div>
                    <div class="detail-value">{prop.description}</div>
                </div>
                
                {f'<div class="images-section"><h3>Images ({len(images)})</h3>{images_html}</div>' if images else ''}
                
                <div>
                    <a href="/admin/properties/{prop.id}/edit/" class="btn btn-primary">Edit</a>
                    <a href="/admin/properties/{prop.id}/delete/" class="btn btn-danger" onclick="return confirm('Are you sure?')">Delete</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html)
