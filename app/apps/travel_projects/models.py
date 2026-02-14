from django.conf import settings
import uuid
from django.db import models


class TravelProject(models.Model):
    """
    Travel Project
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Unique identifier",
    )

    name = models.CharField(
        max_length=255,
        default="Untitled Travel Project",
        help_text="Travel Project for user",
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text="Description of the travel project",
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="travel_projects",
        blank=True,
        null=True,
        help_text="Project Owner",
    )

    class Meta:
        verbose_name = "Travel Project"
        verbose_name_plural = "Travel Projects"

    def __str__(self):
        return self.name
