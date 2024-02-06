"""
Users application serializers

"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.Serializer):
    """
    User serializer

    """

    pk = serializers.IntegerField(
        read_only=True
    )
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )
    username = serializers.CharField(
        max_length=150,
    )
    email = serializers.EmailField()

    def create(self, validated_data: dict) -> UserModel:
        """
        Create a model instance from validated data

        """

        return UserModel.objects.create_user(**validated_data)

    def update(self, instance: UserModel, validated_data: dict) -> UserModel:
        """
        Update a model instance from validated data

        """

        instance.username = validated_data["username"]
        instance.set_password(validated_data["password"])
        instance.email = validated_data["email"]
        instance.save()

        return instance
