from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config
import os


class Command(BaseCommand):
    help = 'Create a superuser from environment variables'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get credentials from environment variables
        username = config('DJANGO_SUPERUSER_USERNAME', default='admin')
        email = config('DJANGO_SUPERUSER_EMAIL', default='admin@bellrockholdings.org')
        password = config('DJANGO_SUPERUSER_PASSWORD', default=None)
        
        if not password:
            self.stdout.write(
                self.style.ERROR('DJANGO_SUPERUSER_PASSWORD environment variable is required!')
            )
            self.stdout.write(
                self.style.WARNING('Set it in Railway: DJANGO_SUPERUSER_PASSWORD=your_secure_password')
            )
            return
        
        # Check if superuser already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING(f'Superuser "{username}" already exists. Skipping creation.')
            )
            return
        
        # Create superuser
        try:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(
                self.style.SUCCESS(f'✅ Superuser "{username}" created successfully!')
            )
            self.stdout.write(
                self.style.SUCCESS(f'   Email: {email}')
            )
            self.stdout.write(
                self.style.SUCCESS(f'   You can now login at: /admin/')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )
