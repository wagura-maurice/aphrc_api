# management/management/commands/migrateFresh.py
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection, transaction
from django.conf import settings
from django.db.utils import OperationalError

# This is a Python class named Command that likely inherits from BaseCommand.
class Command(BaseCommand):
    help = 'Drops the database, recreates it, and runs migrate.'

    def handle(self, *args, **options):
        """
        The function drops and recreates a database specified in the Django settings and then runs the
        migrate command.
        :return: If an exception occurs during the attempt to drop the database, the function will
        return early after rolling back the transaction. This is indicated by the `return` statement
        within the `except` block.
        """
        db_settings = settings.DATABASES['default']
        db_name = db_settings['NAME']

        self.stdout.write(f'Dropping database {db_name}...')
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'DROP DATABASE IF EXISTS `{db_name}`;')
                cursor.execute(f'CREATE DATABASE `{db_name}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;')
                transaction.commit()
            except OperationalError as e:
                self.stdout.write(f'Could not drop the database, maybe permissions issue. Error: {e}')
                transaction.rollback()
                return  # Important to stop execution if the database couldn't be dropped

        # Close the old connection to prevent issues since the database was dropped
        connection.close()

        # Run the migrate command
        self.stdout.write(f'Running migrate for database {db_name}...')
        call_command('migrate')
