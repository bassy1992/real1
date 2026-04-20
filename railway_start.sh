#!/bin/bash

# Navigate to the back directory
cd back

# Run migrations
python manage.py migrate --noinput

# Ensure superuser exists
python manage.py ensure_superuser

# Fix admin permissions
python manage.py fix_admin_perms

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
