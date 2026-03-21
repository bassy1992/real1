from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import display
from .models import Property, PropertyImage


class PropertyImageInline(TabularInline):
    model = PropertyImage
    extra = 1
    fields = ['image', 'url', 'caption', 'order']
    tab = True


@admin.register(Property)
class PropertyAdmin(ModelAdmin):
    list_display = ['title', 'location', 'price_formatted', 'property_type', 'status', 'beds', 'baths', 'sqft']
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


@admin.register(PropertyImage)
class PropertyImageAdmin(ModelAdmin):
    list_display = ['property', 'thumbnail', 'order', 'caption', 'created_at']
    list_filter = ['property', 'created_at']
    search_fields = ['property__title', 'caption']
    readonly_fields = ['created_at', 'preview']
    list_per_page = 50
    
    fieldsets = (
        (None, {
            'fields': ('property', 'image', 'url', 'preview')
        }),
        ('Display Options', {
            'fields': ('caption', 'order')
        }),
        ('Metadata', {
            'fields': ('created_at',),
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
    
    @display(description="Preview")
    def preview(self, obj):
        url = obj.get_image_url()
        if url:
            return format_html(
                '<img src="{}" style="max-width:400px;max-height:300px;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1);" />',
                url
            )
        return "No image available"
