from django import test
from django.urls import reverse


class TestTaskListView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:list")
        self.template_name = "tasks/task_list.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestTaskCreateView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:create")
        self.template_name = "tasks/task_form.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestTaskDetailView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:detail", args=(2,))
        self.url_404 = reverse("tasks:detail", args=(42,))
        self.template_name = "tasks/task_detail.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response_404(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, 404)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestTaskUpdateView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:update", args=(2,))
        self.url_404 = reverse("tasks:update", args=(42,))
        self.template_name = "tasks/task_form.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response_404(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, 404)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestTaskDeleteView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("tasks:delete", args=(2,))
        self.url_404 = reverse("tasks:delete", args=(42,))
        self.client = test.Client()

    def test_response_404(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, 404)

    def test_redirect(self):
        response = self.client.get(self.url_path)
        self.assertRedirects(response, reverse("tasks:list"))
