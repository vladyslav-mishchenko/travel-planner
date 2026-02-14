"""
load_places.py

Django management command to fetch places data from an external API
and load it into the database.

This command retrieves a list of data from the Art Institute of Chicago API,
fetches detailed information for each item, and creates or updates
Place records in the database with the retrieved data.

Usage:
    python manage.py load_places

Behavior:
    - Fetches a list of data from the external API.
    - Iterates through each item to get detailed data.
    - Updates existing Place records or creates new ones.
    - Logs success and failure messages to the console.

Note:
    - Requests failures are logged but do not stop processing.
    - Functionality is under active development and may change.
"""

from django.core.management.base import BaseCommand
import requests

from apps.places.models import Place


class Command(BaseCommand):
    help = "Load places from external API"

    def handle(self, *args, **options):
        url = "https://api.artic.edu/api/v1/artworks/search"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            self.stderr.write(f"Request failed: {e}")
            return

        data = response.json()
        places = data["data"]

        for place in places:
            link = place["api_link"]

            try:
                response_place = requests.get(link, timeout=10)
                response_place.raise_for_status()
            except requests.RequestException as e:
                self.stderr.write(f"Request failed: {e}")

            response_place_data = response_place.json()
            place_data = response_place_data["data"]

            place, created = Place.objects.update_or_create(
                name=place_data["title"],
                defaults={
                    "description": place_data["description"],
                },
            )

            if created:
                print(f"Created: {place}")
            else:
                print(f"Exists: {place}")
