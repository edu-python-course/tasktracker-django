import uuid
from http import HTTPStatus

from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

from tasks.models import TaskModel

PK_EXISTS = uuid.UUID("1b79ca87-203a-4944-ada0-a6a8b9b154be")
PK_NOT_EXISTS = uuid.uuid4()
UserModel = get_user_model()


class TestTaskUpdateView(test.TestCase):
    fixtures = ["users", "tasks"]
    url_path = None
    assignee = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:update", args=(PK_EXISTS,))
        cls.url_404 = reverse("tasks:update", args=(PK_NOT_EXISTS,))
        cls.url_sign_in = "".join(
            [reverse("users:sign-in"), "?next=", cls.url_path]
        )
        cls.template_name = "tasks/task_form.html"
        cls.user = UserModel.objects.get(username="wheed1997")
        cls.assignee = UserModel.objects.get(username="prombery87")
        cls.payload = {
            "summary": "Updated summary",
            "assignee": cls.assignee.pk,
        }
        cls.instance = TaskModel.objects.get(pk=PK_EXISTS)

    def setUp(self) -> None:
        self.client = test.Client()
        self.client.force_login(self.user)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_task_updated(self):
        self.client.post(self.url_path, self.payload)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.summary, self.payload["summary"])
        self.assertEqual(self.instance.assignee, self.assignee)

    def test_not_found(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_anonymous_redirected(self):
        self.client.logout()
        response = self.client.get(self.url_path)
        self.assertRedirects(response, self.url_sign_in)
