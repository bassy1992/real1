from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Fix admin user permissions'

    def handle(self, *args, **options):
        admin_user, created = User.objects.get_or_create(username='admin')
        admin_user.email = 'admin@bellrockholdings.org'
        admin_user.set_password('logan123@')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.is_active = True
        admin_user.save()

        self.stdout.write(self.style.SUCCESS(f'Admin user fixed: {admin_user.username}'))
        self.stdout.write(f'  is_staff: {admin_user.is_staff}')
        self.stdout.write(f'  is_superuser: {admin_user.is_superuser}')
        self.stdout.write(f'  is_active: {admin_user.is_active}')
