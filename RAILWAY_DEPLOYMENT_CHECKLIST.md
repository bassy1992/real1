# Railway Deployment Checklist

## ✅ Pre-Deployment Verification

### Files Ready
- ✅ `back/requirements.txt` - All dependencies listed
- ✅ `back/railway.json` - Railway configuration
- ✅ `back/Procfile` - Process configuration
- ✅ `back/nixpacks.toml` - Build configuration
- ✅ `back/backend/settings.py` - Production-ready settings
- ✅ `back/.env.example` - Environment variables template

### Settings Configuration
- ✅ Database: PostgreSQL support via `dj_database_url`
- ✅ Static files: WhiteNoise configured
- ✅ Media files: DigitalOcean Spaces configured
- ✅ CORS: Configurable via environment variables
- ✅ Security: Production security settings enabled when DEBUG=False

## 🚀 Deployment Steps

### 1. Create Railway Project

1. Go to https://railway.app/dashboard
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose: `bassy1992/real`
5. **CRITICAL**: After project is created, go to Service Settings:
   - Click on your service
   - Go to "Settings" tab
   - Scroll to "Root Directory"
   - Set it to: `back`
   - Click "Save"
6. Railway will now detect your Django app correctly

**Why this is needed**: Your repository has both `front` and `back` folders. Railway needs to know to build from the `back` folder where your Django app lives.

### 2. Add PostgreSQL Database

1. In Railway project, click "New"
2. Select "Database" → "Add PostgreSQL"
3. Railway auto-creates `DATABASE_URL` variable

### 3. Configure Environment Variables

Copy these to Railway → Your Service → Variables:

```bash
# Django Core
SECRET_KEY=btv7psv)&2kiih7gy_$7op2bjqw!udihv__m=c8k2)3fymctdb
DEBUG=False
ALLOWED_HOSTS=*.railway.app

# DigitalOcean Spaces
USE_SPACES=True
DO_SPACES_KEY=DO8014PDYEMPMGC8CMYR
DO_SPACES_SECRET=MRio2V3xaCvUMJXWwGmzAjfJceHIggO1EH4ripqy5j8
DO_SPACES_BUCKET_NAME=lutheran
DO_SPACES_ENDPOINT_URL=https://sfo3.digitaloceanspaces.com
DO_SPACES_REGION=sfo3
DO_SPACES_CDN_DOMAIN=lutheran.sfo3.cdn.digitaloceanspaces.com

# CORS (update after getting Railway URL)
CORS_ALLOWED_ORIGINS=http://localhost:5173,https://your-frontend.vercel.app
```

### 4. Deploy

Railway will automatically:
- Detect Python/Django
- Install dependencies from `requirements.txt`
- Run migrations
- Collect static files
- Start gunicorn server

### 5. Post-Deployment Setup

#### A. Get Your Railway URL
After deployment, Railway provides a URL like:
```
https://your-project-name.up.railway.app
```

#### B. Update Environment Variables
Go back to Variables and update:
```bash
ALLOWED_HOSTS=your-project-name.up.railway.app,*.railway.app
CORS_ALLOWED_ORIGINS=http://localhost:5173,https://your-frontend.vercel.app,https://your-project-name.up.railway.app
```

#### C. Create Superuser
1. In Railway, go to your service
2. Click "..." → "Shell"
3. Run:
```bash
python manage.py createsuperuser
```
Follow prompts to create admin account.

#### D. Load Initial Data (Optional)
```bash
python manage.py load_properties
python manage.py load_investments
```

### 6. Test Your Deployment

Visit these URLs (replace with your Railway URL):

- **API Root**: `https://your-project.railway.app/api/`
- **Properties**: `https://your-project.railway.app/api/properties/`
- **Investments**: `https://your-project.railway.app/api/investments/`
- **Admin Panel**: `https://your-project.railway.app/admin/`

## 🎨 Frontend Deployment

### Update Frontend API URL

In your frontend code, update the API base URL to point to Railway:

**File**: `front/services/propertyService.ts` and `front/services/investmentService.ts`

```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://your-project.railway.app/api';
```

### Deploy Frontend to Vercel

1. Go to https://vercel.com
2. Import GitHub repository: `bassy1992/real`
3. Set **Root Directory**: `front`
4. Add environment variable:
   ```
   VITE_API_URL=https://your-project-name.railway.app/api
   ```
5. Deploy

### Update CORS After Frontend Deployment

Once frontend is deployed, update Railway environment variable:
```bash
CORS_ALLOWED_ORIGINS=https://your-frontend.vercel.app,https://your-project.railway.app
```

## 🔒 Security Checklist

- ✅ `DEBUG=False` in production
- ✅ Strong `SECRET_KEY` generated
- ✅ `ALLOWED_HOSTS` properly configured
- ✅ HTTPS enabled (automatic on Railway)
- ✅ Database credentials secured (Railway manages)
- ✅ CORS properly configured
- ✅ Static files served via WhiteNoise
- ✅ Media files on DigitalOcean Spaces
- ✅ Security headers enabled in production

## 📊 Monitoring

### View Logs
1. Go to your service in Railway
2. Click "Deployments"
3. Select active deployment
4. View real-time logs

### Common Issues

**Issue**: Static files not loading
- **Solution**: Check logs for `collectstatic` errors
- Verify `STATIC_ROOT` and `STATICFILES_STORAGE` settings

**Issue**: Database connection errors
- **Solution**: Verify PostgreSQL service is running
- Check `DATABASE_URL` is set correctly

**Issue**: CORS errors from frontend
- **Solution**: Add frontend URL to `CORS_ALLOWED_ORIGINS`
- Ensure no trailing slashes in URLs

**Issue**: Media uploads failing
- **Solution**: Verify DigitalOcean Spaces credentials
- Check bucket permissions (public read access)
- Ensure `USE_SPACES=True`

## 💰 Cost Estimate

- **Hobby Plan**: $5/month
  - Includes PostgreSQL database
  - 500 hours execution time
  - 100GB bandwidth

- **Pro Plan**: $20/month
  - Unlimited execution time
  - Priority support

## 🔄 Continuous Deployment

Railway automatically deploys when you push to GitHub:

```bash
git add .
git commit -m "Your changes"
git push origin main
```

Railway will:
1. Detect the push
2. Build the application
3. Run migrations
4. Deploy automatically

## 📝 Next Steps

1. ✅ Deploy backend to Railway
2. ✅ Create superuser
3. ✅ Test API endpoints
4. ✅ Deploy frontend to Vercel
5. ✅ Update CORS settings
6. ✅ Test full application
7. 🔲 Set up custom domain (optional)
8. 🔲 Configure monitoring (Sentry, etc.)
9. 🔲 Set up automated backups
10. 🔲 Add email service (SendGrid, etc.)

## 🆘 Support Resources

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Django Deployment: https://docs.djangoproject.com/en/4.2/howto/deployment/

---

**Generated SECRET_KEY for Production:**
```
btv7psv)&2kiih7gy_$7op2bjqw!udihv__m=c8k2)3fymctdb
```

**Important**: Keep this secret key secure and never commit it to version control!
