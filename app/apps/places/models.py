import uuid
from django.db import models


class Place(models.Model):
    """
    Place
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique identifier",
    )
    name = models.CharField(
        max_length=255,
        help_text="Name of the place",
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Description of the place",
    )

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"

    def __str__(self):
        return self.name
