from rest_framework import serializers
from .models import InvestmentOpportunity, Investor, Investment
from properties.serializers import PropertySerializer


class InvestmentOpportunitySerializer(serializers.ModelSerializer):
    property_details = PropertySerializer(source='property_ref', read_only=True)
    funding_percentage = serializers.ReadOnlyField()
    remaining_investment = serializers.ReadOnlyField()
    
    class Meta:
        model = InvestmentOpportunity
        fields = [
            'id', 'property_ref', 'property_details', 'title', 'investment_type', 
            'status', 'risk_level', 'total_investment_needed', 'minimum_investment',
            'current_funding', 'funding_percentage', 'remaining_investment',
            'projected_annual_return', 'projected_appreciation', 'investment_term_months',
            'description', 'highlights', 'financial_projections', 'documents',
            'start_date', 'end_date', 'created_at', 'updated_at'
        ]


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ['id', 'name', 'email', 'phone', 'accredited', 'total_invested', 'created_at']


class InvestmentSerializer(serializers.ModelSerializer):
    investor_details = InvestorSerializer(source='investor', read_only=True)
    opportunity_details = InvestmentOpportunitySerializer(source='opportunity', read_only=True)
    
    class Meta:
        model = Investment
        fields = [
            'id', 'investor', 'investor_details', 'opportunity', 'opportunity_details',
            'amount', 'status', 'ownership_percentage', 'investment_date', 'notes'
        ]
