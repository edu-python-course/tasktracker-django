import uuid
from http import HTTPStatus

from django.contrib.auth import get_user_model
from rest_framework import test
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

from tasks.models import TaskModel

UserModel = get_user_model()
PK_EXISTS = uuid.UUID("1b79ca87-203a-4944-ada0-a6a8b9b154be")


class TestTasksResourceDetailAPIView(test.APITestCase):
    fixtures = ["users", "tokens", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("api:tasks:detail", args=(PK_EXISTS,))
        cls.obj = TaskModel.objects.get(pk=PK_EXISTS)
        cls.reporter = UserModel.objects.get(pk=2)
        cls.assignee = UserModel.objects.get(pk=3)
        cls.data = {
            "summary": "Test tasks resource detail API views"
        }

    def setUp(self) -> None:
        self.client = test.APIClient()
        self.user = UserModel.objects.create_user(
            username="another",
        )
        Token.objects.create(user=self.user)

    def test_assignee_restricted_to_delete(self):
        self.client.force_authenticate(token=self.assignee.auth_token)
        response = self.client.delete(self.url_path)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)

    def test_user_cannot_modify(self):
        self.client.force_authenticate(token=self.user.auth_token)
        response = self.client.put(self.url_path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
