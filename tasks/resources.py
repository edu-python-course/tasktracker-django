"""
Tasks application API resources

"""

from rest_framework import permissions, viewsets

from tasks.models import TaskModel
from tasks.serializers import TaskModelReadSerializer, TaskModelWriteSerializer


class TaskModelViewSet(viewsets.ModelViewSet):
    """
    Task model resources (view set)

    """

    queryset = TaskModel.objects.all()

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TaskModelReadSerializer

        return TaskModelWriteSerializer
