from http import HTTPStatus

from django.contrib.auth import get_user_model
from rest_framework import test
from rest_framework.reverse import reverse_lazy

from tasks.models import TaskModel

UserModel = get_user_model()


class TestTasksListAPI(test.APITestCase):
    fixtures = ["users", "tasks"]
    reporter: UserModel = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse_lazy("api:tasks-list")
        cls.reporter = UserModel.objects.get(pk=2)
        cls.data = {
            "summary": "Test tasks list API",
            "reporter": cls.reporter.pk,
        }

    def setUp(self) -> None:
        self.client = test.APIClient()

    def test_get(self):
        response = self.client.get(self.url_path)

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_post(self):
        response = self.client.post(self.url_path, self.data)

        qs = TaskModel.objects.filter(summary=self.data["summary"])
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(qs.exists())

    def test_bad_request(self):
        response = self.client.post(self.url_path, {})

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
