from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from properties.models import Property


class InvestmentOpportunity(models.Model):
    INVESTMENT_TYPES = [
        ('Fractional', 'Fractional Ownership'),
        ('Full', 'Full Ownership'),
        ('Development', 'Development Project'),
        ('REIT', 'Real Estate Investment Trust'),
    ]
    
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Funded', 'Fully Funded'),
        ('Closed', 'Closed'),
        ('Coming Soon', 'Coming Soon'),
    ]
    
    RISK_LEVELS = [
        ('Low', 'Low Risk'),
        ('Medium', 'Medium Risk'),
        ('High', 'High Risk'),
    ]
    
    property_ref = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='investment_opportunities')
    title = models.CharField(max_length=200)
    investment_type = models.CharField(max_length=50, choices=INVESTMENT_TYPES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Active')
    risk_level = models.CharField(max_length=20, choices=RISK_LEVELS, default='Medium')
    
    # Financial details
    total_investment_needed = models.DecimalField(max_digits=15, decimal_places=2)
    minimum_investment = models.DecimalField(max_digits=15, decimal_places=2)
    current_funding = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    # Returns
    projected_annual_return = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    projected_appreciation = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)])
    investment_term_months = models.IntegerField()
    
    # Details
    description = models.TextField()
    highlights = models.JSONField(default=list)
    financial_projections = models.JSONField(default=dict)
    documents = models.JSONField(default=list)
    
    # Dates
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.investment_type}"

    
    @property
    def funding_percentage(self):
        if self.total_investment_needed > 0:
            return float((self.current_funding / self.total_investment_needed) * 100)
        return 0
    
    @property
    def remaining_investment(self):
        return self.total_investment_needed - self.current_funding
    
    class Meta:
        verbose_name_plural = "Investment Opportunities"
        ordering = ['-created_at']


class Investor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    accredited = models.BooleanField(default=False)
    total_invested = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Investment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name='investments')
    opportunity = models.ForeignKey(InvestmentOpportunity, on_delete=models.CASCADE, related_name='investments')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    ownership_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    investment_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.investor.name} - {self.opportunity.title} - ${self.amount}"
    
    class Meta:
        ordering = ['-investment_date']
