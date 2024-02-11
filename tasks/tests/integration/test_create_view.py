from http import HTTPStatus

from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

from tasks.models import TaskModel

UserModel = get_user_model()


class TestTaskCreateView(test.TestCase):
    fixtures = ["users"]
    url_path = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:create")
        cls.template_name = "tasks/task_form.html"
        cls.reporter = UserModel.objects.get(username="wheed1997")
        cls.admin = UserModel.objects.filter(is_superuser=True).first()
        cls.inactive = UserModel.objects.filter(is_active=False).first()
        cls.url_sign_in = "".join(
            [reverse("users:sign-in"), "?next=", cls.url_path]
        )
        cls.payload = {
            "summary": "New task summary"
        }

    def setUp(self) -> None:
        self.client = test.Client()
        self.client.force_login(self.reporter)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_task_created(self):
        self.client.post(self.url_path, self.payload)
        qs = TaskModel.objects.filter(summary=self.payload["summary"])
        self.assertTrue(qs.exists())

    def test_anonymous_redirected(self):
        self.client.logout()
        response = self.client.get(self.url_path)
        self.assertRedirects(response, self.url_sign_in)
        response = self.client.post(self.url_path, self.payload)
        self.assertRedirects(response, self.url_sign_in)

    def test_permission_denied(self):
        self.client.force_login(UserModel.objects.get(username="butime"))
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
