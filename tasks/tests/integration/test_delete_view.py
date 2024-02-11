import uuid
from http import HTTPStatus

from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

from tasks.models import TaskModel

PK_EXISTS = uuid.UUID("1b79ca87-203a-4944-ada0-a6a8b9b154be")
PK_NOT_EXISTS = uuid.uuid4()
UserModel = get_user_model()


class TestTaskDeleteView(test.TestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:delete", args=(PK_EXISTS,))
        cls.url_404 = reverse("tasks:delete", args=(PK_NOT_EXISTS,))
        cls.url_redirect = reverse("tasks:list")
        cls.user = UserModel.objects.get(username="wheed1997")
        # noinspection PyUnresolvedReferences
        cls.url_sign_in = "".join(
            [reverse("users:sign-in"), "?next=", cls.url_path]
        )

    def setUp(self) -> None:
        self.client = test.Client()
        self.client.force_login(self.user)

    def test_task_deleted(self):
        self.client.post(self.url_path)
        self.assertFalse(TaskModel.objects.filter(pk=PK_EXISTS).exists())

    def test_response_redirects(self):
        response = self.client.post(self.url_path)
        self.assertRedirects(response, self.url_redirect)

    def test_not_found(self):
        response = self.client.post(self.url_404)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_anonymous_redirected(self):
        self.client.logout()
        response = self.client.post(self.url_path)
        self.assertRedirects(response, self.url_sign_in)
