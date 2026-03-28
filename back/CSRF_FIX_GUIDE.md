# CSRF Error Fix Guide

## What Changed

Updated Django settings to properly handle CSRF tokens for both the admin interface and REST API.

## Changes Made

1. **Enhanced CSRF Cookie Settings** (`back/backend/settings.py`):
   - Set explicit `CSRF_COOKIE_NAME` and `CSRF_HEADER_NAME`
   - Disabled `CSRF_COOKIE_DOMAIN` in development mode
   - Kept `CSRF_COOKIE_HTTPONLY = False` to allow JavaScript access

2. **REST Framework Configuration**:
   - Added `SessionAuthentication` for proper CSRF handling
   - Set `AllowAny` permissions for public API endpoints
   - This allows REST API to work without CSRF for GET requests

## If You're Seeing CSRF Error in Django Admin

### Quick Fixes:

1. **Clear Browser Cookies**:
   - Open browser DevTools (F12)
   - Go to Application/Storage tab
   - Clear all cookies for your domain
   - Refresh the page

2. **Check Your Browser**:
   - Ensure cookies are enabled
   - Disable any cookie-blocking extensions temporarily
   - Try in incognito/private mode

3. **For Development (localhost)**:
   - Make sure you're accessing via `http://127.0.0.1:8000` or `http://localhost:8000`
   - Don't mix localhost and 127.0.0.1 in the same session

4. **For Production (Railway)**:
   - Ensure your domain is in `CSRF_TRUSTED_ORIGINS`
   - Check that `ALLOWED_HOSTS` includes your Railway domain
   - Verify you're using HTTPS

### Environment Variables to Check:

```bash
# In Railway, ensure these are set:
CSRF_TRUSTED_ORIGINS=https://your-railway-domain.up.railway.app,https://bellrockholdings.org
ALLOWED_HOSTS=your-railway-domain.up.railway.app,bellrockholdings.org
CORS_ALLOWED_ORIGINS=https://bellrockholdings.org,https://www.bellrockholdings.org
```

## Testing the Fix

### Test Django Admin:
1. Navigate to `/admin/`
2. Try to log in
3. Should work without CSRF errors

### Test REST API:
```bash
# GET requests (should work without CSRF)
curl http://localhost:8000/api/properties/

# POST requests (will need CSRF token if using SessionAuthentication)
curl -X POST http://localhost:8000/api/properties/ \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: <token>" \
  -d '{"title": "Test"}'
```

## For Future POST Requests from Frontend

If you add POST/PUT/DELETE requests from your React frontend, you'll need to:

1. **Get CSRF Token**:
```typescript
function getCookie(name: string): string | null {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop()?.split(';').shift() || null;
  return null;
}

const csrfToken = getCookie('csrftoken');
```

2. **Include in Requests**:
```typescript
fetch(`${API_BASE_URL}/api/endpoint/`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken || '',
  },
  credentials: 'include', // Important for cookies
  body: JSON.stringify(data),
});
```

## Troubleshooting

### Still Getting CSRF Error?

1. Check Django logs for specific error details
2. Verify middleware order in settings.py
3. Ensure `CsrfViewMiddleware` is enabled
4. Check that `CORS_ALLOW_CREDENTIALS = True`

### For Railway Deployment:

```bash
# SSH into Railway and check
python manage.py shell

# In shell:
from django.conf import settings
print(settings.CSRF_TRUSTED_ORIGINS)
print(settings.ALLOWED_HOSTS)
print(settings.CORS_ALLOWED_ORIGINS)
```

## Summary

The CSRF configuration is now properly set up for:
- ✅ Django Admin interface (requires CSRF token)
- ✅ REST API GET requests (no CSRF needed)
- ✅ REST API POST/PUT/DELETE (will need CSRF token when implemented)
- ✅ Cross-origin requests from your frontend
