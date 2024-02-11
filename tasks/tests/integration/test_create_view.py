from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

from tasks.models import TaskModel

UserModel = get_user_model()


class TestTaskCreateView(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:create")
        cls.template_name = "tasks/task_form.html"
        cls.user = UserModel.objects.get(username="wheed1997")
        # noinspection PyUnresolvedReferences
        cls.url_sign_in = "".join(
            [reverse("users:sign-in"), "?next=", cls.url_path]
        )
        cls.payload = {
            "summary": "New task summary"
        }

    def setUp(self) -> None:
        self.client = test.Client()
        self.client.force_login(self.user)

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