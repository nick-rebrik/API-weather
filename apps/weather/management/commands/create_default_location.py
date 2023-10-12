import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.weather.models import Location

load_dotenv()

DEFAULT_LOCATION = os.environ.get('DEFAULT_LOCATION')


class Command(BaseCommand):
    def handle(self, *args, **options):
        location, created = Location.objects.get_or_create(name=DEFAULT_LOCATION, is_main=True)

        if created:
            self.stdout.write(self.style.SUCCESS(f'{DEFAULT_LOCATION} location created.'))
        else:
            self.stdout.write(self.style.WARNING(f'{DEFAULT_LOCATION} alredy exists.'))
