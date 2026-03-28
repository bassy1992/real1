from django.contrib import admin
from .models import InvestmentOpportunity, Investor, Investment


@admin.register(InvestmentOpportunity)
class InvestmentOpportunityAdmin(admin.ModelAdmin):
    list_display = ['title', 'investment_type', 'status', 'risk_level', 'total_investment_needed', 'current_funding']
    list_filter = ['investment_type', 'status', 'risk_level', 'start_date']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 20
    date_hierarchy = 'start_date'
    
    fieldsets = (
        (None, {
            'fields': ('property_ref', 'title', 'description')
        }),
        ('Investment Configuration', {
            'fields': (('investment_type', 'status', 'risk_level'),)
        }),
        ('Financial Details', {
            'fields': (
                ('total_investment_needed', 'minimum_investment', 'current_funding'),
                ('projected_annual_return', 'projected_appreciation', 'investment_term_months')
            )
        }),
        ('Timeline', {
            'fields': (('start_date', 'end_date'),)
        }),
        ('Additional Data', {
            'fields': ('highlights', 'financial_projections', 'documents'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'accredited', 'total_invested', 'created_at']
    list_filter = ['accredited', 'created_at']
    search_fields = ['name', 'email', 'phone']
    readonly_fields = ['created_at']
    list_per_page = 20
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Investor Status', {
            'fields': ('accredited', 'total_invested')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ['investor', 'opportunity', 'amount', 'ownership_percentage', 'status', 'investment_date']
    list_filter = ['status', 'investment_date']
    search_fields = ['investor__name', 'opportunity__title']
    readonly_fields = ['investment_date']
    list_per_page = 20
    date_hierarchy = 'investment_date'
    
    fieldsets = (
        ('Investment Parties', {
            'fields': ('investor', 'opportunity')
        }),
        ('Investment Terms', {
            'fields': (('amount', 'ownership_percentage'), 'status')
        }),
        ('Additional Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('investment_date',),
            'classes': ('collapse',)
        }),
    )

