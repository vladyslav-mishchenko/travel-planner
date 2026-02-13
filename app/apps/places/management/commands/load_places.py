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
                title=place_data["title"],
                defaults={
                    "description": place_data["description"],
                },
            )

            if created:
                print(f"Created: {place}")
            else:
                print(f"Exists: {place}")
