from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import InvestmentOpportunity, Investor, Investment
from .serializers import InvestmentOpportunitySerializer, InvestorSerializer, InvestmentSerializer


class InvestmentOpportunityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvestmentOpportunity.objects.all()
    serializer_class = InvestmentOpportunitySerializer
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all active investment opportunities"""
        opportunities = InvestmentOpportunity.objects.filter(status='Active')
        serializer = self.get_serializer(opportunities, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_type(self, request):
        """Filter opportunities by investment type"""
        investment_type = request.query_params.get('type', None)
        if investment_type:
            opportunities = InvestmentOpportunity.objects.filter(investment_type=investment_type)
        else:
            opportunities = InvestmentOpportunity.objects.all()
        serializer = self.get_serializer(opportunities, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_risk(self, request):
        """Filter opportunities by risk level"""
        risk_level = request.query_params.get('risk', None)
        if risk_level:
            opportunities = InvestmentOpportunity.objects.filter(risk_level=risk_level)
        else:
            opportunities = InvestmentOpportunity.objects.all()
        serializer = self.get_serializer(opportunities, many=True)
        return Response(serializer.data)


class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer


class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
