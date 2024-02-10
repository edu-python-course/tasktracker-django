"""
Users application models

"""

from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, ImageField


class UserModel(AbstractUser):
    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ("last_name", "first_name", "username")

    email = EmailField(
        unique=True,
        verbose_name="email address",
    )
    image = ImageField(
        blank=True,
        default="avatars/default.svg",
        upload_to="avatars",
    )

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.get_full_name() or self.username
