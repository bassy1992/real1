#!/bin/bash
# Railway startup script with PostgreSQL library path fix

# Find and set PostgreSQL library path
export LD_LIBRARY_PATH=$(find /nix/store -name "libpq.so*" -exec dirname {} \; | head -1):$LD_LIBRARY_PATH

# Run migrations
python manage.py migrate

# Start gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
