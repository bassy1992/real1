from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
    help = 'Ensure superuser exists with specific credentials'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get credentials from environment variables
        username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        
        if not password:
            self.stdout.write(self.style.ERROR('❌ DJANGO_SUPERUSER_PASSWORD environment variable is not set'))
            self.stdout.write(self.style.WARNING('   Set it in Railway Variables to create superuser'))
            return
        
        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists'))
            
            # Update password and ensure superuser status
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.save()
            
            self.stdout.write(self.style.SUCCESS(f'✅ Password updated for "{username}"'))
            self.stdout.write(self.style.SUCCESS(f'   Username: {username}'))
            
        except User.DoesNotExist:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'✅ Superuser "{username}" created!'))
            self.stdout.write(self.style.SUCCESS(f'   Username: {username}'))
            self.stdout.write(self.style.SUCCESS(f'   Email: {email}'))
