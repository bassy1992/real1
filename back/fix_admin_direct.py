#!/usr/bin/env python
"""
Direct admin user fix script
Run this on Railway: railway run python fix_admin_direct.py
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model

def fix_admin():
    User = get_user_model()
    
    username = 'admin'
    email = 'admin@bellrockholdings.org'
    password = 'logan123@'
    
    try:
        user = User.objects.get(username=username)
        print(f"Found existing user: {username}")
        
        # Update password and permissions
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.email = email
        user.save()
        
        print("=" * 50)
        print("✅ SUCCESS! Admin user updated!")
        print("=" * 50)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Email: {email}")
        print(f"Is Staff: {user.is_staff}")
        print(f"Is Superuser: {user.is_superuser}")
        print(f"Is Active: {user.is_active}")
        print("=" * 50)
        
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print("=" * 50)
        print("✅ SUCCESS! Admin user created!")
        print("=" * 50)
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Email: {email}")
        print("=" * 50)
    
    # Verify the user can authenticate
    from django.contrib.auth import authenticate
    auth_user = authenticate(username=username, password=password)
    if auth_user:
        print("✅ Authentication test PASSED")
    else:
        print("❌ Authentication test FAILED - something is wrong")
    
    return user

if __name__ == '__main__':
    fix_admin()
