from core.models import PublicIdModel, TimeStampedModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class User(AbstractUser, PublicIdModel, TimeStampedModel):
    """Custom Model for users."""

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        blank=True, null=True
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=True
    )

    objects = UserManager()

    def to_dict(self):
        """Convert instance to json."""

        return {
            'id': self.public_id,
            'email': self.email,
            'is_active': self.is_active,
            'date_joined': self.date_joined
        }
