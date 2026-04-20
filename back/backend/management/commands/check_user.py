from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Check user permissions'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username to check')

    def handle(self, *args, **options):
        User = get_user_model()
        username = options['username']
        
        try:
            user = User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS(f'✅ User found: {user.username}'))
            self.stdout.write(f'   Email: {user.email}')
            self.stdout.write(f'   is_active: {user.is_active}')
            self.stdout.write(f'   is_staff: {user.is_staff}')
            self.stdout.write(f'   is_superuser: {user.is_superuser}')
            self.stdout.write(f'   last_login: {user.last_login}')
            self.stdout.write(f'   date_joined: {user.date_joined}')
            
            # Check password
            self.stdout.write(f'\n   Password hash: {user.password[:50]}...')
            
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'❌ User "{username}" not found'))
