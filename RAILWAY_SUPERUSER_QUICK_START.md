# 🚀 Quick Start: Create Railway Superuser

## Fastest Method (Recommended)

### Option 1: Using the Setup Script

```bash
./setup_railway_superuser.sh
```

Follow the prompts and you're done!

### Option 2: Manual Railway CLI

```bash
# Install Railway CLI (if not installed)
npm install -g @railway/cli

# Login
railway login

# Link to project
railway link

# Create superuser
railway run python manage.py createsuperuser
```

Enter when prompted:
- Username: `admin`
- Email: `admin@bellrockholdings.org`
- Password: (your secure password)

### Option 3: Automatic (Environment Variables)

1. **Add to Railway Dashboard → Variables:**
   ```bash
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_EMAIL=admin@bellrockholdings.org
   DJANGO_SUPERUSER_PASSWORD=YourSecurePassword123!
   ```

2. **Redeploy** (automatic on next push)

3. **Check logs:**
   ```bash
   railway logs
   ```
   Look for: `✅ Superuser "admin" created successfully!`

## Login

After creation, login at:
```
https://real-production-4319.up.railway.app/admin/
```

## Troubleshooting

### "Railway CLI not found"
```bash
npm install -g @railway/cli
```

### "Superuser already exists"
```bash
railway run python manage.py changepassword admin
```

### "Password too common"
Use a stronger password with:
- 12+ characters
- Mix of letters, numbers, symbols
- Example: `BellRock2026!Admin#Secure`

## Full Documentation

See `back/CREATE_SUPERUSER_RAILWAY.md` for complete guide.

---

**Quick Commands:**

```bash
# Create superuser
railway run python manage.py createsuperuser

# Change password
railway run python manage.py changepassword admin

# Check logs
railway logs

# Open admin
open https://real-production-4319.up.railway.app/admin/
```
