from django import test

from tasks import models


class TestTaskModel(test.TestCase):
    def test_cast_to_string(self):
        instance = models.TaskModel(summary="The captain pulls with urchin")
        self.assertEqual(str(instance), "The captain pulls with urchin")
