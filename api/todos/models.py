from core.models import PublicIdModel, TimeStampedModel
from django.db import models
from users.models import User


class Lists(PublicIdModel, TimeStampedModel):
    """Model for List."""
    user = models.ForeignKey(
        User,
        models.DO_NOTHING,
        blank=False, null=False,
    )

    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "list"
        verbose_name_plural = "Lists"

    def __str__(self):
        return self.name


class Todos(PublicIdModel, TimeStampedModel):
    """Model for To-do."""

    lists = models.ForeignKey(
        Lists,
        models.DO_NOTHING,
        blank=False, null=False,
    )

    name = models.CharField(max_length=255)

    is_complete = models.BooleanField(
        default=True
    )

    class Meta:
        verbose_name = "todo"
        verbose_name_plural = "todos"

    def __str__(self):
        return self.name
