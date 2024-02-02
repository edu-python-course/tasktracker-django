import datetime
import unittest

from django.utils import timezone

from tasks.templatetags.tasks import is_within_days


class TestIsWithinDays(unittest.TestCase):
    def test_is_within_days(self):
        date = timezone.now() - datetime.timedelta(days=3)
        self.assertTrue(is_within_days(date, 5))
        self.assertFalse(is_within_days(date, 2))
