from django import test
from django.urls import reverse


class TestTaskListView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:list")
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"task list view")


class TestTaskCreateView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:create")
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"task create view")


class TestTaskDetailView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:detail", args=(42,))
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertRegex(response.content, rb"task detail view: \d+")


class TestTaskUpdateView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:update", args=(42,))
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertRegex(response.content, rb"task update view: \d+")


class TestTaskDeleteView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:delete", args=(42,))
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertRegex(response.content, rb"task delete view: \d+")
