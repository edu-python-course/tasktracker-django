from django.contrib.auth import get_user_model
from rest_framework import test

from users.serializers import UserSerializer

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

    def test_user_creation(self):
        serializer = UserSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)

        username = self.data["username"]
        self.assertTrue(UserModel.objects.filter(username=username).exists())
