# Railway Environment Variables Setup

## Quick Setup Guide

### Step 1: Generate SECRET_KEY
Run this locally to generate a secure key:
```bash
python generate_secret_key.py
```
Copy the output.

### Step 2: Add Environment Variables in Railway

Go to your Railway project → Variables tab and add these:

#### Required Variables:
```
SECRET_KEY=<paste-the-generated-key-here>
DEBUG=False
ALLOWED_HOSTS=<your-app-name>.up.railway.app
```

#### Optional Variables (if using DigitalOcean Spaces):
```
USE_SPACES=True
DO_SPACES_KEY=<your-key>
DO_SPACES_SECRET=<your-secret>
DO_SPACES_BUCKET_NAME=<your-bucket>
DO_SPACES_ENDPOINT_URL=https://sfo3.digitaloceanspaces.com
DO_SPACES_REGION=sfo3
DO_SPACES_CDN_DOMAIN=<your-bucket>.sfo3.cdn.digitaloceanspaces.com
```

#### CORS Settings (update after deployment):
```
CORS_ALLOWED_ORIGINS=https://<your-frontend>.vercel.app,https://<your-domain>.com
CSRF_TRUSTED_ORIGINS=https://<your-app-name>.up.railway.app,https://<your-domain>.com
```

### Step 3: Add PostgreSQL Database
1. In Railway dashboard, click "New" → "Database" → "PostgreSQL"
2. Railway automatically sets `DATABASE_URL` - no manual configuration needed

### Step 4: Deploy
1. Connect your GitHub repository
2. Railway will automatically deploy when you push to main branch
3. Check logs for any errors

### Step 5: Verify Deployment
Visit: `https://<your-app-name>.up.railway.app/admin/`

## Troubleshooting

### "SECRET_KEY environment variable is not set"
- Make sure you added SECRET_KEY in Railway Variables tab
- Redeploy after adding the variable

### Database Connection Errors
- Ensure PostgreSQL service is running in Railway
- Check that DATABASE_URL is automatically set

### Static Files Not Loading
- Check build logs to ensure collectstatic ran successfully
- Verify WhiteNoise is in MIDDLEWARE settings

### CORS Errors
- Update CORS_ALLOWED_ORIGINS with your frontend URL
- Update CSRF_TRUSTED_ORIGINS with your backend URL
- Redeploy after updating variables
