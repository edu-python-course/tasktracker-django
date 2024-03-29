from django.contrib.auth import get_user_model
from rest_framework import test

from users.serializers import UserModelSerializer

UserModel = get_user_model()


class TestUserSerializer(test.APITestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.data = {
            "username": "test_user",
            "email": "test@email.com",
            "password": "<PASSWORD>",
        }
        cls.new_data = {
            "username": "new_test",
            "email": "new_test@email.com",
            "password": "<NEW_PASSWORD>",
            "first_name": "John",
            "last_name": "Doe",
        }

    def test_user_creation(self):
        serializer = UserModelSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)

        username = self.data["username"]
        self.assertTrue(UserModel.objects.filter(username=username).exists())

    def test_user_update(self):
        instance = UserModel.objects.create_user(**self.data)
        serializer = UserModelSerializer(instance, data=self.new_data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, serializer.validated_data)

        instance.refresh_from_db()
        self.assertEqual(instance.username, self.new_data["username"])
        self.assertEqual(instance.email, self.new_data["email"])
        self.assertEqual(instance.first_name, self.new_data["first_name"])
        self.assertEqual(instance.last_name, self.new_data["last_name"])

    def test_password_hashed(self):
        serializer = UserModelSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.create(serializer.validated_data)

        self.assertTrue(instance.check_password(self.data["password"]))

        serializer = UserModelSerializer(instance, data=self.new_data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.update(instance, serializer.validated_data)

        self.assertTrue(instance.check_password(self.new_data["password"]))

    def test_username_validator(self):
        data = self.data.copy()
        data["username"] = "butime"
        serializer = UserModelSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_email_validator(self):
        data = self.data.copy()
        data["email"] = "WilcomeBrownlock@teleworm.us"
        serializer = UserModelSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_serialize_data(self):
        instance = UserModel.objects.filter(
            is_active=True, is_superuser=False
        ).first()
        serializer = UserModelSerializer(instance)
        self.assertIn("pk", serializer.data)
        self.assertIn("email", serializer.data)
        self.assertIn("first_name", serializer.data)
        self.assertIn("last_name", serializer.data)
