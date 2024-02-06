from django import test
from django.contrib.auth import get_user_model

from tasks.models import TaskModel
from tasks.serializers import TaskModelWriteSerializer


class TestTaskModelWriteSerializer(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.reporter = get_user_model().objects.get(pk=2)
        cls.assignee = get_user_model().objects.get(pk=3)

    def setUp(self) -> None:
        task = TaskModel.objects.create(
            summary="Test summary",
            description="Test description",
            reporter=self.reporter,
            assignee=self.assignee,
        )
        # because of RandomUUID usage, should be fetched from DB
        self.instance = TaskModel.objects.get(created_at=task.created_at)

    def test_update(self):
        # since update method has been modified, it should be tested
        serializer = TaskModelWriteSerializer(
            self.instance,
            {
                "summary": "Updated summary",
                "reporter": self.assignee.pk,
                "assignee": self.reporter.pk,
            },
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.instance.refresh_from_db()
        self.assertEqual(self.instance.reporter, self.reporter)
        self.assertEqual(self.instance.assignee, self.reporter)
        self.assertEqual(self.instance.summary, "Updated summary")
