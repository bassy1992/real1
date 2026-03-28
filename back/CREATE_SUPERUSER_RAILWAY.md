# Create Superuser on Railway

This guide shows you how to create a Django superuser on Railway.

## Method 1: Using Railway CLI (Recommended)

### Prerequisites
- Railway CLI installed: `npm install -g @railway/cli`
- Logged in: `railway login`

### Steps

1. **Link to your Railway project:**
   ```bash
   railway link
   ```

2. **Run the createsuperuser command:**
   ```bash
   railway run python manage.py createsuperuser
   ```

3. **Follow the prompts:**
   - Username: `admin` (or your choice)
   - Email: `admin@bellrockholdings.org`
   - Password: (enter a secure password)
   - Password (again): (confirm password)

4. **Done!** You can now login at:
   ```
   https://real-production-4319.up.railway.app/admin/
   ```

## Method 2: Using Environment Variables (Automated)

This method automatically creates a superuser on deployment.

### Steps

1. **Add environment variables to Railway:**

   Go to Railway Dashboard → Your Project → Variables → Add:

   ```bash
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_EMAIL=admin@bellrockholdings.org
   DJANGO_SUPERUSER_PASSWORD=YourSecurePassword123!
   ```

2. **Update your start script:**

   Edit `railway_start.sh` to include the superuser creation command:

   ```bash
   #!/bin/bash
   
   # Run migrations
   python manage.py migrate --noinput
   
   # Collect static files
   python manage.py collectstatic --noinput
   
   # Create superuser if it doesn't exist
   python manage.py create_superuser
   
   # Start the server
   gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
   ```

3. **Redeploy:**
   ```bash
   git add .
   git commit -m "Add automatic superuser creation"
   git push
   ```

4. **Check logs:**
   ```bash
   railway logs
   ```
   
   Look for: `✅ Superuser "admin" created successfully!`

## Method 3: Using Railway Shell (Interactive)

### Steps

1. **Open Railway shell:**
   ```bash
   railway shell
   ```

2. **Run Django shell:**
   ```bash
   python manage.py shell
   ```

3. **Create superuser programmatically:**
   ```python
   from django.contrib.auth import get_user_model
   User = get_user_model()
   
   User.objects.create_superuser(
       username='admin',
       email='admin@bellrockholdings.org',
       password='YourSecurePassword123!'
   )
   
   print("Superuser created!")
   exit()
   ```

## Method 4: Using Railway Dashboard (One-time Command)

### Steps

1. **Go to Railway Dashboard**
2. **Select your project**
3. **Click on your backend service**
4. **Go to "Settings" tab**
5. **Scroll to "Deploy" section**
6. **Click "Run a command"**
7. **Enter:**
   ```bash
   python manage.py createsuperuser --noinput --username admin --email admin@bellrockholdings.org
   ```
   
   Note: This won't work without setting DJANGO_SUPERUSER_PASSWORD first.

## Recommended Approach

**Use Method 2 (Environment Variables)** for production because:
- ✅ Automatic on deployment
- ✅ Secure (password in environment variables)
- ✅ Idempotent (won't create duplicates)
- ✅ No manual intervention needed

## Security Best Practices

### Strong Password Requirements
- Minimum 12 characters
- Mix of uppercase and lowercase
- Include numbers and special characters
- Don't use common words or patterns

### Example Strong Passwords
```
BellRock2026!Secure#Admin
AdminBR$2026*SecurePass
BR-Admin-2026!Secure#99
```

### After Creating Superuser

1. **Login immediately:**
   ```
   https://real-production-4319.up.railway.app/admin/
   ```

2. **Change password if needed:**
   - Login → Top right → Change password

3. **Create additional staff users:**
   - Admin → Users → Add user
   - Set appropriate permissions

4. **Enable two-factor authentication (optional):**
   - Install `django-otp` or similar package

## Troubleshooting

### Error: "Superuser already exists"

**Solution:** The superuser is already created. Try logging in or reset the password:

```bash
railway run python manage.py changepassword admin
```

### Error: "DJANGO_SUPERUSER_PASSWORD is required"

**Solution:** Set the environment variable in Railway:

1. Railway Dashboard → Variables
2. Add: `DJANGO_SUPERUSER_PASSWORD=YourPassword`
3. Redeploy

### Error: "This password is too common"

**Solution:** Use a stronger password with:
- At least 12 characters
- Mix of letters, numbers, and symbols

### Error: "Unable to connect to database"

**Solution:** 
1. Check DATABASE_URL is set in Railway
2. Verify database is running
3. Check Railway logs for connection errors

### Can't login after creating superuser

**Solution:**
1. Verify username and password
2. Check if user is active:
   ```bash
   railway run python manage.py shell
   ```
   ```python
   from django.contrib.auth import get_user_model
   User = get_user_model()
   user = User.objects.get(username='admin')
   print(f"Active: {user.is_active}")
   print(f"Staff: {user.is_staff}")
   print(f"Superuser: {user.is_superuser}")
   ```

## Verification

After creating the superuser, verify it works:

1. **Visit admin panel:**
   ```
   https://real-production-4319.up.railway.app/admin/
   ```

2. **Login with credentials:**
   - Username: `admin`
   - Password: (your password)

3. **Check permissions:**
   - You should see all models (Properties, Investments, etc.)
   - You should be able to add/edit/delete records

## Managing Multiple Superusers

### Create additional superusers:

```bash
railway run python manage.py createsuperuser
```

### List all superusers:

```bash
railway run python manage.py shell
```

```python
from django.contrib.auth import get_user_model
User = get_user_model()

superusers = User.objects.filter(is_superuser=True)
for user in superusers:
    print(f"Username: {user.username}, Email: {user.email}")
```

### Delete a superuser:

```bash
railway run python manage.py shell
```

```python
from django.contrib.auth import get_user_model
User = get_user_model()

user = User.objects.get(username='admin')
user.delete()
print("Superuser deleted")
```

## Automated Setup Script

For convenience, here's a complete setup script:

```bash
#!/bin/bash
# setup_railway_superuser.sh

echo "🚀 Setting up Railway Superuser..."

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Installing..."
    npm install -g @railway/cli
fi

# Login to Railway
echo "📝 Logging in to Railway..."
railway login

# Link to project
echo "🔗 Linking to project..."
railway link

# Create superuser
echo "👤 Creating superuser..."
railway run python manage.py create_superuser

echo "✅ Done! You can now login at:"
echo "   https://real-production-4319.up.railway.app/admin/"
```

Save as `setup_railway_superuser.sh` and run:
```bash
chmod +x setup_railway_superuser.sh
./setup_railway_superuser.sh
```

## Quick Reference

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| Railway CLI | Interactive, secure | Requires CLI setup | One-time setup |
| Environment Variables | Automatic, idempotent | Password in env vars | Production |
| Railway Shell | Direct access | Manual process | Debugging |
| Dashboard Command | No CLI needed | Limited functionality | Quick fixes |

## Next Steps

After creating your superuser:

1. ✅ Login to admin panel
2. ✅ Create additional staff users
3. ✅ Set up user permissions
4. ✅ Configure admin settings
5. ✅ Test CRUD operations
6. ✅ Upload test images
7. ✅ Create test properties

## Support

If you encounter issues:
1. Check Railway logs: `railway logs`
2. Verify environment variables are set
3. Ensure database is connected
4. Check Django settings for ALLOWED_HOSTS

---

**Last Updated:** March 28, 2026  
**Status:** ✅ Ready to use
