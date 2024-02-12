"""
Users application serializers

"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    """
    User serializer

    """

    pk = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = UserModel
        fields = (
            "pk", "username", "password", "email",
            "first_name", "last_name",
        )

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if "password" in validated_data:
            instance.set_password(validated_data["password"])
            instance.save()

        return instance

    def validate(self, attrs):
        username = attrs.get("username")
        if UserModel.objects.filter(username=username).exists():
            raise serializers.ValidationError({
                "username": "Username is already taken",
            })

        return attrs
