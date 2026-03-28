# 🚀 Railway-Vercel Deployment Guide

## Overview

This repository contains a full-stack real estate application with:
- **Frontend:** React + TypeScript + Vite (deployed on Vercel)
- **Backend:** Django + REST Framework (deployed on Railway)
- **Database:** PostgreSQL (Railway)
- **Storage:** DigitalOcean Spaces

## 🎯 Current Setup

- **Frontend URL:** https://bellrockholdings.org
- **Backend URL:** https://real-production-4319.up.railway.app
- **Backend API:** https://real-production-4319.up.railway.app/api

## 📁 Project Structure

```
.
├── back/                          # Django backend
│   ├── backend/                   # Django settings
│   │   └── settings.py           # ✅ Updated with CORS
│   ├── properties/               # Properties app
│   ├── investment_opportunities/ # Investments app
│   └── .env.example              # ✅ Updated with production values
│
├── front/                        # React frontend
│   ├── services/
│   │   ├── propertyService.ts   # ✅ Updated to use centralized API URL
│   │   └── investmentService.ts # ✅ Already using centralized API URL
│   ├── constants.ts              # ✅ Updated with Railway URL
│   └── .env.local                # ✅ Updated with production API URL
│
└── Documentation/
    ├── QUICK_START.md            # 5-minute setup guide
    ├── DEPLOYMENT_CHECKLIST.md   # Detailed deployment steps
    ├── VERCEL_RAILWAY_CONNECTION.md  # Complete connection guide
    ├── ENV_VARIABLES_REFERENCE.md    # Environment variables
    ├── ARCHITECTURE.md           # System architecture
    ├── CONNECTION_SUMMARY.md     # Summary of changes
    ├── DEPLOYMENT_STEPS.txt      # Printable checklist
    └── verify_connection.sh      # Automated testing script
```

## ⚡ Quick Deployment

### 1. Railway (Backend)

Add environment variables:
```bash
CORS_ALLOWED_ORIGINS=https://bellrockholdings.org,https://www.bellrockholdings.org
FRONTEND_URL=https://bellrockholdings.org
ALLOWED_HOSTS=real-production-4319.up.railway.app
DEBUG=False
```

### 2. Vercel (Frontend)

Add environment variable:
```bash
VITE_API_BASE_URL=https://real-production-4319.up.railway.app/api
```

### 3. Test

```bash
./verify_connection.sh
```

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [QUICK_START.md](QUICK_START.md) | Get started in 5 minutes |
| [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md) | Step-by-step deployment guide |
| [VERCEL_RAILWAY_CONNECTION.md](VERCEL_RAILWAY_CONNECTION.md) | Comprehensive connection guide |
| [ENV_VARIABLES_REFERENCE.md](ENV_VARIABLES_REFERENCE.md) | All environment variables explained |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System architecture and data flow |
| [CONNECTION_SUMMARY.md](CONNECTION_SUMMARY.md) | Summary of all changes made |
| [DEPLOYMENT_STEPS.txt](DEPLOYMENT_STEPS.txt) | Printable deployment checklist |

## 🔧 What Was Changed

### Backend Changes
1. Added `bellrockholdings.org` to CORS allowed origins
2. Added Railway domain to `ALLOWED_HOSTS`
3. Enabled `CORS_ALLOW_CREDENTIALS`
4. Updated `.env.example` with production values

### Frontend Changes
1. Updated `constants.ts` with Railway backend URL
2. Made API URL configurable via `VITE_API_BASE_URL`
3. Fixed `propertyService.ts` to use centralized API URL
4. Updated `.env.local` with production API URL

## 🧪 Testing

### Automated Testing
```bash
chmod +x verify_connection.sh
./verify_connection.sh
```

### Manual Testing
```bash
# Test backend
curl https://real-production-4319.up.railway.app/api/properties/
curl https://real-production-4319.up.railway.app/api/investments/opportunities/

# Test frontend
open https://bellrockholdings.org
```

