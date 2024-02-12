from django.contrib.auth import get_user_model
from rest_framework import test
from rest_framework.exceptions import PermissionDenied

from tasks.models import TaskModel
from tasks.serializers import TaskModelReadSerializer

UserModel = get_user_model()


class TestTaskModelReadSerializer(test.APITestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.data = {
            "summary": "Test task summary",
            "assignee": UserModel.objects.get(pk=2),
            "reporter": UserModel.objects.get(pk=3),
        }
        cls.serializer = TaskModelReadSerializer

    def test_create_raises_exception(self):
        serializer = self.serializer(data=self.data)
        self.assertRaises(PermissionDenied, serializer.create, self.data)

    def test_update_raises_exception(self):
        instance = TaskModel.objects.first()
        serializer = self.serializer(instance, data=self.data)
        self.assertRaises(
            PermissionDenied, serializer.update, instance, self.data
        )
