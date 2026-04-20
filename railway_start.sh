#!/bin/bash

echo "========================================="
echo "🚀 RAILWAY STARTUP SCRIPT STARTING"
echo "========================================="

# Navigate to the back directory
cd back

echo "📂 Current directory: $(pwd)"
echo "📋 Files in directory:"
ls -la

# Run migrations
echo ""
echo "🔄 Running migrations..."
python manage.py migrate --noinput

# Test database
echo ""
echo "🧪 Testing database connection..."
python manage.py test_db

# Create admin user
echo ""
echo "👤 Creating admin user..."
python manage.py create_admin

# Test database again
echo ""
echo "🧪 Testing database after user creation..."
python manage.py test_db

# Fix admin permissions
echo ""
echo "🔧 Fixing admin permissions..."
python manage.py fix_admin_perms

# Collect static files
echo ""
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "========================================="
echo "✅ STARTUP SCRIPT COMPLETED"
echo "========================================="
echo ""

# Start Gunicorn
echo "🌐 Starting Gunicorn..."
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
