from django.contrib.auth import get_user_model
from rest_framework import test
from rest_framework.exceptions import PermissionDenied

from tasks.models import TaskModel
from tasks.serializers import TaskModelReadSerializer, TaskModelWriteSerializer

UserModel = get_user_model()


class TestTaskModelReadSerializer(test.APITestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.data = {
            "summary": "Test task summary",
            "assignee": UserModel.objects.get(pk=2),
            "reporter": UserModel.objects.get(pk=3),
        }
        cls.serializer = TaskModelReadSerializer

    def test_create_raises_exception(self):
        serializer = self.serializer(data=self.data)
        self.assertRaises(PermissionDenied, serializer.create, self.data)

    def test_update_raises_exception(self):
        instance = TaskModel.objects.first()
        serializer = self.serializer(instance, data=self.data)
        self.assertRaises(
            PermissionDenied, serializer.update, instance, self.data
        )


class TestTaskModelWriteSerializer(test.APITestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.admin = UserModel.objects.get(pk=1)
        cls.assignee = UserModel.objects.get(pk=2)
        cls.reporter = UserModel.objects.get(pk=3)
        cls.inactive = UserModel.objects.get(pk=4)
        cls.serializer = TaskModelWriteSerializer

    def test_task_creation(self):
        serializer = self.serializer(data={
            "summary": "Test task write serializer",
            "reporter": self.reporter.pk,
        })
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        qs = TaskModel.objects.filter(pk=instance.pk)
        self.assertTrue(qs.exists())

    def test_status_update(self):
        # required to handle AJAX requests from HTMX front-end: GH-73, GH-74
        instance = TaskModel.objects.create(
            summary="Test partial update for completed status",
            reporter=self.reporter,
            assignee=self.assignee,
            completed=False,
        )

        serializer = self.serializer(
            instance, {"completed": True}, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertTrue(instance.completed)

        serializer = self.serializer(
            instance, {"completed": False}, partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertFalse(instance.completed)

    def test_assignee_validation_admin(self):
        payload = {
            "summary": "Admin assignee",
            "reporter": self.reporter.pk,
            "assignee": self.admin.pk,
        }
        serializer = self.serializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn("assignee", serializer.errors)

    def test_assignee_validation_inactive(self):
        payload = {
            "summary": "Inactive assignee",
            "reporter": self.reporter.pk,
            "assignee": self.inactive.pk,
        }
        serializer = self.serializer(data=payload)
        self.assertFalse(serializer.is_valid())
        self.assertIn("assignee", serializer.errors)

    def test_assignee_validation(self):
        instance = TaskModel.objects.create(
            summary="Test task write serializer",
            reporter=self.reporter,
        )
        serializer = self.serializer(instance, {
            "summary": "Update assignee",
            "reporter": self.reporter.pk,
            "assignee": self.assignee.pk,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.assertTrue(instance.assignee, self.assignee)

    def test_reporter_not_updated(self):
        instance = TaskModel.objects.create(
            summary="Test reporter update",
            reporter=self.reporter,
        )
        serializer = self.serializer(instance, data={
            "summary": "Updated summary",
            "reporter": self.assignee.pk,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(instance.summary, "Updated summary")
        self.assertEqual(instance.reporter, self.reporter)
