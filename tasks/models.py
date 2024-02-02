"""
Tasks application models

"""

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class TaskModel(models.Model):
    """
    Task model implementation

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
