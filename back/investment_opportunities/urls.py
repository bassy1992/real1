from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvestmentOpportunityViewSet, InvestorViewSet, InvestmentViewSet

router = DefaultRouter()
router.register(r'opportunities', InvestmentOpportunityViewSet, basename='investment-opportunity')
router.register(r'investors', InvestorViewSet, basename='investor')
router.register(r'investments', InvestmentViewSet, basename='investment')

urlpatterns = [
    path('', include(router.urls)),
]
