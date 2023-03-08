"""
Django Command wait for the database to  be available
"""
import time
from django.core.management.base import BaseCommand
from mysql.connector.errors import Error as MysqlError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """ Django Command to wait fro the database. """
    def handle(self, *args, **options):
        """ Entrpoint for command """
        self.stdout.write('waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (MysqlError, OperationalError):
                self.stdout.write("Database Unavailable, waiting for 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
