from django import test
from django.contrib.auth import get_user_model

from users import serializers

UserModel = get_user_model()


class TestUserSerializer(test.TestCase):
    @classmethod
    def setUp(cls):
        cls.data = {
            "username": "test",
            "email": "test@email.org",
            "password": "<PASSWORD>",
        }
        cls.updated_data = {
            "username": "updated",
            "email": "updated@email.org",
            "password": "<UPDATED_PASSWORD>",
        }

    def test_user_create(self):
        serializer = serializers.UserSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)

        self.assertEqual(UserModel.objects.count(), 1)

    def test_user_update(self):
        instance = UserModel.objects.create_user(**self.data)
        serializer = serializers.UserSerializer(instance, self.updated_data)
        serializer.is_valid(raise_exception=True)
        serializer.update(instance, serializer.validated_data)

        instance.refresh_from_db()
        self.assertEqual(instance.username, self.updated_data["username"])
        self.assertEqual(instance.email, self.updated_data["email"])
        self.assertTrue(instance.check_password(self.updated_data["password"]))

    def test_user_retrieve(self):
        instance = UserModel.objects.create_user(**self.data)
        expected = self.data.copy()
        del expected["password"]
        expected.update({"pk": instance.pk})

        serializer = serializers.UserSerializer(instance)
        self.assertDictEqual(serializer.data, expected)
