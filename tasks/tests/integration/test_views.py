from django import test
from django.urls import reverse


class TestTaskListView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:list")
        cls.template_name = "task_list.html"

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
        cls.url_path = reverse("tasks:detail", kwargs={"pk": cls.pk})
        cls.template_name = "task_detail.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestTaskCreateView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("tasks:create")
        cls.template_name = "task_form.html"

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
        cls.url_path = reverse("tasks:update", kwargs={"pk": cls.pk})
        cls.template_name = "task_form.html"

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)


class TestTaskDeleteView(test.TestCase):
    pk = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.pk = 42
        cls.url_path = reverse("tasks:delete", kwargs={"pk": cls.pk})
        cls.url_redirect = reverse("tasks:list")

    def setUp(self) -> None:
        self.client = test.Client()

    def test_response_redirects(self):
        response = self.client.get(self.url_path)
        self.assertRedirects(response, self.url_redirect)
