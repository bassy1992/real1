#!/usr/bin/env python
"""
Simple script to create a superuser on Railway.
Run this with: railway run python create_admin.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Superuser credentials
username = 'admin'
email = 'admin@bellrockholdings.org'
password = 'logan123@'

# Check if user already exists
if User.objects.filter(username=username).exists():
    print(f"❌ User '{username}' already exists!")
    user = User.objects.get(username=username)
    print(f"   Email: {user.email}")
    print(f"   Is superuser: {user.is_superuser}")
    print(f"   Is staff: {user.is_staff}")
    print(f"   Is active: {user.is_active}")
    
    # Update password
    user.set_password(password)
    user.save()
    print(f"✅ Password updated for '{username}'")
else:
    # Create superuser
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"✅ Superuser '{username}' created successfully!")
    print(f"   Email: {email}")
    print(f"   Password: {password}")

print("\n🌐 Login at: https://real-production-4319.up.railway.app/admin/")
print(f"   Username: {username}")
print(f"   Password: {password}")
