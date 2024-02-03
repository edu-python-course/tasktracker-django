import uuid

from django import test
from django.urls import reverse

from tasks import models


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
    fixtures = ["users", "tasks"]

    def setUp(self) -> None:
        instance_uuid = models.TaskModel.objects.first().uuid
        self.url_path = reverse("tasks:detail", args=(instance_uuid,))
        self.url_404 = reverse("tasks:detail", args=(uuid.uuid4(),))
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
    fixtures = ["users", "tasks"]

    def setUp(self) -> None:
        instance_uuid = models.TaskModel.objects.first().uuid
        self.url_path = reverse("tasks:update", args=(instance_uuid,))
        self.url_404 = reverse("tasks:update", args=(uuid.uuid4(),))
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
    fixtures = ["users", "tasks"]

    def setUp(self) -> None:
        instance_uuid = models.TaskModel.objects.first().uuid
        self.url_path = reverse("tasks:delete", args=(instance_uuid,))
        self.url_404 = reverse("tasks:delete", args=(uuid.uuid4(),))
        self.client = test.Client()

    def test_response_404(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, 404)

    def test_redirect(self):
        response = self.client.get(self.url_path)
        self.assertRedirects(response, reverse("tasks:list"))
