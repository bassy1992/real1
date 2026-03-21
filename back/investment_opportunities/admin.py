from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import InvestmentOpportunity, Investor, Investment


@admin.register(InvestmentOpportunity)
class InvestmentOpportunityAdmin(ModelAdmin):
    list_display = ['title', 'investment_type', 'status', 'risk_level', 'total_needed', 'current_funding', 'funding_bar']
    list_filter = ['investment_type', 'status', 'risk_level', 'start_date']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at', 'funding_percentage', 'remaining_investment']
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
        ('Calculated Fields', {
            'fields': ('funding_percentage', 'remaining_investment'),
            'classes': ('collapse',)
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
    
    @display(description="Total Needed", ordering="total_investment_needed")
    def total_needed(self, obj):
        return format_html('<span style="font-weight:500;">${}</span>', f'{obj.total_investment_needed:,.0f}')
    
    @display(description="Current Funding", ordering="current_funding")
    def current_funding(self, obj):
        return format_html('<span style="font-weight:500;">${}</span>', f'{obj.current_funding:,.0f}')
    
    @display(description="Funding Progress")
    def funding_bar(self, obj):
        percentage = obj.funding_percentage
        color = "#f59e0b" if percentage < 50 else "#10b981" if percentage < 100 else "#3b82f6"
        return format_html(
            '<div style="width:120px;background:#f3f4f6;border-radius:6px;overflow:hidden;height:24px;position:relative;">'
            '<div style="width:{}%;background:{};height:100%;transition:width 0.3s;"></div>'
            '<span style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:11px;font-weight:600;color:#1f2937;">{:.0f}%</span>'
            '</div>',
            min(percentage, 100), color, percentage
        )


@admin.register(Investor)
class InvestorAdmin(ModelAdmin):
    list_display = ['name', 'email', 'phone', 'accredited', 'total_invested_display', 'created_at']
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
    
    @display(description="Total Invested", ordering="total_invested")
    def total_invested_display(self, obj):
        return format_html('<span style="font-weight:500;color:#059669;">${}</span>', f'{obj.total_invested:,.2f}')


@admin.register(Investment)
class InvestmentAdmin(ModelAdmin):
    list_display = ['investor', 'opportunity', 'amount_display', 'ownership_percentage', 'status', 'investment_date']
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
    
    @display(description="Amount", ordering="amount")
    def amount_display(self, obj):
        return format_html('<span style="font-weight:500;color:#059669;">${}</span>', f'{obj.amount:,.2f}')
