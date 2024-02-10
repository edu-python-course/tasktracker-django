from http import HTTPStatus

from django import test
from django.urls import reverse

from tasks import views


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
        cls.pk = 42
        cls.url_path = reverse("tasks:detail", kwargs={"pk": cls.pk})
        cls.view = views.task_detail_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, 42)
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
        cls.pk = 42
        cls.url_path = reverse("tasks:update", kwargs={"pk": cls.pk})
        cls.view = views.task_update_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, self.pk)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestTaskDeleteView(test.TestCase):
    pk = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.pk = 42
        cls.url_path = reverse("tasks:delete", kwargs={"pk": cls.pk})
        cls.view = views.task_delete_view
        cls.request_factory = test.RequestFactory()

    def test_response_301(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, self.pk)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
