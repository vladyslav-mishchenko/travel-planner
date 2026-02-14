import uuid
from django.db import models
from apps.places.models import Place
from apps.travel_projects.models import TravelProject


class TravelPlace(models.Model):
    """
    Travel Place
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique identifier",
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Notes of the place",
    )

    travel_project = models.ForeignKey(
        TravelProject,
        on_delete=models.PROTECT,
    )

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Travel Place"
        verbose_name_plural = "Travel Places"

    def __str__(self):
        return self.id
