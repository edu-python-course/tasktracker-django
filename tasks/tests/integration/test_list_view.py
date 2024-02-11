from django import test
from django.urls import reverse


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
