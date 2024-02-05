"""
Users application models

"""

from django.contrib.auth.models import AbstractUser
from django.db.models import ImageField


# Current project may be not the best example to demonstrate custom user
# model usage. There are migrations dependent on built-in auth application,
# that cannot be unapply. The Django documentation recommends to implement
# custom user model for every newly started project. Otherwise, it says to
# extend existing built-in user model with 1-to-1 relationship to other
# models.
class UserModel(AbstractUser):
    """
    User model implementation

    """

    class Meta:
        db_table = "user"
        verbose_name = "user"
        verbose_name_plural = "users"

    image = ImageField(
        upload_to="avatars",
        default="avatars/default.svg",
        blank=True,
    )

    def __str__(self) -> str:
        """
        Return a string version of an instance

        """

        return self.get_full_name() or self.username

    @classmethod
    def get_default_image(cls) -> str:
        """
        Return the default image name

        """

        return cls._meta.get_field("image").get_default()
