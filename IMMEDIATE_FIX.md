# IMMEDIATE FIX - Run This Now

## Option 1: Using Railway CLI (FASTEST)

```bash
# 1. Install Railway CLI (if not installed)
npm install -g @railway/cli

# 2. Login
railway login

# 3. Link to your project (choose the backend service)
cd back
railway link

# 4. Run the fix script directly
railway run python fix_admin_direct.py
```

This will immediately fix the admin user on your production database.

## Option 2: Using Railway Dashboard

1. Go to https://railway.app/dashboard
2. Open your backend service
3. Click on "Settings" tab
4. Scroll to "Service Variables"
5. Click "Raw Editor"
6. Add these variables if not present:
   ```
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_EMAIL=admin@bellrockholdings.org
   DJANGO_SUPERUSER_PASSWORD=logan123@
   ```
7. Go to "Deployments" tab
8. Click "Deploy" to trigger a new deployment

## Option 3: Railway Shell (MOST RELIABLE)

1. Go to Railway dashboard
2. Open your backend service
3. Click on the "..." menu (three dots)
4. Select "Shell" or "Connect"
5. In the shell, run:
   ```bash
   python manage.py shell
   ```
6. Paste this code:
   ```python
   from django.contrib.auth import get_user_model
   User = get_user_model()
   user = User.objects.get(username='admin')
   user.set_password('logan123@')
   user.is_superuser = True
   user.is_staff = True
   user.is_active = True
   user.save()
   print("Password reset!")
   exit()
   ```

## After Running Any Option Above

Login at: https://real-production-4319.up.railway.app/admin/

- **Username**: `admin`
- **Password**: `logan123@`

## If STILL Not Working

Check Railway logs for errors:
```bash
railway logs
```

Or verify the user exists:
```bash
railway run python manage.py shell
```
Then:
```python
from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.all()
for u in users:
    print(f"User: {u.username}, Staff: {u.is_staff}, Super: {u.is_superuser}, Active: {u.is_active}")
```
