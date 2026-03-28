# Connecting Railway Backend to Vercel Frontend

This guide explains how to connect your Railway backend (https://real-production-4319.up.railway.app/) to your Vercel frontend (bellrockholdings.org).

## Changes Made

### Backend (Django on Railway)

1. **Updated CORS Settings** (`back/backend/settings.py`)
   - Added `bellrockholdings.org` and `www.bellrockholdings.org` to allowed origins
   - Enabled `CORS_ALLOW_CREDENTIALS = True` for cookie/session support

2. **Updated Allowed Hosts** (`back/backend/settings.py`)
   - Added Railway domain: `real-production-4319.up.railway.app`

3. **Updated Environment Example** (`back/.env.example`)
   - Set proper CORS_ALLOWED_ORIGINS with production domains
   - Set FRONTEND_URL to bellrockholdings.org

### Frontend (React/Vite on Vercel)

1. **Updated API Base URL** (`front/constants.ts`)
   - Changed from localhost to Railway backend URL
   - Made it configurable via environment variable: `VITE_API_BASE_URL`

2. **Added Environment Variable** (`front/.env.local`)
   - Added `VITE_API_BASE_URL=https://real-production-4319.up.railway.app/api`

## Railway Deployment Steps

### 1. Update Environment Variables on Railway

Go to your Railway project settings and add/update these environment variables:

```bash
# Required
SECRET_KEY=<your-secret-key>
DEBUG=False
DATABASE_URL=<automatically-set-by-railway>

# CORS Configuration
CORS_ALLOWED_ORIGINS=https://bellrockholdings.org,https://www.bellrockholdings.org,http://localhost:5173
FRONTEND_URL=https://bellrockholdings.org

# Allowed Hosts
ALLOWED_HOSTS=real-production-4319.up.railway.app,localhost,127.0.0.1

# DigitalOcean Spaces (if using)
USE_SPACES=True
DO_SPACES_KEY=<your-key>
DO_SPACES_SECRET=<your-secret>
DO_SPACES_BUCKET_NAME=lutheran
DO_SPACES_ENDPOINT_URL=https://sfo3.digitaloceanspaces.com
DO_SPACES_REGION=sfo3
DO_SPACES_CDN_DOMAIN=lutheran.sfo3.cdn.digitaloceanspaces.com
```

### 2. Deploy Backend to Railway

```bash
cd back
git add .
git commit -m "Configure CORS for Vercel frontend"
git push
```

Railway will automatically redeploy your backend.

### 3. Verify Backend is Running

Test your backend API:

```bash
curl https://real-production-4319.up.railway.app/api/properties/
curl https://real-production-4319.up.railway.app/api/investments/opportunities/
```

## Vercel Deployment Steps

### 1. Configure Environment Variables on Vercel

Go to your Vercel project settings → Environment Variables and add:

```bash
VITE_API_BASE_URL=https://real-production-4319.up.railway.app/api
GEMINI_API_KEY=<your-gemini-api-key>
```

### 2. Deploy Frontend to Vercel

```bash
cd front
git add .
git commit -m "Connect to Railway backend"
git push
```

Or manually trigger a deployment from the Vercel dashboard.

### 3. Verify Frontend is Connected

1. Visit https://bellrockholdings.org
2. Open browser DevTools → Network tab
3. Navigate to Properties or Investments page
4. Check that API calls are going to `https://real-production-4319.up.railway.app/api/`
5. Verify data is loading correctly

## Troubleshooting

### CORS Errors

If you see CORS errors in the browser console:

1. Check Railway environment variables include your Vercel domain
2. Verify `CORS_ALLOWED_ORIGINS` includes `https://bellrockholdings.org`
3. Redeploy Railway backend after environment variable changes

### 404 Errors

If API endpoints return 404:

1. Verify the backend URL is correct: `https://real-production-4319.up.railway.app/api/`
2. Check that the backend is running on Railway
3. Test endpoints directly with curl

### SSL/HTTPS Issues

Both Railway and Vercel provide automatic HTTPS. Ensure:

1. Frontend uses `https://` for API calls (not `http://`)
2. Backend `SECURE_SSL_REDIRECT = True` is set when `DEBUG = False`

### Environment Variables Not Working

1. Vercel: Environment variables must start with `VITE_` to be exposed to the frontend
2. Railway: After changing environment variables, trigger a new deployment
3. Clear browser cache and hard refresh (Cmd+Shift+R / Ctrl+Shift+R)

## Testing Checklist

- [ ] Backend health check: `https://real-production-4319.up.railway.app/admin/`
- [ ] Properties API: `https://real-production-4319.up.railway.app/api/properties/`
- [ ] Investments API: `https://real-production-4319.up.railway.app/api/investments/opportunities/`
- [ ] Frontend loads: `https://bellrockholdings.org`
- [ ] Properties page displays data from backend
- [ ] Investments page displays data from backend
- [ ] No CORS errors in browser console
- [ ] Images load from DigitalOcean Spaces

## Local Development

For local development, you can still use localhost:

```bash
# Frontend .env.local
VITE_API_BASE_URL=http://localhost:8000/api
```

The backend already allows localhost origins in CORS settings.

## Next Steps

1. Set up custom domain on Railway (optional)
2. Configure CDN for static assets (optional)
3. Set up monitoring and logging
4. Configure backup strategy for database
5. Set up CI/CD pipeline for automated deployments
