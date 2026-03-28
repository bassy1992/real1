from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Reset admin password - EMERGENCY USE ONLY'

    def handle(self, *args, **options):
        User = get_user_model()
        
        try:
            user = User.objects.get(username='admin')
            user.set_password('logan123@')
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.save()
            
            self.stdout.write(self.style.SUCCESS('✅ Admin password reset to: logan123@'))
            
        except User.DoesNotExist:
            user = User.objects.create_superuser('admin', 'admin@bellrockholdings.org', 'logan123@')
            self.stdout.write(self.style.SUCCESS('✅ Admin user created with password: logan123@'))
