from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection


class Command(BaseCommand):
    help = 'Test database connection and list users'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Test database connection
        self.stdout.write(self.style.WARNING('🔍 Testing database connection...'))
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            self.stdout.write(self.style.SUCCESS('✅ Database connection OK'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Database connection failed: {e}'))
            return
        
        # List all users
        self.stdout.write(self.style.WARNING('\n📋 Listing all users:'))
        users = User.objects.all()
        
        if not users:
            self.stdout.write(self.style.WARNING('   No users found in database'))
        else:
            for user in users:
                self.stdout.write(self.style.SUCCESS(f'   - {user.username} (staff={user.is_staff}, superuser={user.is_superuser})'))
        
        self.stdout.write(self.style.WARNING(f'\n📊 Total users: {users.count()}'))