### Browser Testing
1. Visit https://bellrockholdings.org
2. Open DevTools (F12) → Network tab
3. Navigate to Properties/Investments pages
4. Verify API calls go to Railway backend
5. Check Console for errors

## ✅ Success Checklist

- [ ] Backend running on Railway
- [ ] Frontend deployed on Vercel
- [ ] Environment variables configured
- [ ] API endpoints accessible
- [ ] No CORS errors
- [ ] Data loads on frontend
- [ ] Images load from DigitalOcean Spaces

## 🐛 Common Issues

### CORS Errors
**Problem:** Browser shows "CORS policy" errors

**Solution:**
1. Verify Railway has `CORS_ALLOWED_ORIGINS` set
2. Include `https://bellrockholdings.org`
3. Redeploy Railway backend
4. Clear browser cache

### 404 Errors
**Problem:** API calls return 404

**Solution:**
1. Check Vercel `VITE_API_BASE_URL` is correct
2. Verify Railway backend is running
3. Test endpoints with curl
4. Check for trailing slash issues

### Environment Variables Not Working
**Problem:** Frontend still uses localhost

**Solution:**
1. Verify variable starts with `VITE_` prefix
2. Redeploy Vercel after adding variables
3. Clear browser cache and hard refresh
4. Check DevTools → Network tab for actual URLs

## 🔗 Important Links

- **Frontend:** https://bellrockholdings.org
- **Backend API:** https://real-production-4319.up.railway.app/api/
- **Admin Panel:** https://real-production-4319.up.railway.app/admin/
- **Railway Dashboard:** https://railway.app/
- **Vercel Dashboard:** https://vercel.com/

## 📊 API Endpoints

### Properties
- `GET /api/properties/` - List all properties
- `GET /api/properties/{id}/` - Get property details
- `GET /api/properties/by_status/?status=For Sale` - Filter by status
- `GET /api/properties/by_type/?type=Villa` - Filter by type

### Investments
- `GET /api/investments/opportunities/` - List all opportunities
- `GET /api/investments/opportunities/active/` - Active opportunities
- `GET /api/investments/opportunities/{id}/` - Get opportunity details
- `GET /api/investments/opportunities/by_type/?type=Fractional` - Filter by type

## 🔐 Security

- ✅ HTTPS enabled on both Railway and Vercel
- ✅ CORS configured for specific domains only
- ✅ DEBUG=False in production
- ✅ Secrets stored in environment variables
- ✅ Database credentials managed by Railway
- ✅ DigitalOcean Spaces with CDN

## 💰 Cost Estimate

- **Railway:** $5/month (Hobby) or $20/month (Pro)
- **Vercel:** Free (Hobby) or $20/month (Pro)
- **DigitalOcean Spaces:** $5/month
- **Total:** $10-45/month depending on plan

## 🚀 Next Steps

After successful deployment:

1. **Monitoring**
   - Set up error tracking (Sentry)
   - Configure uptime monitoring
   - Set up log aggregation

2. **Performance**
   - Enable CDN for static assets
   - Add Redis caching
   - Optimize database queries

3. **Security**
   - Set up rate limiting
   - Enable DDoS protection
   - Configure security headers

4. **Backup**
   - Automate database backups
   - Set up media file backups
   - Test restore procedures

5. **CI/CD**
   - Set up automated testing
   - Configure deployment pipelines
   - Add staging environment

## 📞 Support

If you encounter issues:
1. Check the relevant documentation file
2. Run `./verify_connection.sh`
3. Review Railway and Vercel logs
4. Check browser DevTools console

## 📝 Notes

- All code changes are complete and tested
- No syntax errors in modified files
- Environment variables need to be set on Railway and Vercel
- Both platforms will auto-deploy after variable changes

---

**Last Updated:** March 28, 2026  
**Status:** ✅ Ready for deployment  
**Version:** 1.0.0
