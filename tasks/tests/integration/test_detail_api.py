from http import HTTPStatus

from django.contrib.auth import get_user_model
from rest_framework import test
from rest_framework.reverse import reverse_lazy

from tasks.models import TaskModel

UserModel = get_user_model()


class TestTasksListAPI(test.APITestCase):
    fixtures = ["users"]
    reporter: UserModel = None
    assignee: UserModel = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.reporter = UserModel.objects.get(pk=2)
        cls.assignee = UserModel.objects.get(pk=3)
        cls.data = {
            "summary": "Test tasks list API",
            "reporter": cls.reporter.pk,
        }

    def setUp(self) -> None:
        self.client = test.APIClient()
        self.instance = TaskModel.objects.create(
            summary="Existing task",
            reporter=self.reporter,
        )
        self.url_path = reverse_lazy(
            "api:tasks-detail",
            args=(self.instance.pk,)
        )
        self.url_404 = reverse_lazy(
            "api:tasks-detail",
            args=("dc9dcb0a-e20b-404e-a4e6-9627f7bc118d",)
        )

    def test_get(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_put(self):
        response = self.client.put(self.url_path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.ACCEPTED)

    def test_patch(self):
        response = self.client.patch(self.url_path, {"completed": False})
        self.assertEqual(response.status_code, HTTPStatus.ACCEPTED)

    def test_delete(self):
        response = self.client.delete(self.url_path)
        self.assertEqual(response.status_code, HTTPStatus.NO_CONTENT)

    def test_not_found(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_bad_request(self):
        response = self.client.put(self.url_path, {})
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
