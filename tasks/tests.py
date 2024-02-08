from http import HTTPStatus

from django import test
from django.urls import reverse
from tasks import views


class TestTaskListView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("list")
        cls.response_content = b"task list"
        cls.view = views.task_list_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.content, self.response_content)


class TestTaskDetailView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.pk = 42
        cls.url_path = reverse("detail", kwargs={"pk": cls.pk})
        cls.response_content = b"task detail"
        cls.view = views.task_detail_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, 42)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, 42)
        self.assertEqual(response.content, self.response_content)


class TestTaskCreateView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("create")
        cls.response_content = b"task create"
        cls.view = views.task_create_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.content, self.response_content)


class TestTaskUpdateView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.pk = 42
        cls.url_path = reverse("update", kwargs={"pk": cls.pk})
        cls.response_content = b"task update"
        cls.view = views.task_update_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, self.pk)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, self.pk)
        self.assertEqual(response.content, self.response_content)


class TestTaskDeleteView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.pk = 42
        cls.url_path = reverse("delete", kwargs={"pk": cls.pk})
        cls.response_content = b"task delete"
        cls.view = views.task_delete_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, self.pk)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request, self.pk)
        self.assertEqual(response.content, self.response_content)
