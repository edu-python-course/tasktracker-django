"""
Tasks application serializers

"""

from rest_framework import serializers

from tasks.models import TaskModel
from users.serializers import UserModelSerializer


class TaskModelReadSerializer(serializers.ModelSerializer):
    """
    Read-only task model serializer

    """

    reporter = UserModelSerializer()
    assignee = UserModelSerializer()

    class Meta:
        model = TaskModel
        fields = "__all__"


class TaskModelWriteSerializer(serializers.ModelSerializer):
    """
    Task model serializer

    """

    class Meta:
        model = TaskModel
        fields = "__all__"

    def update(self, instance, validated_data):
        # ensure that ``reporter`` field would not be updated
        validated_data.pop("reporter", None)

        return super().update(instance, validated_data)
