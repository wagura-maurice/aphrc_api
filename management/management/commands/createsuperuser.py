# application/management/management/commands/createsuperuser.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser programmatically'

    def handle(self, *args, **options):
        # Check if the superuser already exists
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.WARNING('A superuser already exists.'))
            return

        # Create the superuser
        username = input('Enter username: ')
        email = input('Enter email address: ')
        password = input('Enter password: ')

        try:
            user = User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{user.username}" created successfully.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {e}'))