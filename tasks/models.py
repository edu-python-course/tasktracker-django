"""
Tasks application models

"""

import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy

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
    :ivar assignee: reference to a user that task is assigned to.
    :type assignee: :class: `UserModel`, optional
    :ivar reporter: reference to a user that created the task.
    :type reporter: :class: `UserModel`

    Represents a tasks registered in the system.
    Each new task is created as uncompleted by default.
    Each task gets its ``created_at`` timestamp once on task creation.
    Each task updates its ``updated_at`` timestamp on each task save.

    """

    class Meta:
        db_table = "task"
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ("-updated_at", "-created_at")

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
        verbose_name="primary key",
    )

    summary = models.CharField(
        max_length=128,
        help_text="Required. 128 characters or fewer."
    )
    description = models.TextField(
        blank=True,
        default="",
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="completed status"
    )

    # task metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # relationships
    assignee = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks_assigned",
        verbose_name="assigned to",
    )
    reporter = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
        related_name="tasks_reported",
        verbose_name="reported by",
    )

    @property
    def title(self) -> str:
        return str(self)

    def __str__(self) -> str:
        """Return a string version of an instance"""

        return self.summary

    def can_delete(self, user: UserModel) -> bool:
        """
        Check if the user permitted to delete this instance

        """

        return self.reporter == user

    def can_update(self, user: UserModel) -> bool:
        """
        Check if the user permitted to edit this instance

        """

        return self.assignee == user or self.reporter == user

    def get_absolute_url(self) -> str:
        """
        Return URL path to the instance detail view

        """

        return reverse_lazy("tasks:detail", args=(self.pk,))
