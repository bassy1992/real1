# Railway Manual Setup Guide

Due to the monorepo structure (both `front` and `back` folders), Railway needs manual configuration.

## Step-by-Step Setup

### 1. Create Railway Project

1. Go to https://railway.app/dashboard
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose: `bassy1992/real`
5. Railway will create a service

### 2. Configure Root Directory

**CRITICAL STEP:**

1. Click on your service in Railway
2. Go to "Settings" tab
3. Scroll to "Root Directory"
4. Enter: `back`
5. Click outside the field to save
6. Railway will automatically redeploy

### 3. Add PostgreSQL Database

1. In your Railway project, click "+ New"
2. Select "Database" → "Add PostgreSQL"
3. Railway automatically creates `DATABASE_URL` environment variable

### 4. Configure Environment Variables

Go to your Django service → "Variables" tab and add:

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
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

### 5. Deploy

Railway will automatically:
- Detect Django from `back/manage.py`
- Install dependencies from `back/requirements.txt`
- Run migrations
- Start with gunicorn

### 6. Get Your Railway URL

After deployment completes, Railway provides a URL like:
```
https://your-project-name.up.railway.app
```

### 7. Update Environment Variables

Update these variables with your actual Railway URL:

```bash
ALLOWED_HOSTS=your-project-name.up.railway.app,*.railway.app
CORS_ALLOWED_ORIGINS=http://localhost:5173,https://your-project-name.up.railway.app
```

### 8. Create Superuser

1. In Railway, click on your service
2. Click "..." menu → "Shell"  
3. Run:
```bash
python manage.py createsuperuser
```

Follow prompts to create admin account.

### 9. Test Your Deployment

Visit these URLs (replace with your Railway URL):

- API Root: `https://your-project.railway.app/api/`
- Properties: `https://your-project.railway.app/api/properties/`
- Investments: `https://your-project.railway.app/api/investments/`
- Admin: `https://your-project.railway.app/admin/`

## Why Root Directory is Important

Your repository structure:
```
/
├── back/          ← Django app is here
│   ├── manage.py
│   ├── requirements.txt
│   └── backend/
└── front/         ← React app
```

By setting Root Directory to `back`, Railway:
- Finds `manage.py` and detects Django
- Uses `requirements.txt` from the correct location
- Runs all commands in the right directory
- Properly configures the Python path

## Troubleshooting

### Issue: "No module named 'backend'"
**Solution**: Ensure Root Directory is set to `back` in service settings

### Issue: "libpq.so.5: cannot open shared object file"
**Solution**: Railway should auto-install PostgreSQL libraries when it detects psycopg2-binary in requirements.txt. If not, the Root Directory setting should fix this.

### Issue: Static files not loading
**Solution**: Check deployment logs for collectstatic errors. Railway runs this automatically.

### Issue: CORS errors
**Solution**: Add your frontend URL to `CORS_ALLOWED_ORIGINS` environment variable

## Next Steps

1. ✅ Set Root Directory to `back`
2. ✅ Add PostgreSQL database
3. ✅ Configure environment variables
4. ✅ Deploy and test
5. 🔲 Deploy frontend to Vercel
6. 🔲 Update CORS settings
7. 🔲 Set up custom domain (optional)

## Support

If you encounter issues:
- Check Railway deployment logs
- Verify Root Directory is set to `back`
- Ensure all environment variables are set
- Check PostgreSQL database is running

---

**Important**: The Root Directory setting is the key to successful deployment!
