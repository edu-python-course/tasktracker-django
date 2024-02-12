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

    pk = serializers.IntegerField(read_only=True)

    password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=150, write_only=True)
    email = serializers.EmailField()

    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data["username"]
        instance.email = validated_data["email"]
        instance.set_password(validated_data["password"])

        first_name = validated_data.get("first_name", instance.first_name)
        instance.first_name = first_name
        last_name = validated_data.get("last_name", instance.last_name)
        instance.last_name = last_name

        instance.save()

        return instance
