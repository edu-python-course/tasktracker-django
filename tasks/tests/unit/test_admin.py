from django import test
from django.contrib.auth import get_user_model

from tasks.admin import TaskModelAdmin
from tasks.models import TaskModel

UserModel = get_user_model()


class TestTaskModelAdmin(test.TestCase):
    admin: UserModel = None
    reporter: UserModel = None
    assignee: UserModel = None

    @classmethod
    def setUpTestData(cls) -> None:
        cls.admin = UserModel(
            username="butime"
        )
        cls.assignee = UserModel(
            username="prombery87",
            first_name="Dora",
            last_name="Headstrong"
        )
        cls.reporter = UserModel(
            username="wheed1997",
            first_name="Pippin",
            last_name="Sackville-Baggins"
        )

    def setUp(self) -> None:
        self.task_admin = TaskModelAdmin(
            model=TaskModel, admin_site=None
        )

    def test_get_reporter_full_name(self):
        instance = TaskModel(reporter=self.reporter)
        value = self.task_admin.get_reporter(instance)
        self.assertEqual(value, self.reporter.get_full_name())

    def test_get_assignee_full_name(self):
        instance = TaskModel(assignee=self.assignee)
        value = self.task_admin.get_assignee(instance)
        self.assertEqual(value, self.assignee.get_full_name())

    def test_get_reporter_username(self):
        instance = TaskModel(reporter=self.admin)
        value = self.task_admin.get_reporter(instance)
        self.assertEqual(value, self.admin.username)

    def test_get_assignee_username(self):
        instance = TaskModel(assignee=self.admin)
        value = self.task_admin.get_assignee(instance)
        self.assertEqual(value, self.admin.username)

    def test_get_assignee_none(self):
        instance = TaskModel()
        value = self.task_admin.get_assignee(instance)
        self.assertIsNone(value)
