import uuid
from http import HTTPStatus

from django import test
from django.urls import reverse

from tasks.models import TaskModel

PK_EXISTS = uuid.UUID("1b79ca87-203a-4944-ada0-a6a8b9b154be")
PK_NOT_EXISTS = uuid.uuid4()


class TestTaskListView(test.TestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:list")
        cls.template_name = "tasks/task_list.html"
        cls.total = 48

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_response_context(self):
        response = self.client.get(self.url_path)
        self.assertIn("object_list", response.context)
        self.assertEqual(len(response.context["object_list"]), self.total)


class TestTaskDetailView(test.TestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:detail", args=(PK_EXISTS,))
        cls.url_404 = reverse("tasks:detail", args=(PK_NOT_EXISTS,))
        cls.template_name = "tasks/task_detail.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_not_found(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_response_context(self):
        response = self.client.get(self.url_path)
        self.assertIn("object", response.context)
        self.assertIsInstance(response.context["object"], TaskModel)
        self.assertEqual(response.context["object"].pk, PK_EXISTS)


class TestTaskCreateView(test.TestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:create")
        cls.template_name = "tasks/task_form.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestTaskUpdateView(test.TestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:update", args=(PK_EXISTS,))
        cls.url_404 = reverse("tasks:update", args=(PK_NOT_EXISTS,))
        cls.template_name = "tasks/task_form.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_not_found(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)


class TestTaskDeleteView(test.TestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:delete", args=(PK_EXISTS,))
        cls.url_404 = reverse("tasks:delete", args=(PK_NOT_EXISTS,))
        cls.url_redirect = reverse("tasks:list")

    def setUp(self) -> None:
        self.client = test.Client()

    def test_response_redirects(self):
        response = self.client.get(self.url_path)
        self.assertRedirects(response, self.url_redirect)

    def test_not_found(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
