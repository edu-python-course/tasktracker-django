import uuid

from django import test
from django.contrib.auth import get_user
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
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "summary": "New task",
        }

    def setUp(self) -> None:
        self.url_path = reverse("tasks:create")
        self.template_name = "tasks/task_form.html"
        self.client = test.Client()
        self.client.login(username="wheed1997", password="enohR4cog")

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_anonymous_request(self):
        self.client.logout()
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 302)
        response = self.client.post(self.url_path, self.data)
        self.assertEqual(response.status_code, 302)

    def test_task_created(self):
        self.client.post(self.url_path, self.data)
        self.assertEqual(models.TaskModel.objects.count(), 1)

    def test_response_redirect(self):
        response = self.client.post(self.url_path, self.data)
        url = models.TaskModel.objects.first().get_absolute_url()
        self.assertRedirects(response, url)

    def test_task_reporter(self):
        self.client.post(self.url_path, self.data)
        instance = models.TaskModel.objects.first()
        self.assertEqual(instance.reporter, get_user(self.client))


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
