"""
Tasks application serializers

"""

from rest_framework import exceptions, serializers

from tasks.models import TaskModel
from users.serializers import UserModelSerializer


class TaskModelReadSerializer(serializers.ModelSerializer):
    """
    Used to retrieve data on task instances

    This serializer should not be used to create or update tasks.

    """

    assignee = UserModelSerializer(read_only=True)
    reporter = UserModelSerializer(read_only=True)

    class Meta:
        model = TaskModel
        fields = "__all__"

    def create(self, validated_data):
        raise exceptions.PermissionDenied(
            "Cannot create instance using read-only serializer"
        )

    def update(self, instance, validated_data):
        raise exceptions.PermissionDenied(
            "Cannot update instance using read-only serializer"
        )
