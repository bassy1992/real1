#!/bin/bash
# Railway start script for Django backend

cd back
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn backend.wsgi:application --bind 0.0.0.0:${PORT:-8000}
