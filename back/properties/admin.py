from django.contrib import admin
from django.utils.html import format_html
from django.contrib import messages
from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import display
from .models import Property, PropertyImage


class PropertyImageInline(TabularInline):
    model = PropertyImage
    extra = 1
    fields = ['image', 'url', 'caption', 'order', 'preview_thumbnail']
    readonly_fields = ['preview_thumbnail']
    tab = True
    
    @display(description="Preview")
    def preview_thumbnail(self, obj):
        if obj.pk:  # Only show for existing objects
            url = obj.get_image_url()
            if url:
                return format_html(
                    '<img src="{}" style="max-width:150px;max-height:100px;object-fit:cover;border-radius:4px;" />',
                    url
                )
        return "—"


@admin.register(Property)
class PropertyAdmin(ModelAdmin):
    list_display = ['title', 'location', 'price_formatted', 'property_type', 'status', 'beds', 'baths', 'sqft', 'image_count']
    list_filter = ['property_type', 'status', 'beds', 'baths']
    search_fields = ['title', 'location', 'description']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [PropertyImageInline]
    list_per_page = 20
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'location')
        }),
        ('Property Details', {
            'fields': (('property_type', 'status'), ('beds', 'baths', 'sqft'), 'price')
        }),
        ('Location Coordinates', {
            'fields': (('latitude', 'longitude'),)
        }),
        ('Additional Information', {
            'fields': ('amenities', 'images'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    @display(description="Price", ordering="price")
    def price_formatted(self, obj):
        return format_html('<span style="font-weight:500;">${}</span>', f'{obj.price:,}')
    
    @display(description="Images")
    def image_count(self, obj):
        count = obj.uploaded_images.count()
        if count > 0:
            return format_html('<span style="color:#10b981;font-weight:500;">{} images</span>', count)
        return format_html('<span style="color:#6b7280;">No images</span>')
    
    def delete_model(self, request, obj):
        """Override to show message about image deletion"""
        image_count = obj.uploaded_images.count()
        super().delete_model(request, obj)
        if image_count > 0:
            messages.success(
                request,
                f'Property "{obj.title}" and {image_count} associated image(s) deleted from database and DigitalOcean Spaces.'
            )


@admin.register(PropertyImage)
class PropertyImageAdmin(ModelAdmin):
    list_display = ['property', 'thumbnail', 'order', 'caption', 'storage_type', 'created_at']
    list_filter = ['property', 'created_at']
    search_fields = ['property__title', 'caption']
    readonly_fields = ['created_at', 'preview', 'storage_info']
    list_per_page = 50
    
    fieldsets = (
        (None, {
            'fields': ('property', 'image', 'url', 'preview')
        }),
        ('Display Options', {
            'fields': ('caption', 'order')
        }),
        ('Metadata', {
            'fields': ('storage_info', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    @display(description="Thumbnail")
    def thumbnail(self, obj):
        url = obj.get_image_url()
        if url:
            return format_html(
                '<img src="{}" style="width:60px;height:40px;object-fit:cover;border-radius:4px;" />',
                url
            )
        return "—"
    
    @display(description="Type")
    def storage_type(self, obj):
        if obj.image:
            return format_html('<span style="color:#10b981;">📁 Uploaded</span>')
        elif obj.url:
            return format_html('<span style="color:#3b82f6;">🔗 External URL</span>')
        return "—"
    
    @display(description="Preview")
    def preview(self, obj):
        url = obj.get_image_url()
        if url:
            return format_html(
                '<img src="{}" style="max-width:400px;max-height:300px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1);" />',
                url
            )
        return "No image available"
    
    @display(description="Storage Information")
    def storage_info(self, obj):
        if obj.image:
            return format_html(
                '<div style="padding:10px;background:#f3f4f6;border-radius:6px;">'
                '<strong>File:</strong> {}<br>'
                '<strong>URL:</strong> <a href="{}" target="_blank">{}</a><br>'
                '<strong>Storage:</strong> DigitalOcean Spaces<br>'
                '<span style="color:#ef4444;">⚠️ Deleting this record will also delete the file from DigitalOcean Spaces</span>'
                '</div>',
                obj.image.name,
                obj.image.url,
                obj.image.url
            )
        elif obj.url:
            return format_html(
                '<div style="padding:10px;background:#f3f4f6;border-radius:6px;">'
                '<strong>External URL:</strong> <a href="{}" target="_blank">{}</a><br>'
                '<span style="color:#3b82f6;">ℹ️ This is an external URL and won\'t be deleted</span>'
                '</div>',
                obj.url,
                obj.url
            )
        return "No storage information available"
    
    def delete_model(self, request, obj):
        """Override to show message about file deletion"""
        property_title = obj.property.title
        has_file = bool(obj.image)
        super().delete_model(request, obj)
        if has_file:
            messages.success(
                request,
                f'Image for "{property_title}" deleted from database and DigitalOcean Spaces.'
            )
    
    def delete_queryset(self, request, queryset):
        """Override bulk delete to show message"""
        count = queryset.count()
        files_count = queryset.filter(image__isnull=False).count()
        super().delete_queryset(request, queryset)
        if files_count > 0:
            messages.success(
                request,
                f'{count} image record(s) deleted. {files_count} file(s) removed from DigitalOcean Spaces.'
            )
