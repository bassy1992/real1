# Admin Login Troubleshooting

## Current Credentials

- **Username**: `admin`
- **Password**: `logan123@`
- **Admin URL**: `https://real-production-4319.up.railway.app/admin/`

## If You Can't Login

### Step 1: Wait for Railway Deployment
The CSRF fixes need to deploy first. Check Railway dashboard to ensure deployment is complete.

### Step 2: Clear Browser Data
1. Open DevTools (F12)
2. Go to Application → Storage
3. Click "Clear site data"
4. Refresh the page

### Step 3: Try Incognito Mode
Open the admin URL in an incognito/private window to rule out cookie issues.

### Step 4: Reset Superuser via Railway CLI

If still having issues, run this command in Railway:

```bash
# In Railway CLI or via Railway dashboard shell
python manage.py ensure_superuser
```

This will:
- Create the admin user if it doesn't exist
- Reset the password to `logan123@` if it does exist
- Ensure all superuser permissions are set

### Step 5: Manual Password Reset (Alternative)

If the above doesn't work, use Railway shell:

```bash
# Access Railway shell
railway shell

# Run Django shell
python manage.py shell

# In Python shell:
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.get(username='admin')
user.set_password('logan123@')
user.is_superuser = True
user.is_staff = True
user.is_active = True
user.save()
print("Password reset successfully!")
exit()
```

### Step 6: Check Railway Logs

```bash
railway logs
```

Look for any errors related to:
- Database connection
- User authentication
- CSRF tokens

## Common Issues

### Issue: "Please enter the correct username and password"
- **Cause**: Wrong credentials or user doesn't exist
- **Fix**: Run `python manage.py ensure_superuser` in Railway

### Issue: CSRF verification failed
- **Cause**: Cookie issues or CSRF configuration
- **Fix**: Clear cookies and wait for latest deployment

### Issue: "This account is inactive"
- **Cause**: User account is disabled
- **Fix**: Run the manual password reset script above (sets `is_active = True`)

### Issue: Can't access /admin/ at all
- **Cause**: Django not running or routing issue
- **Fix**: Check Railway logs and ensure service is running

## Verify Deployment

Check these URLs to ensure backend is running:

1. **Health Check**: `https://real-production-4319.up.railway.app/api/properties/`
   - Should return JSON with properties

2. **Admin Login**: `https://real-production-4319.up.railway.app/admin/`
   - Should show login form (not 404)

## Quick Test Script

Create a test to verify the user exists:

```bash
# In Railway shell
python manage.py shell

# Run this:
from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.filter(is_superuser=True)
for user in users:
    print(f"Username: {user.username}, Email: {user.email}, Active: {user.is_active}")
```

## Need to Create New Superuser?

If you want different credentials:

```bash
# In Railway shell
python manage.py createsuperuser

# Follow the prompts to enter:
# - Username
# - Email
# - Password (enter twice)
```

## Environment Variables to Check

In Railway dashboard, verify these are set:

```
SECRET_KEY=<your-secret-key>
DEBUG=False
DATABASE_URL=<automatically-set-by-railway>
ALLOWED_HOSTS=real-production-4319.up.railway.app
CSRF_TRUSTED_ORIGINS=https://real-production-4319.up.railway.app
```

## Still Having Issues?

1. Check Railway deployment logs for errors
2. Verify the database is connected (check Railway dashboard)
3. Ensure migrations have run: `python manage.py migrate`
4. Try creating a completely new superuser with different credentials
