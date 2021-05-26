from core.models import PublicIdModel, TimeStampedModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, PublicIdModel, TimeStampedModel):
    """Custom Model for users."""

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=True
    )
