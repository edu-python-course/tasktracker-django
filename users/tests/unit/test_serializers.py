from django import test
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from users.serializers import UserModelSerializer

UserModel = get_user_model()


class TestUserModelSerializer(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.data = {
            "username": "test",
            "email": "test@email.org",
            "password": "<PASSWORD>",
            "confirm_password": "<PASSWORD>",
        }
        cls.instance = UserModel.objects.get(pk=1)  # username: "butime"

    def test_user_created(self):
        serializer = UserModelSerializer(data=self.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        qs = UserModel.objects.filter(email=self.data["email"])
        self.assertTrue(qs.exists())

    def test_create_password_hashing(self):
        serializer = UserModelSerializer(data=self.data)

        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        self.assertTrue(instance.check_password(self.data["password"]))

    def test_update_password_hashing(self):
        serializer = UserModelSerializer(self.instance, data=self.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.instance.refresh_from_db()
        self.assertTrue(self.instance.check_password(self.data["password"]))

    def test_username_validation(self):
        data = self.data.copy()
        data.update({"username": "butime"})
        serializer = UserModelSerializer(data=data)
        self.assertRaises(
            ValidationError, serializer.is_valid, raise_exception=True
        )
        self.assertIn("username", serializer.errors)

    def test_passwords_validation(self):
        data = self.data.copy()
        data.update({"confirm_password": "<ANOTHER_PASSWORD>"})
        serializer = UserModelSerializer(data=data)
        self.assertRaises(
            ValidationError, serializer.is_valid, raise_exception=True
        )
        self.assertIn("password", serializer.errors)
        self.assertIn("confirm_password", serializer.errors)

    def test_partial_update(self):
        # since validate method is modified, this behavior should be tested
        # to avoid errors
        data = {"first_name": "Wilcome", "last_name": "Brownlock"}
        serializer = UserModelSerializer(
            self.instance, data, partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.first_name, data["first_name"])
        self.assertEqual(self.instance.last_name, data["last_name"])

    def test_partial_password_update(self):
        data = {"password": "<NEW_PASSWORD>"}  # no confirm password provided
        serializer = UserModelSerializer(self.instance, data, partial=True)

        self.assertRaises(
            ValidationError, serializer.is_valid, raise_exception=True
        )
        self.assertIn("password", serializer.errors)
        self.assertIn("confirm_password", serializer.errors)
