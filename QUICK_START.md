# 🚀 Quick Start: Connect Railway to Vercel

## 1️⃣ Railway Environment Variables

Go to Railway → Your Project → Variables → Add these:

```bash
CORS_ALLOWED_ORIGINS=https://bellrockholdings.org,https://www.bellrockholdings.org
FRONTEND_URL=https://bellrockholdings.org
ALLOWED_HOSTS=real-production-4319.up.railway.app
DEBUG=False
```

Railway will auto-redeploy (wait 2-3 min).

## 2️⃣ Vercel Environment Variables

Go to Vercel → Your Project → Settings → Environment Variables → Add:

```bash
VITE_API_BASE_URL=https://real-production-4319.up.railway.app/api
```

Then redeploy your frontend.

## 3️⃣ Test

```bash
./verify_connection.sh
```

Or visit: https://bellrockholdings.org

## ✅ Done!

Your frontend should now load data from the Railway backend.

---

**Need help?** See `DEPLOYMENT_CHECKLIST.md` for detailed steps.
