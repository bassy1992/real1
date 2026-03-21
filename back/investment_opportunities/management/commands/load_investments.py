from django.core.management.base import BaseCommand
from investment_opportunities.models import InvestmentOpportunity
from properties.models import Property
from datetime import date, timedelta
from decimal import Decimal


class Command(BaseCommand):
    help = 'Load sample investment opportunities'

    def handle(self, *args, **kwargs):
        InvestmentOpportunity.objects.all().delete()
        
        properties = Property.objects.all()
        if not properties.exists():
            self.stdout.write(self.style.ERROR('No properties found. Run load_properties first.'))
            return
        
        opportunities_data = [
            {
                'property_ref': properties[0],
                'title': 'Azure Bay Villa - Fractional Ownership',
                'investment_type': 'Fractional',
                'status': 'Active',
                'risk_level': 'Low',
                'total_investment_needed': Decimal('12500000'),
                'minimum_investment': Decimal('250000'),
                'current_funding': Decimal('8750000'),
                'projected_annual_return': Decimal('8.5'),
                'projected_appreciation': Decimal('12.0'),
                'investment_term_months': 60,
                'description': 'Own a piece of this stunning Malibu oceanfront estate. Fractional ownership allows you to enjoy luxury coastal living with professional property management and guaranteed rental income.',
                'highlights': [
                    'Prime Malibu beachfront location',
                    'Professional property management included',
                    'Guaranteed 30 days annual usage',
                    'Rental income distribution',
                    'Exit strategy after 5 years'
                ],
                'financial_projections': {
                    'year_1': {'rental_income': 425000, 'expenses': 175000, 'net_income': 250000},
                    'year_3': {'rental_income': 485000, 'expenses': 190000, 'net_income': 295000},
                    'year_5': {'rental_income': 550000, 'expenses': 210000, 'net_income': 340000}
                },
                'documents': ['Prospectus.pdf', 'Financial_Analysis.pdf', 'Legal_Agreement.pdf'],
                'start_date': date.today(),
                'end_date': date.today() + timedelta(days=1825)
            },
            {
                'property_ref': properties[1] if len(properties) > 1 else properties[0],
                'title': 'Manhattan Skyline Penthouse REIT',
                'investment_type': 'REIT',
                'status': 'Active',
                'risk_level': 'Medium',
                'total_investment_needed': Decimal('15000000'),
                'minimum_investment': Decimal('50000'),
                'current_funding': Decimal('12500000'),
                'projected_annual_return': Decimal('10.2'),
                'projected_appreciation': Decimal('15.5'),
                'investment_term_months': 36,
                'description': 'Invest in a diversified portfolio of luxury Manhattan penthouses through our REIT structure. Professional management with quarterly distributions.',
                'highlights': [
                    'Diversified NYC luxury portfolio',
                    'Quarterly dividend distributions',
                    'SEC-registered REIT',
                    'Liquidity after 12 months',
                    'Tax-advantaged structure'
                ],
                'financial_projections': {
                    'year_1': {'rental_income': 1800000, 'expenses': 650000, 'net_income': 1150000},
                    'year_2': {'rental_income': 1950000, 'expenses': 680000, 'net_income': 1270000},
                    'year_3': {'rental_income': 2100000, 'expenses': 710000, 'net_income': 1390000}
                },
                'documents': ['REIT_Prospectus.pdf', 'Portfolio_Overview.pdf', 'Tax_Benefits.pdf'],
                'start_date': date.today() - timedelta(days=30),
                'end_date': date.today() + timedelta(days=1065)
            },
            {
                'property_ref': properties[3] if len(properties) > 3 else properties[0],
                'title': 'Dubai Oasis Estate Development',
                'investment_type': 'Development',
                'status': 'Active',
                'risk_level': 'High',
                'total_investment_needed': Decimal('25000000'),
                'minimum_investment': Decimal('500000'),
                'current_funding': Decimal('18000000'),
                'projected_annual_return': Decimal('18.5'),
                'projected_appreciation': Decimal('35.0'),
                'investment_term_months': 48,
                'description': 'Ground-floor opportunity in Dubai\'s most exclusive development. High returns with architectural innovation in the heart of the desert.',
                'highlights': [
                    'Prime Dubai location',
                    'Award-winning architecture',
                    'Pre-construction pricing',
                    'Government incentives',
                    'Exit at completion or hold'
                ],
                'financial_projections': {
                    'year_1': {'development_costs': 8000000, 'pre_sales': 3000000, 'net': -5000000},
                    'year_2': {'development_costs': 12000000, 'pre_sales': 15000000, 'net': 3000000},
                    'year_4': {'completion_value': 45000000, 'total_costs': 25000000, 'net': 20000000}
                },
                'documents': ['Development_Plan.pdf', 'Architectural_Renders.pdf', 'Market_Analysis.pdf'],
                'start_date': date.today() - timedelta(days=60),
                'end_date': date.today() + timedelta(days=1460)
            },
            {
                'property_ref': properties[2] if len(properties) > 2 else properties[0],
                'title': 'Cotswold Manor Full Acquisition',
                'investment_type': 'Full',
                'status': 'Coming Soon',
                'risk_level': 'Low',
                'total_investment_needed': Decimal('8900000'),
                'minimum_investment': Decimal('8900000'),
                'current_funding': Decimal('0'),
                'projected_annual_return': Decimal('6.5'),
                'projected_appreciation': Decimal('8.0'),
                'investment_term_months': 120,
                'description': 'Exclusive opportunity to acquire a historic 17th-century manor. Perfect for family office or private estate with strong appreciation potential.',
                'highlights': [
                    'Historic Grade II listed property',
                    'Fully restored with modern amenities',
                    '50 acres of pristine grounds',
                    'Equestrian facilities',
                    'Strong UK property market'
                ],
                'financial_projections': {
                    'year_1': {'rental_income': 180000, 'expenses': 120000, 'net_income': 60000},
                    'year_5': {'rental_income': 220000, 'expenses': 135000, 'net_income': 85000},
                    'year_10': {'property_value': 11500000, 'appreciation': 2600000}
                },
                'documents': ['Property_Survey.pdf', 'Historical_Documentation.pdf', 'Valuation_Report.pdf'],
                'start_date': date.today() + timedelta(days=30),
                'end_date': date.today() + timedelta(days=3680)
            }
        ]
        
        for data in opportunities_data:
            InvestmentOpportunity.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(opportunities_data)} investment opportunities'))
