"""
Tasks application API resources permissions

"""

from rest_framework import permissions


class TasksResourcePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Check if a user has permission to perform operation on task detail
        resource.

        Only reporters are permitted to remove their tasks.
        Only reporters or assignees are permitted to modify their tasks.

        """

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == "DELETE":
            return obj.reporter == request.user

        return obj.assignee == request.user or obj.reporter == request.user

    def has_permission(self, request, view):
        """
        Check if a user has permission to perform operation on tasks list
        resource.

        Only authenticated, non-admin users can create tasks.

        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and not request.user.is_superuser
