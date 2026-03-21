# Railway Deployment Guide

This guide will help you deploy the BELLEROCK platform to Railway.

## Prerequisites

- Railway account (sign up at https://railway.app)
- GitHub repository (already set up at https://github.com/bassy1992/real.git)
- DigitalOcean Spaces account for media storage

## Deployment Steps

### 1. Create New Railway Project

1. Go to https://railway.app/dashboard
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository: `bassy1992/real`
5. Railway will detect your Django application

### 2. Add PostgreSQL Database

1. In your Railway project, click "New"
2. Select "Database" → "Add PostgreSQL"
3. Railway will automatically create a `DATABASE_URL` environment variable

### 3. Configure Environment Variables

Go to your Django service → Variables tab and add:

#### Required Variables

```bash
# Django Core
SECRET_KEY=<generate-a-secure-random-key>
DEBUG=False
ALLOWED_HOSTS=<your-railway-domain>.railway.app

# DigitalOcean Spaces (from your existing setup)
USE_SPACES=True
DO_SPACES_KEY=DO8014PDYEMPMGC8CMYR
DO_SPACES_SECRET=MRio2V3xaCvUMJXWwGmzAjfJceHIggO1EH4ripqy5j8
DO_SPACES_BUCKET_NAME=lutheran
DO_SPACES_ENDPOINT_URL=https://sfo3.digitaloceanspaces.com
DO_SPACES_REGION=sfo3
DO_SPACES_CDN_DOMAIN=lutheran.sfo3.cdn.digitaloceanspaces.com

# CORS (update with your frontend URL)
CORS_ALLOWED_ORIGINS=https://<your-frontend-domain>.vercel.app,https://<your-railway-domain>.railway.app
```

#### Generate SECRET_KEY

Run this in Python to generate a secure key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use this online: https://djecrety.ir/

### 4. Configure Build Settings

Railway should automatically detect your Django app. If not, set:

**Root Directory**: `back`

**Build Command**: (leave empty, Railway will use requirements.txt)

**Start Command**: 
```bash
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn backend.wsgi:application
```

### 5. Deploy

1. Click "Deploy" or push to your GitHub repository
2. Railway will automatically build and deploy
3. Monitor the deployment logs for any errors

### 6. Run Initial Setup Commands

After first deployment, open the Railway shell and run:

```bash
# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py load_properties
python manage.py load_investments
```

To access the shell:
1. Go to your service in Railway
2. Click on the "..." menu
3. Select "Shell"

### 7. Access Your Application

Your backend will be available at:
```
https://<your-project-name>.railway.app
```

Admin panel:
```
https://<your-project-name>.railway.app/admin/
```

API:
```
https://<your-project-name>.railway.app/api/properties/
```

## Frontend Deployment

### Option 1: Deploy to Vercel

1. Go to https://vercel.com
2. Import your GitHub repository
3. Set Root Directory to `front`
4. Add environment variable:
   ```
   VITE_API_URL=https://<your-railway-backend>.railway.app/api
   ```
5. Deploy

### Option 2: Deploy to Railway

1. In your Railway project, click "New" → "GitHub Repo"
2. Select the same repository
3. Set Root Directory to `front`
4. Add environment variable:
   ```
   VITE_API_URL=https://<your-railway-backend>.railway.app/api
   ```
5. Deploy

### Update Frontend API URL

Update `front/services/propertyService.ts` and `front/services/investmentService.ts`:

```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';
```

## Custom Domain Setup

### Backend Domain

1. In Railway, go to your Django service
2. Click "Settings" → "Domains"
3. Click "Add Domain"
4. Enter your custom domain (e.g., `api.bellerock.com`)
5. Add the CNAME record to your DNS provider:
   ```
   CNAME api <your-project>.railway.app
   ```
6. Update `ALLOWED_HOSTS` environment variable to include your domain

### Frontend Domain

Follow similar steps for your frontend service or Vercel deployment.

## Environment Variables Reference

### Django Backend

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `django-insecure-...` |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `api.bellerock.com` |
| `DATABASE_URL` | PostgreSQL connection | Auto-set by Railway |
| `USE_SPACES` | Enable DigitalOcean Spaces | `True` |
| `DO_SPACES_KEY` | Spaces access key | `DO8014...` |
| `DO_SPACES_SECRET` | Spaces secret key | `MRio2V3x...` |
| `DO_SPACES_BUCKET_NAME` | Bucket name | `lutheran` |
| `DO_SPACES_ENDPOINT_URL` | Spaces endpoint | `https://sfo3.digitaloceanspaces.com` |
| `DO_SPACES_REGION` | Spaces region | `sfo3` |
| `DO_SPACES_CDN_DOMAIN` | CDN domain | `lutheran.sfo3.cdn.digitaloceanspaces.com` |
| `CORS_ALLOWED_ORIGINS` | Allowed CORS origins | `https://bellerock.com` |

## Troubleshooting

### Static Files Not Loading

1. Check that `collectstatic` ran successfully in logs
2. Verify `STATIC_ROOT` is set correctly
3. Ensure WhiteNoise is in `MIDDLEWARE`

### Database Connection Errors

1. Verify PostgreSQL service is running
2. Check `DATABASE_URL` is set correctly
3. Ensure migrations have run

### CORS Errors

1. Add your frontend URL to `CORS_ALLOWED_ORIGINS`
2. Ensure the URL format is correct (no trailing slash)
3. Check that `corsheaders` middleware is enabled

### Media Files Not Uploading

1. Verify DigitalOcean Spaces credentials
2. Check bucket permissions (should allow public read)
3. Ensure `USE_SPACES=True` is set

## Monitoring

### View Logs

In Railway:
1. Go to your service
2. Click "Deployments"
3. Select the active deployment
4. View logs in real-time

### Database Backups

Railway automatically backs up PostgreSQL databases. To manually backup:

1. Go to PostgreSQL service
2. Click "Data" tab
3. Use Railway CLI or pg_dump

## Scaling

Railway automatically scales based on usage. To configure:

1. Go to service settings
2. Adjust resources under "Resources" tab
3. Set memory and CPU limits

## Cost Optimization

- **Hobby Plan**: $5/month for small projects
- **Pro Plan**: $20/month for production apps
- **Database**: Included in plan
- **Bandwidth**: First 100GB free

## Security Checklist

- ✅ `DEBUG=False` in production
- ✅ Strong `SECRET_KEY` set
- ✅ `ALLOWED_HOSTS` configured
- ✅ HTTPS enabled (automatic on Railway)
- ✅ Database credentials secured
- ✅ CORS properly configured
- ✅ Static files served via WhiteNoise
- ✅ Media files on DigitalOcean Spaces

## Support

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Django Docs: https://docs.djangoproject.com

## Next Steps

1. Set up monitoring (e.g., Sentry)
2. Configure email service (e.g., SendGrid)
3. Set up CI/CD pipeline
4. Add SSL certificate for custom domain
5. Configure CDN for static files
6. Set up automated backups
