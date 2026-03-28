#!/usr/bin/env python3
"""
Railway Deployment Pre-flight Check
Run this script before deploying to verify everything is configured correctly.
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a required file exists."""
    if Path(filepath).exists():
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} MISSING: {filepath}")
        return False

def check_requirements():
    """Verify all required files exist."""
    print("\n🔍 Checking Required Files...\n")
    
    checks = [
        ("requirements.txt", "Dependencies file"),
        ("railway.json", "Railway config"),
        ("Procfile", "Process file"),
        ("nixpacks.toml", "Nixpacks config"),
        ("manage.py", "Django management script"),
        ("backend/settings.py", "Django settings"),
        ("backend/wsgi.py", "WSGI application"),
        (".env.example", "Environment variables template"),
    ]
    
    all_passed = True
    for filepath, description in checks:
        if not check_file_exists(filepath, description):
            all_passed = False
    
    return all_passed

def check_settings():
    """Check Django settings configuration."""
    print("\n🔍 Checking Django Settings...\n")
    
    try:
        # Add parent directory to path
        sys.path.insert(0, str(Path(__file__).parent))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
        
        from django.conf import settings
        
        checks = {
            "WhiteNoise in MIDDLEWARE": 'whitenoise.middleware.WhiteNoiseMiddleware' in settings.MIDDLEWARE,
            "CORS middleware configured": 'corsheaders.middleware.CorsMiddleware' in settings.MIDDLEWARE,
            "Static files configured": hasattr(settings, 'STATIC_ROOT'),
            "Database URL support": hasattr(settings, 'DATABASES'),
            "Storages app installed": 'storages' in settings.INSTALLED_APPS,
        }
        
        all_passed = True
        for check_name, passed in checks.items():
            if passed:
                print(f"✅ {check_name}")
            else:
                print(f"❌ {check_name}")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"❌ Error checking settings: {e}")
        return False

def check_dependencies():
    """Check if all dependencies are installed."""
    print("\n🔍 Checking Dependencies...\n")
    
    required_packages = [
        'django',
        'djangorestframework',
        'corsheaders',
        'PIL',  # Pillow
        'unfold',
        'boto3',
        'storages',
        'gunicorn',
        'whitenoise',
        'psycopg2',
        'decouple',
        'dj_database_url',
    ]
    
    all_installed = True
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} NOT INSTALLED")
            all_installed = False
    
    return all_installed

def print_deployment_info():
    """Print deployment information."""
    print("\n" + "="*60)
    print("🚀 RAILWAY DEPLOYMENT INFORMATION")
    print("="*60)
    
    print("\n📋 Required Environment Variables for Railway:\n")
    env_vars = [
        ("SECRET_KEY", "Django secret key (generate new one!)"),
        ("DEBUG", "False"),
        ("ALLOWED_HOSTS", "*.railway.app"),
        ("DATABASE_URL", "Auto-set by Railway PostgreSQL"),
        ("USE_SPACES", "True"),
        ("DO_SPACES_KEY", "Your DigitalOcean Spaces key"),
        ("DO_SPACES_SECRET", "Your DigitalOcean Spaces secret"),
        ("DO_SPACES_BUCKET_NAME", "Your bucket name"),
        ("DO_SPACES_ENDPOINT_URL", "https://sfo3.digitaloceanspaces.com"),
        ("DO_SPACES_REGION", "sfo3"),
        ("DO_SPACES_CDN_DOMAIN", "Your CDN domain"),
        ("CORS_ALLOWED_ORIGINS", "Your frontend URLs (comma-separated)"),
    ]
    
    for var_name, description in env_vars:
        print(f"  • {var_name}: {description}")
    
    print("\n📝 Deployment Steps:\n")
    steps = [
        "1. Create new Railway project from GitHub",
        "2. Add PostgreSQL database",
        "3. Set environment variables (see above)",
        "4. Deploy (automatic)",
        "5. Create superuser via Railway shell",
        "6. Test API endpoints",
        "7. Update frontend with Railway URL",
    ]
    
    for step in steps:
        print(f"  {step}")
    
    print("\n🔗 Useful Commands:\n")
    commands = [
        ("Create superuser", "python manage.py createsuperuser"),
        ("Load properties", "python manage.py load_properties"),
        ("Load investments", "python manage.py load_investments"),
        ("Check deployment", "python manage.py check --deploy"),
    ]
    
    for cmd_name, cmd in commands:
        print(f"  • {cmd_name}:")
        print(f"    {cmd}")
    
    print("\n" + "="*60)

def main():
    """Run all pre-flight checks."""
    print("\n" + "="*60)
    print("🚀 RAILWAY DEPLOYMENT PRE-FLIGHT CHECK")
    print("="*60)
    
    files_ok = check_requirements()
    deps_ok = check_dependencies()
    settings_ok = check_settings()
    
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60 + "\n")
    
    if files_ok and deps_ok and settings_ok:
        print("✅ All checks passed! Ready for Railway deployment.")
        print_deployment_info()
        return 0
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        if not deps_ok:
            print("\n💡 Tip: Run 'pip install -r requirements.txt' to install dependencies")
        return 1

if __name__ == "__main__":
    sys.exit(main())
