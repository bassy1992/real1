#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
This is a wrapper that delegates to back/manage.py
"""
import os
import sys

if __name__ == '__main__':
    # Change to the back directory where the actual Django project is
    os.chdir('back')
    
    # Add back directory to Python path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'back'))
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
