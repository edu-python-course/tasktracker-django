"""
Users application serializers

"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    """
    User model serializer

    This serializer is used to retrieve or update user instances.

    """

    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = UserModel
        fields = ("pk",
                  "username", "password", "confirm_password",
                  "first_name", "last_name", "email", "image")

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
            instance.save()

        return instance

    def validate(self, data: dict) -> dict:
        """
        Perform custom validations, before declared via model validators

        :raise: `rest_framework.exceptions.ValidationError`

        """

        # validate existing usernames
        if UserModel.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError({
                "username": "username is already taken",
            })

        # validate passwords match
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError({
                "password": "passwords don't match",
                "confirm_password": "passwords don't match",
            })

        # remove confirm password key
        if "confirm_password" in data:
            del data["confirm_password"]

        return super().validate(data)
