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
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls):
        cls.data = {
            "summary": "Updated summary",
        }

    def setUp(self) -> None:
        self.client = test.Client()
        self.client.login(username="prombery87", password="ieZeiSh5k")
        models.TaskModel.objects.create(
            summary="Testing", reporter=get_user(self.client)
        )
        self.instance = models.TaskModel.objects.first()
        self.url_path = reverse("tasks:update", args=(self.instance.pk,))
        self.url_404 = reverse("tasks:update", args=(uuid.uuid4(),))
        self.template_name = "tasks/task_form.html"

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response_404(self):
        response = self.client.get(self.url_404)
        self.assertEqual(response.status_code, 404)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_anonymous_request(self):
        self.client.logout()
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 302)
        response = self.client.post(self.url_path, self.data)
        self.assertEqual(response.status_code, 302)

    def test_permission_denied(self):
        self.client.login(username="wheed1997", password="enohR4cog")
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 403)
        response = self.client.post(self.url_path, self.data)
        self.assertEqual(response.status_code, 403)

    def test_task_updated(self):
        self.client.post(self.url_path, self.data)
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.summary, self.data["summary"])

    def test_response_redirect(self):
        response = self.client.post(self.url_path, self.data)
        self.assertRedirects(response, self.instance.get_absolute_url())

    def test_assignee_can_edit(self):
        self.client.login(username="wheed1997", password="enohR4cog")
        self.instance.assignee = get_user(self.client)
        self.instance.save()
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)


class TestTaskDeleteView(test.TestCase):
    fixtures = ["users"]

    def setUp(self) -> None:
        self.client = test.Client()
        self.client.login(username="prombery87", password="ieZeiSh5k")
        models.TaskModel.objects.create(
            summary="Testing", reporter=get_user(self.client)
        )
        self.instance = models.TaskModel.objects.first()
        self.url_path = reverse("tasks:delete", args=(self.instance.pk,))
        self.url_404 = reverse("tasks:delete", args=(uuid.uuid4(),))

    def test_response_404(self):
        response = self.client.post(self.url_404)
        self.assertEqual(response.status_code, 404)

    def test_task_deleted(self):
        self.client.post(self.url_path)
        qs = models.TaskModel.objects.filter(pk=self.instance.pk)
        self.assertFalse(qs.exists())

    def test_response_redirect(self):
        response = self.client.post(self.url_path)
        self.assertRedirects(response, reverse("tasks:list"))

    def test_permission_denied(self):
        self.client.logout()
        response = self.client.post(self.url_path)
        self.assertEqual(response.status_code, 403)
        self.client.login(username="wheed1997", password="enohR4cog")
        response = self.client.post(self.url_path)
        self.assertEqual(response.status_code, 403)
