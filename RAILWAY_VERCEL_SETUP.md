# Railway ↔️ Vercel Connection Setup

Complete guide for connecting your Railway Django backend to your Vercel React frontend.

## 📚 Documentation Index

1. **[QUICK_START.md](QUICK_START.md)** - Get started in 5 minutes
2. **[CONNECTION_SUMMARY.md](CONNECTION_SUMMARY.md)** - Overview of changes
3. **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - Step-by-step deployment
4. **[VERCEL_RAILWAY_CONNECTION.md](VERCEL_RAILWAY_CONNECTION.md)** - Detailed guide
5. **[ENV_VARIABLES_REFERENCE.md](ENV_VARIABLES_REFERENCE.md)** - Environment variables
6. **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture
7. **[verify_connection.sh](verify_connection.sh)** - Automated testing script

## 🎯 What This Setup Does

Connects:
- **Frontend:** bellrockholdings.org (Vercel)
- **Backend:** https://real-production-4319.up.railway.app/ (Railway)
- **Database:** PostgreSQL (Railway)
- **Storage:** DigitalOcean Spaces

## ⚡ Quick Setup

### Step 1: Railway Environment Variables
```bash
CORS_ALLOWED_ORIGINS=https://bellrockholdings.org,https://www.bellrockholdings.org
FRONTEND_URL=https://bellrockholdings.org
ALLOWED_HOSTS=real-production-4319.up.railway.app
DEBUG=False
```

### Step 2: Vercel Environment Variables
```bash
VITE_API_BASE_URL=https://real-production-4319.up.railway.app/api
```

### Step 3: Deploy & Test
```bash
./verify_connection.sh
```

## 📋 Files Changed

### Backend
- ✅ `back/backend/settings.py` - CORS and allowed hosts
- ✅ `back/.env.example` - Environment variable examples

### Frontend
- ✅ `front/constants.ts` - API base URL configuration
- ✅ `front/services/propertyService.ts` - Use centralized API URL
- ✅ `front/.env.local` - Environment variables

## 🧪 Testing

### Automated
```bash
chmod +x verify_connection.sh
./verify_connection.sh
```

### Manual
```bash
# Test backend
curl https://real-production-4319.up.railway.app/api/properties/

# Test frontend
open https://bellrockholdings.org
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| CORS errors | Update Railway CORS_ALLOWED_ORIGINS |
| 404 errors | Check Vercel VITE_API_BASE_URL |
| Env vars not working | Redeploy after changes |
| Still using localhost | Clear browser cache |

See [VERCEL_RAILWAY_CONNECTION.md](VERCEL_RAILWAY_CONNECTION.md) for detailed troubleshooting.

## 🔗 Important Links

- **Frontend:** https://bellrockholdings.org
- **Backend API:** https://real-production-4319.up.railway.app/api/
- **Admin Panel:** https://real-production-4319.up.railway.app/admin/
- **Railway Dashboard:** https://railway.app/
- **Vercel Dashboard:** https://vercel.com/

## 📊 Architecture

```
User Browser
    ↓
Vercel Frontend (bellrockholdings.org)
    ↓
Railway Backend (real-production-4319.up.railway.app)
    ↓
PostgreSQL + DigitalOcean Spaces
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture.

## ✅ Success Criteria

- [ ] Frontend loads at bellrockholdings.org
- [ ] Properties page shows data
- [ ] Investments page shows data
- [ ] No CORS errors
- [ ] Images load from DigitalOcean Spaces

## 📞 Need Help?

1. Check [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
2. Review [VERCEL_RAILWAY_CONNECTION.md](VERCEL_RAILWAY_CONNECTION.md)
3. Run `./verify_connection.sh`
4. Check Railway/Vercel logs

## 🎉 Next Steps

After successful deployment:
- [ ] Set up monitoring
- [ ] Configure backups
- [ ] Add custom domain (if needed)
- [ ] Set up CI/CD pipeline
- [ ] Enable error tracking
- [ ] Configure CDN

---

**Last Updated:** March 28, 2026
**Status:** Ready for deployment
