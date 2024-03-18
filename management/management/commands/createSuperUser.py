# management/management/commands/createSuperUser.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

# This is a Python class named Command that likely inherits from BaseCommand.
class Command(BaseCommand):
    help = 'Create a superuser programmatically'

    def handle(self, *args, **options):
        """
        The function checks if a superuser exists and creates one if not, providing appropriate messages
        for different outcomes.
        :return: If a superuser already exists, a warning message is printed and the function returns
        without creating a new superuser.
        """
        """
        The function checks if a superuser already exists and creates one if not.
        :return: If a superuser already exists, a warning message is printed and the function returns
        without creating a new superuser. If a new superuser is successfully created, a success message
        is printed. If an error occurs during the creation of the superuser, an error message is
        printed.
        """
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