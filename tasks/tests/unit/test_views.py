from http import HTTPStatus

from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

from tasks import models, views


class TestTaskListView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:list")
        cls.view = views.task_list_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestTaskDetailView(test.TestCase):
    pk = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.view = views.task_detail_view
        cls.request_factory = test.RequestFactory()
        cls.reporter = get_user_model().objects.create(
            username="test_detail", email="test_detail@email.org"
        )

    def setUp(self) -> None:
        self.instance = models.TaskModel.objects.create(
            summary="Bung holes wave from beauties like small sons.",
            reporter=self.reporter
        )

    def test_response_200(self):
        request = self.request_factory.get(self.instance.get_absolute_url())
        response = self.view(request, self.instance.pk)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestTaskCreateView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:create")
        cls.view = views.task_create_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestTaskUpdateView(test.TestCase):
    pk = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.view = views.task_update_view
        cls.request_factory = test.RequestFactory()
        cls.reporter = get_user_model().objects.create(
            username="test_update", email="test_update@email.org"
        )

    def setUp(self) -> None:
        self.instance = models.TaskModel.objects.create(
            summary="Where is the cloudy tribble?",
            reporter=get_user_model().objects.create(username="update_test")
        )

    def test_response_200(self):
        request = self.request_factory.get(self.instance.get_absolute_url())
        response = self.view(request, self.instance.pk)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestTaskDeleteView(test.TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.view = views.task_delete_view
        cls.request_factory = test.RequestFactory()
        cls.reporter = get_user_model().objects.create(
            username="test_delete", email="test_delete@email.org"
        )

    def setUp(self) -> None:
        self.instance = models.TaskModel.objects.create(
            summary="The landlubber endures with grace, hail the reef.",
            reporter=self.reporter
        )

    def test_response_301(self):
        request = self.request_factory.get(self.instance.get_absolute_url())
        response = self.view(request, self.instance.pk)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
