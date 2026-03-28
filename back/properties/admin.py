from django.contrib import admin
from django.utils.html import format_html
from django.contrib import messages
from .models import Property, PropertyImage


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    fields = ['image', 'url', 'caption', 'order']
    list_per_page = 10


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'price', 'property_type', 'status', 'beds', 'baths', 'sqft']
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


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ['property', 'order', 'caption', 'created_at']
    list_filter = ['property', 'created_at']
    search_fields = ['property__title', 'caption']
    readonly_fields = ['created_at']
    list_per_page = 50
    
    fieldsets = (
        (None, {
            'fields': ('property', 'image', 'url')
        }),
        ('Display Options', {
            'fields': ('caption', 'order')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

