from http import HTTPStatus

from django import test
from django.urls import reverse

PK_EXISTS = 42
PK_NOT_EXISTS = 24


class TestTaskListView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:list")
        cls.template_name = "tasks/task_list.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestTaskDetailView(test.TestCase):
    pk = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.pk = 42
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


class TestTaskCreateView(test.TestCase):
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
    pk = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.pk = 42
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
    pk = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.pk = 42
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
