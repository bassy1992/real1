# Deployment Checklist: Connecting Railway Backend to Vercel Frontend

## ✅ Pre-Deployment Checklist

### Backend Changes (Already Done)
- [x] Updated `back/backend/settings.py` with CORS settings for bellrockholdings.org
- [x] Added Railway domain to ALLOWED_HOSTS
- [x] Updated `back/.env.example` with production values
- [x] Enabled CORS_ALLOW_CREDENTIALS

### Frontend Changes (Already Done)
- [x] Updated `front/constants.ts` to use Railway backend URL
- [x] Made API_BASE_URL configurable via environment variable
- [x] Updated `front/.env.local` with production API URL

## 🚀 Deployment Steps

### Step 1: Update Railway Environment Variables

1. Go to Railway dashboard: https://railway.app/
2. Select your project: `real-production-4319`
3. Click on your backend service
4. Go to "Variables" tab
5. Add/update these variables:

```bash
CORS_ALLOWED_ORIGINS=https://bellrockholdings.org,https://www.bellrockholdings.org,http://localhost:5173
FRONTEND_URL=https://bellrockholdings.org
ALLOWED_HOSTS=real-production-4319.up.railway.app,localhost,127.0.0.1
DEBUG=False
```

6. Railway will automatically redeploy (wait 2-3 minutes)

### Step 2: Verify Backend Deployment

Run the verification script:
```bash
./verify_connection.sh
```

Or manually test:
```bash
curl https://real-production-4319.up.railway.app/api/properties/
curl https://real-production-4319.up.railway.app/api/investments/opportunities/
```

Expected: HTTP 200 responses with JSON data

### Step 3: Update Vercel Environment Variables

1. Go to Vercel dashboard: https://vercel.com/
2. Select your project (bellrockholdings.org)
3. Go to Settings → Environment Variables
4. Add this variable:

```bash
VITE_API_BASE_URL=https://real-production-4319.up.railway.app/api
```

5. Select "Production", "Preview", and "Development"
6. Click "Save"

### Step 4: Deploy Frontend to Vercel

Option A - Automatic (if connected to Git):
```bash
cd front
git add .
git commit -m "Connect to Railway backend"
git push
```

Option B - Manual:
1. Go to Vercel dashboard
2. Click "Deployments"
3. Click "Redeploy" on the latest deployment
4. Select "Use existing Build Cache: No"

Wait for deployment to complete (1-2 minutes)

### Step 5: Verify Frontend Deployment

1. Visit: https://bellrockholdings.org
2. Open browser DevTools (F12)
3. Go to Network tab
4. Navigate to Properties page
5. Check for API calls to `https://real-production-4319.up.railway.app/api/properties/`
6. Verify no CORS errors in Console tab

## 🧪 Testing Checklist

After deployment, verify these:

### Backend Tests
- [ ] Admin panel accessible: https://real-production-4319.up.railway.app/admin/
- [ ] Properties API returns data: https://real-production-4319.up.railway.app/api/properties/
- [ ] Investments API returns data: https://real-production-4319.up.railway.app/api/investments/opportunities/
- [ ] No 500 errors in Railway logs

### Frontend Tests
- [ ] Homepage loads: https://bellrockholdings.org
- [ ] Properties page displays data
- [ ] Investments page displays data
- [ ] Images load from DigitalOcean Spaces
- [ ] No CORS errors in browser console
- [ ] No 404 errors for API calls

### Cross-Origin Tests
- [ ] API calls work from bellrockholdings.org
- [ ] API calls work from www.bellrockholdings.org (if configured)
- [ ] Cookies/sessions work (if using authentication)

## 🐛 Troubleshooting

### Issue: CORS Errors

**Symptoms:** Browser console shows "CORS policy" errors

**Solution:**
1. Check Railway environment variables include your domain
2. Verify CORS_ALLOWED_ORIGINS has `https://bellrockholdings.org`
3. Redeploy Railway backend
4. Clear browser cache and hard refresh

### Issue: 404 Not Found

**Symptoms:** API calls return 404

**Solution:**
1. Verify API URL in Vercel environment variables
2. Check Railway backend is running
3. Test API endpoints directly with curl
4. Verify URL doesn't have trailing slash issues

### Issue: Environment Variables Not Working

**Symptoms:** Frontend still uses localhost

**Solution:**
1. Verify Vercel environment variable starts with `VITE_`
2. Redeploy Vercel frontend after adding variables
3. Check browser DevTools → Network tab for actual URLs being called
4. Clear browser cache

### Issue: SSL/Certificate Errors

**Symptoms:** Mixed content warnings

**Solution:**
1. Ensure all URLs use `https://` not `http://`
2. Check Railway backend has SSL enabled (automatic)
3. Verify Vercel frontend uses HTTPS (automatic)

## 📊 Monitoring

After deployment, monitor:

### Railway
- Check logs: `railway logs`
- Monitor CPU/Memory usage
- Check database connections
- Review error rates

### Vercel
- Check deployment logs
- Monitor function execution times
- Review error tracking
- Check bandwidth usage

## 🔄 Rollback Plan

If something goes wrong:

### Railway
1. Go to Deployments tab
2. Click on previous working deployment
3. Click "Redeploy"

### Vercel
1. Go to Deployments tab
2. Find previous working deployment
3. Click "..." → "Promote to Production"

## 📝 Post-Deployment Tasks

- [ ] Update DNS records if using custom domain
- [ ] Set up monitoring/alerting
- [ ] Configure backup strategy
- [ ] Document API endpoints
- [ ] Set up CI/CD pipeline
- [ ] Enable error tracking (Sentry, etc.)
- [ ] Configure CDN for static assets
- [ ] Set up staging environment

## 🎉 Success Criteria

Deployment is successful when:
- ✅ Frontend loads at https://bellrockholdings.org
- ✅ Properties page shows data from Railway backend
- ✅ Investments page shows data from Railway backend
- ✅ No CORS errors in browser console
- ✅ Images load from DigitalOcean Spaces
- ✅ No errors in Railway or Vercel logs
- ✅ Page load time < 3 seconds
- ✅ All API endpoints return 200 status codes

## 📞 Support

If you encounter issues:
1. Check Railway logs: https://railway.app/
2. Check Vercel logs: https://vercel.com/
3. Review this checklist
4. Check VERCEL_RAILWAY_CONNECTION.md for detailed troubleshooting
