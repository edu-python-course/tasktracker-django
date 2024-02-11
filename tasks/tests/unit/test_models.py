import uuid

from django import test
from django.urls import reverse

from tasks.models import TaskModel


class TestTaskModel(test.TestCase):
    def test_stringify(self):
        summary = "Damn yer girl, feed the skull."
        instance = TaskModel(summary=summary)
        self.assertEqual(str(instance), summary)

    def test_title_property(self):
        summary = "Arrr, madness!"
        instance = TaskModel(summary=summary)
        self.assertEqual(str(instance), instance.title)

    def test_get_url(self):
        pk = uuid.uuid4()
        instance = TaskModel(pk=pk)
        expected = reverse("tasks:detail", args=(pk,))
        self.assertEqual(instance.get_absolute_url(), expected)
