# Environment Variables Reference

Quick reference for setting up environment variables on Railway and Vercel.

## Railway Backend Environment Variables

Copy these to your Railway project settings:

```bash
# Django Core
SECRET_KEY=your-django-secret-key-here
DEBUG=False

# Database (automatically set by Railway)
DATABASE_URL=postgresql://...

# Hosts
ALLOWED_HOSTS=real-production-4319.up.railway.app,localhost,127.0.0.1

# CORS Configuration
CORS_ALLOWED_ORIGINS=https://bellrockholdings.org,https://www.bellrockholdings.org,http://localhost:5173,http://localhost:3000
FRONTEND_URL=https://bellrockholdings.org

# DigitalOcean Spaces
USE_SPACES=True
DO_SPACES_KEY=DO8014PDYEMPMGC8CMYR
DO_SPACES_SECRET=MRio2V3xaCvUMJXWwGmzAjfJceHIggO1EH4ripqy5j8
DO_SPACES_BUCKET_NAME=lutheran
DO_SPACES_ENDPOINT_URL=https://sfo3.digitaloceanspaces.com
DO_SPACES_REGION=sfo3
DO_SPACES_CDN_DOMAIN=lutheran.sfo3.cdn.digitaloceanspaces.com
```

## Vercel Frontend Environment Variables

Copy these to your Vercel project settings → Environment Variables:

```bash
# API Configuration
VITE_API_BASE_URL=https://real-production-4319.up.railway.app/api

# Gemini API (if using AI features)
GEMINI_API_KEY=your-gemini-api-key-here
```

## Important Notes

### Railway
- After adding/updating environment variables, Railway will automatically redeploy
- `DATABASE_URL` is automatically provided by Railway when you add a PostgreSQL database
- Make sure to generate a strong `SECRET_KEY` for production

### Vercel
- Environment variables starting with `VITE_` are exposed to the frontend code
- Changes to environment variables require a new deployment to take effect
- You can set different values for Production, Preview, and Development environments

## How to Set Environment Variables

### Railway
1. Go to your Railway project dashboard
2. Click on your backend service
3. Go to "Variables" tab
4. Click "New Variable" or "Raw Editor"
5. Paste the variables
6. Railway will automatically redeploy

### Vercel
1. Go to your Vercel project dashboard
2. Click "Settings" → "Environment Variables"
3. Add each variable with its value
4. Select which environments (Production, Preview, Development)
5. Click "Save"
6. Redeploy your project

## Generating a Django SECRET_KEY

Run this command to generate a secure secret key:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Or use this online: https://djecrety.ir/

## Testing Environment Variables

### Railway
```bash
# SSH into Railway container (if available)
railway run env

# Or check logs
railway logs
```

### Vercel
```bash
# Test locally with Vercel CLI
vercel env pull .env.local
vercel dev
```

## Security Best Practices

1. ✅ Never commit `.env` files to git
2. ✅ Use different SECRET_KEY for development and production
3. ✅ Set DEBUG=False in production
4. ✅ Rotate secrets regularly
5. ✅ Use Railway's secret management for sensitive data
6. ✅ Limit CORS_ALLOWED_ORIGINS to only your domains
7. ✅ Keep DigitalOcean Spaces credentials secure
