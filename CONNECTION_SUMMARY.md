# Railway ↔️ Vercel Connection Summary

## 🎯 Objective
Connect Railway backend (https://real-production-4319.up.railway.app/) to Vercel frontend (bellrockholdings.org)

## ✅ What Was Done

### 1. Backend Configuration (Django)
- Added bellrockholdings.org to CORS allowed origins
- Added Railway domain to ALLOWED_HOSTS
- Enabled CORS credentials support
- Updated environment variable examples

### 2. Frontend Configuration (React/Vite)
- Changed API base URL from localhost to Railway backend in `constants.ts`
- Fixed hardcoded localhost URL in `propertyService.ts`
- Made API URL configurable via environment variable
- Added VITE_API_BASE_URL to .env.local
- All services now use centralized API_BASE_URL from constants

### 3. Documentation Created
- `VERCEL_RAILWAY_CONNECTION.md` - Comprehensive connection guide
- `ENV_VARIABLES_REFERENCE.md` - Environment variables reference
- `DEPLOYMENT_CHECKLIST.md` - Step-by-step deployment guide
- `verify_connection.sh` - Automated verification script

## 🚀 Quick Start

### Railway (Backend)
Add these environment variables:
```bash
CORS_ALLOWED_ORIGINS=https://bellrockholdings.org,https://www.bellrockholdings.org
FRONTEND_URL=https://bellrockholdings.org
ALLOWED_HOSTS=real-production-4319.up.railway.app
```

### Vercel (Frontend)
Add this environment variable:
```bash
VITE_API_BASE_URL=https://real-production-4319.up.railway.app/api
```

## 📋 Next Steps

1. **Update Railway environment variables** (see ENV_VARIABLES_REFERENCE.md)
2. **Wait for Railway to redeploy** (automatic, ~2-3 minutes)
3. **Update Vercel environment variables** (see ENV_VARIABLES_REFERENCE.md)
4. **Redeploy Vercel frontend** (automatic if Git-connected)
5. **Test the connection** (run `./verify_connection.sh`)
6. **Verify in browser** (visit https://bellrockholdings.org)

## 🧪 Testing

Run the verification script:
```bash
./verify_connection.sh
```

Or test manually:
```bash
# Test backend
curl https://real-production-4319.up.railway.app/api/properties/

# Test frontend
open https://bellrockholdings.org
```

## 📚 Documentation

- **Full Guide:** `VERCEL_RAILWAY_CONNECTION.md`
- **Environment Variables:** `ENV_VARIABLES_REFERENCE.md`
- **Deployment Steps:** `DEPLOYMENT_CHECKLIST.md`

## ⚡ Current Status

✅ Backend is running on Railway
✅ Backend API endpoints are accessible
✅ Code changes are complete
⏳ Waiting for environment variable updates
⏳ Waiting for deployments

## 🔗 Important URLs

- **Backend:** https://real-production-4319.up.railway.app/
- **Backend API:** https://real-production-4319.up.railway.app/api/
- **Backend Admin:** https://real-production-4319.up.railway.app/admin/
- **Frontend:** https://bellrockholdings.org
- **Railway Dashboard:** https://railway.app/
- **Vercel Dashboard:** https://vercel.com/

## 🎉 Success Indicators

When everything is working:
- Frontend loads at bellrockholdings.org
- Properties page shows data from Railway
- Investments page shows data from Railway
- No CORS errors in browser console
- Images load from DigitalOcean Spaces

## 🐛 Common Issues

1. **CORS Errors** → Update Railway CORS_ALLOWED_ORIGINS
2. **404 Errors** → Check Vercel VITE_API_BASE_URL
3. **Env vars not working** → Redeploy after changes
4. **Still using localhost** → Clear browser cache

See `VERCEL_RAILWAY_CONNECTION.md` for detailed troubleshooting.
