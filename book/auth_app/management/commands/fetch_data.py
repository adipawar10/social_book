from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Fetch data from the local PostgreSQL database via SQL query'

    def handle(self, *args, **kwargs):
        # Your raw SQL query
        query = "SELECT * FROM auth_app_customuser;"

        # Execute the query
        with connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        # Print the fetched data
        for row in rows:
            self.stdout.write(str(row))
