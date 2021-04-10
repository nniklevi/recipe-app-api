import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Pauses execution until Database is ready

    Args:
        BaseCommand ([type]): [Base class for all Django Management Commands]
    """

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write("\nWaiting for the database...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second.")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available"))
