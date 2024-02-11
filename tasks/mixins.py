"""
Tasks application mixins

"""

from typing import Callable

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http.request import HttpRequest

UserModel = get_user_model()


class TaskCreatePermissionMixin(UserPassesTestMixin):
    """
    Used to test if a user can create a task instance

    """

    request: HttpRequest

    def test_func(self):
        user: UserModel = self.request.user

        return user.is_authenticated and not user.is_superuser


class TaskUpdatePermissionMixin(UserPassesTestMixin):
    """
    Used to test if a user can create a task instance

    """

    request: HttpRequest
    get_object: Callable

    def test_func(self):
        return self.get_object().can_update(self.request.user)


class TaskDeletePermissionMixin(UserPassesTestMixin):
    """
    Used to test if a user can create a task instance

    """

    request: HttpRequest
    get_object: Callable

    def test_func(self):
        return self.get_object().can_delete(self.request.user)
