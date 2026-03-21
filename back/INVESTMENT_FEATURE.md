# Investment Opportunities Feature

## Overview
A comprehensive investment platform for luxury real estate opportunities including fractional ownership, full acquisitions, development projects, and REITs.

## Features

### Investment Types
- **Fractional Ownership**: Share ownership of luxury properties
- **Full Ownership**: Complete property acquisition
- **Development Projects**: Ground-floor development opportunities
- **REIT**: Real Estate Investment Trust portfolios

### Risk Levels
- Low Risk: Stable, established properties
- Medium Risk: Balanced risk/reward opportunities
- High Risk: High-return development projects

### Investment Details
- Minimum investment amounts
- Projected annual returns
- Projected appreciation rates
- Investment terms (months/years)
- Funding progress tracking
- Financial projections

## API Endpoints

### Get All Opportunities
```
GET /api/investments/opportunities/
```

### Get Active Opportunities
```
GET /api/investments/opportunities/active/
```

### Get Opportunity by ID
```
GET /api/investments/opportunities/{id}/
```

### Filter by Type
```
GET /api/investments/opportunities/by_type/?type=Fractional
```

### Filter by Risk
```
GET /api/investments/opportunities/by_risk/?risk=Low
```

## Database Models

### InvestmentOpportunity
- Links to Property model
- Financial details (total needed, minimum, current funding)
- Returns (annual return %, appreciation %)
- Investment term
- Highlights and documents
- Status tracking

### Investor
- Investor profile
- Accreditation status
- Total invested amount

### Investment
- Links investor to opportunity
- Investment amount
- Ownership percentage
- Status tracking

## Sample Data
Run the management command to load sample investment opportunities:
```bash
python manage.py load_investments
```

This creates 4 diverse investment opportunities:
1. Azure Bay Villa - Fractional Ownership (70% funded)
2. Manhattan Penthouse REIT (83% funded)
3. Dubai Development Project (72% funded)
4. Cotswold Manor Full Acquisition (Coming Soon)

## Frontend Integration
The frontend displays:
- Investment cards with key metrics
- Funding progress bars
- Risk and status badges
- Detailed modal views
- Filter by type and risk level
- Financial projections
- Key highlights

## Admin Interface
Access at `/admin/` to:
- Manage investment opportunities
- Track investor profiles
- Monitor investments
- Update funding progress
