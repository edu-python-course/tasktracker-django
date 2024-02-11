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
    fixtures = ["users"]
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
        cls.reporter = UserModel.objects.get(username="wheed1997")
        cls.assignee = UserModel.objects.get(username="prombery87")
        cls.inactive = UserModel.objects.filter(is_active=False).first()
        cls.admin = UserModel.objects.filter(is_superuser=True).first()
        cls.payload = {
            "summary": "Updated summary",
            "assignee": cls.assignee.pk,
        }

    def setUp(self) -> None:
        self.client = test.Client()
        self.client.force_login(self.reporter)
        self.instance = TaskModel.objects.create(
            uuid=PK_EXISTS,
            summary="Test task",
            reporter=self.reporter,
        )

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_task_updated_by_reporter(self):
        self.client.post(self.url_path, self.payload)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.summary, self.payload["summary"])
        self.assertEqual(self.instance.assignee, self.assignee)

    def test_task_updated_by_assignee(self):
        self.instance.assignee = self.assignee
        self.instance.save()
        self.client.force_login(self.assignee)
        self.client.post(self.url_path, self.payload)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.summary, self.payload["summary"])

    def test_not_found(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_anonymous_redirected(self):
        self.client.logout()
        response = self.client.get(self.url_path)
        self.assertRedirects(response, self.url_sign_in)

    def test_permission_denied(self):
        # test authenticated user
        self.client.force_login(self.assignee)
        response = self.client.post(self.url_path, self.payload)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)
        # test superuser
        self.client.force_login(self.admin)
        response = self.client.post(self.url_path, self.payload)
        self.assertEqual(response.status_code, HTTPStatus.FORBIDDEN)

    def test_admin_assignee(self):
        payload = self.payload.copy()
        payload["assignee"] = self.admin.pk
        response = self.client.post(self.url_path, payload)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_inactive_assignee(self):
        payload = self.payload.copy()
        payload["assignee"] = self.inactive.pk
        response = self.client.post(self.url_path, payload)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
