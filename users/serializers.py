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
