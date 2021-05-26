from users.models import User


class UserRepository:
    """User Repository."""

    MODEL = User

    @classmethod
    def create_user(cls, email, password, **kwargs):
        """Create user.
        Args:
            email(str): User email
            password(str): User Password
        Return:
            instance: User instance.
        """
        user = cls.MODEL.objects.create_user(
            email=email,
            password=password,
            is_active=kwargs.get('is_active', True),
            username=None
        )
        return user
