# Railway Deployment Guide

## Prerequisites
- Railway account (https://railway.app)
- GitHub repository connected to Railway

## Environment Variables to Set in Railway

### Backend (Django)
Set these in your Railway backend service:

```
SECRET_KEY=<generate-a-secure-random-key>
DEBUG=False
ALLOWED_HOSTS=<your-railway-domain>.railway.app,<your-custom-domain>
DATABASE_URL=<automatically-set-by-railway-postgres>

# DigitalOcean Spaces (if using)
USE_SPACES=True
DO_SPACES_KEY=<your-spaces-key>
DO_SPACES_SECRET=<your-spaces-secret>
DO_SPACES_BUCKET_NAME=<your-bucket-name>
DO_SPACES_ENDPOINT_URL=https://sfo3.digitaloceanspaces.com
DO_SPACES_REGION=sfo3
DO_SPACES_CDN_DOMAIN=<your-bucket>.sfo3.cdn.digitaloceanspaces.com

# CORS Settings
CORS_ALLOWED_ORIGINS=https://<your-frontend-domain>,https://<your-custom-domain>
FRONTEND_URL=https://<your-frontend-domain>

# CSRF Settings
CSRF_TRUSTED_ORIGINS=https://<your-railway-backend>.railway.app,https://<your-custom-domain>

# Custom Domain (optional)
CUSTOM_DOMAIN=<your-custom-domain>
```

### Frontend (React/Vite)
Set these in your Railway frontend service:

```
VITE_API_BASE_URL=https://<your-railway-backend>.railway.app/api
GEMINI_API_KEY=<your-gemini-api-key>
```

## Deployment Steps

### 1. Create Railway Project
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login to Railway
railway login

# Link to your project (or create new)
railway link
```

### 2. Add PostgreSQL Database
- In Railway dashboard, click "New" → "Database" → "PostgreSQL"
- Railway will automatically set the `DATABASE_URL` environment variable

### 3. Deploy Backend
- Create a new service from your GitHub repository
- Set root directory to `/back` (or configure nixpacks.toml)
- Add all environment variables listed above
- Deploy

### 4. Deploy Frontend
- Create another service from the same repository
- Set root directory to `/front`
- Add frontend environment variables
- Deploy

### 5. Configure Custom Domain (Optional)
- In Railway dashboard, go to your service settings
- Add your custom domain
- Update DNS records as instructed by Railway
- Update `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` accordingly

## Post-Deployment

### Create Superuser
After first deployment, create an admin user:
```bash
railway run python manage.py createsuperuser
```

Or use the `ensure_superuser` command which runs automatically on deployment.

## Troubleshooting

### Static Files Not Loading
- Ensure `collectstatic` runs during build
- Check `STATIC_ROOT` and `STATIC_URL` in settings.py
- Verify WhiteNoise is installed and configured

### Database Connection Issues
- Verify `DATABASE_URL` is set by Railway
- Check PostgreSQL service is running
- Ensure migrations ran successfully

### CORS Errors
- Update `CORS_ALLOWED_ORIGINS` with correct frontend URL
- Add `CSRF_TRUSTED_ORIGINS` with backend URL
- Restart the service after updating environment variables

## Monitoring
- Check logs in Railway dashboard
- Monitor database usage
- Set up alerts for errors

## Local Development vs Production
- Local: Uses SQLite, DEBUG=True, local CORS origins
- Production: Uses PostgreSQL, DEBUG=False, production CORS origins
- Environment variables control the behavior
