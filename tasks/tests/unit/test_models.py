from django import test

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
