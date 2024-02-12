"""
Tasks application serializers

"""

from django.contrib.auth import get_user_model
from rest_framework import exceptions, serializers

from tasks.models import TaskModel
from users.serializers import UserModelSerializer

UserModel = get_user_model()


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


class TaskModelWriteSerializer(serializers.ModelSerializer):
    """
    Used to create and update task instances

    """

    class Meta:
        model = TaskModel
        fields = "__all__"

    def update(self, instance, validated_data):
        if "reporter" in validated_data:
            del validated_data["reporter"]

        return super().update(instance, validated_data)

    # noinspection PyMethodMayBeStatic
    def validate_assignee(self, value: UserModel):
        """
        Validate assignee

        Cannot be superuser, or inactive user.

        """

        if value.is_superuser or not value.is_active:
            raise serializers.ValidationError("Invalid value")

        return value
