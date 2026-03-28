# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User's Browser                          │
│                    https://bellrockholdings.org                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTPS
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Vercel (Frontend)                          │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  React + TypeScript + Vite                               │  │
│  │  - Home Page                                             │  │
│  │  - Properties Page                                       │  │
│  │  - Investments Page                                      │  │
│  │  - Contact Page                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Environment Variables:                                         │
│  - VITE_API_BASE_URL=https://real-production-4319...           │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ API Calls (HTTPS)
                             │ /api/properties/
                             │ /api/investments/opportunities/
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              Railway (Backend)                                  │
│         https://real-production-4319.up.railway.app             │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Django REST Framework                                   │  │
│  │  - Properties API                                        │  │
│  │  - Investments API                                       │  │
│  │  - Admin Panel                                           │  │
│  │  - CORS Middleware                                       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Environment Variables:                                         │
│  - CORS_ALLOWED_ORIGINS=https://bellrockholdings.org           │
│  - ALLOWED_HOSTS=real-production-4319.up.railway.app           │
│  - DATABASE_URL=postgresql://...                               │
│  - DO_SPACES_KEY=...                                           │
└────────────┬────────────────────────────┬───────────────────────┘
             │                            │
             │                            │
             ▼                            ▼
┌─────────────────────────┐  ┌──────────────────────────────────┐
│  Railway PostgreSQL     │  │  DigitalOcean Spaces             │
│  (Database)             │  │  (Media Storage)                 │
│                         │  │                                  │
│  - Properties           │  │  - Property Images               │
│  - Investments          │  │  - Investment Documents          │
│  - Investors            │  │  - Static Assets                 │
│  - Users                │  │                                  │
└─────────────────────────┘  └──────────────────────────────────┘
```

## Data Flow

### 1. User Visits Website
```
User → bellrockholdings.org → Vercel serves React app
```

### 2. Frontend Loads Data
```
React App → API_BASE_URL → Railway Backend → PostgreSQL
                                          → DigitalOcean Spaces
```

### 3. Backend Returns Data
```
PostgreSQL → Django → REST API → JSON Response → React App → User
```

## API Endpoints

### Properties
- `GET /api/properties/` - List all properties
- `GET /api/properties/{id}/` - Get property details
- `GET /api/properties/by_status/?status=For Sale` - Filter by status
- `GET /api/properties/by_type/?type=Villa` - Filter by type

### Investments
- `GET /api/investments/opportunities/` - List all opportunities
- `GET /api/investments/opportunities/active/` - Active opportunities only
- `GET /api/investments/opportunities/{id}/` - Get opportunity details
- `GET /api/investments/opportunities/by_type/?type=Fractional` - Filter by type

## Security

### CORS Configuration
```python
CORS_ALLOWED_ORIGINS = [
    'https://bellrockholdings.org',
    'https://www.bellrockholdings.org',
    'http://localhost:5173',  # Development
]
```

### HTTPS
- ✅ Railway: Automatic SSL/TLS
- ✅ Vercel: Automatic SSL/TLS
- ✅ DigitalOcean Spaces: CDN with HTTPS

### Environment Variables
- Secrets stored in Railway/Vercel dashboards
- Never committed to Git
- Different values for dev/prod

## Deployment Pipeline

### Backend (Railway)
```
Git Push → Railway detects changes → Build → Deploy → Health Check
```

### Frontend (Vercel)
```
Git Push → Vercel detects changes → Build → Deploy → Preview URL
```

## Monitoring

### Railway
- Application logs
- Database metrics
- CPU/Memory usage
- Request/Response times

### Vercel
- Deployment logs
- Function execution times
- Bandwidth usage
- Error tracking

## Scalability

### Current Setup
- Railway: Shared CPU, 512MB RAM
- Vercel: Serverless functions
- PostgreSQL: Railway managed
- DigitalOcean Spaces: CDN enabled

### Future Scaling Options
- Railway: Upgrade to dedicated CPU
- Database: Add read replicas
- CDN: Add Cloudflare for additional caching
- Caching: Add Redis for API responses

## Backup Strategy

### Database
- Railway automatic daily backups
- Manual backups before major changes
- Export data regularly

### Media Files
- DigitalOcean Spaces versioning
- Regular snapshots
- Cross-region replication (optional)

## Development Workflow

### Local Development
```
Frontend: npm run dev (localhost:5173)
Backend: python manage.py runserver (localhost:8000)
Database: SQLite (local) or PostgreSQL (Docker)
```

### Staging (Optional)
```
Frontend: Vercel preview deployments
Backend: Railway staging environment
Database: Separate staging database
```

### Production
```
Frontend: bellrockholdings.org (Vercel)
Backend: real-production-4319.up.railway.app (Railway)
Database: Railway PostgreSQL
```

## Cost Breakdown

### Railway
- Hobby Plan: $5/month
- PostgreSQL: Included
- Bandwidth: 100GB included

### Vercel
- Hobby Plan: Free
- Pro Plan: $20/month (if needed)
- Bandwidth: 100GB included

### DigitalOcean Spaces
- $5/month for 250GB storage
- $0.01/GB for bandwidth over 1TB

### Total Estimated Cost
- Minimum: $10/month (Railway + DO Spaces)
- Recommended: $35/month (Railway Pro + Vercel Pro + DO Spaces)
