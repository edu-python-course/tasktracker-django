"""
Tasks application models

"""

from django.contrib.auth import get_user_model
from django.contrib.postgres.functions import RandomUUID
from django.db import models
from django.urls import reverse

UserModel = get_user_model()


class TaskModel(models.Model):
    """
    Task model implementation

    :ivar uuid: primary key
    :type uuid: :class: `uuid.UUID`
    :ivar summary: title, or short description (up to 128 characters).
    :type summary: str
    :ivar description: detailed description, defaults to None.
    :type description: str
    :ivar completed: completed status, defaults to False.
    :type completed: bool
    :ivar created_at: created timestamp, non-editable.
    :type created_at: :class: `datetime.datetime`
    :ivar updated_at: updated timestamp, non-editable.
    :type updated_at: :class: `datetime.datetime`
    :ivar assignee: reference to a user that task is assigned to (optional).
    :ivar reporter: reference to a user that created the task.

    Represents a tasks registered in the system.
    Each new task is created as uncompleted by default.
    Each task gets its created timestamp automatically on task creation.
    Each task updates its updated timestamp automatically on task save.

    """

    class Meta:
        db_table = "task"
        ordering = ("-created_at", "-updated_at")
        verbose_name = "task"
        verbose_name_plural = "tasks"  # default behavior

    uuid = models.UUIDField(
        default=RandomUUID(),
        editable=False,
        primary_key=True,
        verbose_name="primary key"
    )

    summary = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # users model relationship
    assignee = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks_assigned"
    )
    reporter = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
        related_name="tasks_reported"
    )

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.summary

    def get_absolute_url(self) -> str:
        """
        Return a URL to the task detail page

        :raise: `django.core.exceptions.ObjectDoesNotExist`

        """

        # Since RandomUUID function is used to generate primary key value,
        # task instance should be fetched from the database first.
        # You can avoid this behavior by using ``uuid.uuid4`` to generate
        # uuid value.

        fetched_obj = TaskModel.objects.get(
            reporter_id=self.reporter_id,
            created_at=self.created_at
        )

        return reverse("tasks:detail", args=(fetched_obj.pk,))
