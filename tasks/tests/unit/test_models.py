import uuid

from django import test
from django.contrib.auth import get_user_model
from django.urls import reverse

from tasks.models import TaskModel

UserModel = get_user_model()


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


class TestTaskModelPermissions(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.assignee = UserModel(username="assignee")
        cls.reporter = UserModel(username="reporter")
        cls.non_user = UserModel(username="none")

    def setUp(self) -> None:
        self.instance = TaskModel(reporter=self.reporter,
                                  assignee=self.assignee)

    def test_can_edit(self):
        self.assertTrue(self.instance.can_update(self.reporter))
        self.assertTrue(self.instance.can_update(self.assignee))
        self.assertFalse(self.instance.can_update(self.non_user))

    def test_can_delete(self):
        self.assertTrue(self.instance.can_delete(self.reporter))
        self.assertFalse(self.instance.can_delete(self.assignee))
        self.assertFalse(self.instance.can_delete(self.non_user))
