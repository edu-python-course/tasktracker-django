import uuid
from http import HTTPStatus

from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

from tasks.models import TaskModel

PK_EXISTS = uuid.UUID("1b79ca87-203a-4944-ada0-a6a8b9b154be")
PK_NOT_EXISTS = uuid.uuid4()
UserModel = get_user_model()


class TestTaskDetailView(test.TestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:detail", args=(PK_EXISTS,))
        cls.url_404 = reverse("tasks:detail", args=(PK_NOT_EXISTS,))
        cls.template_name = "tasks/task_detail.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_not_found(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_response_context(self):
        response = self.client.get(self.url_path)
        self.assertIn("object", response.context)
        self.assertIsInstance(response.context["object"], TaskModel)
        self.assertEqual(response.context["object"].pk, PK_EXISTS)
