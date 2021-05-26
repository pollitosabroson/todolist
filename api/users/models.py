from core.models import PublicIdModel, TimeStampedModel
from django.contrib.auth.base_user import AbstractBaseUser


# Create your models here.
class User(PublicIdModel, TimeStampedModel, AbstractBaseUser):
    """Custom Model for users."""
