from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Ensure superuser exists with specific credentials'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = 'admin'
        email = 'admin@bellrockholdings.org'
        password = 'logan123@'
        
        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists'))
            
            # Update password
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.save()
            
            self.stdout.write(self.style.SUCCESS(f'✅ Password updated for "{username}"'))
            self.stdout.write(self.style.SUCCESS(f'   Username: {username}'))
            self.stdout.write(self.style.SUCCESS(f'   Password: {password}'))
            
        except User.DoesNotExist:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'✅ Superuser "{username}" created!'))
            self.stdout.write(self.style.SUCCESS(f'   Username: {username}'))
            self.stdout.write(self.style.SUCCESS(f'   Email: {email}'))
            self.stdout.write(self.style.SUCCESS(f'   Password: {password}'))
