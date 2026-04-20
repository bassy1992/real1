from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create admin user with hardcoded credentials for Railway'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = 'logan'
        email = 'logan@bellrockholdings.org'
        password = 'logans123'
        
        # Delete existing user if exists
        User.objects.filter(username=username).delete()
        
        # Create new superuser
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        
        # Explicitly set all permissions
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        
        # Verify the user was created correctly
        user.refresh_from_db()
        
        self.stdout.write(self.style.SUCCESS(f'✅ Superuser "{username}" created successfully!'))
        self.stdout.write(self.style.SUCCESS(f'   Username: {username}'))
        self.stdout.write(self.style.SUCCESS(f'   Email: {email}'))
        self.stdout.write(self.style.SUCCESS(f'   Password: {password}'))
        self.stdout.write(self.style.SUCCESS(f'   is_staff: {user.is_staff}'))
        self.stdout.write(self.style.SUCCESS(f'   is_superuser: {user.is_superuser}'))
        self.stdout.write(self.style.SUCCESS(f'   is_active: {user.is_active}'))
        self.stdout.write(self.style.SUCCESS(f'   Login at: /admin/'))
