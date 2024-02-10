from django import test

from users.models import UserModel


class TestUserModel(test.TestCase):
    def test_stringify_full_name(self):
        instance = UserModel(first_name="Wilcome", last_name="Brownlock")
        self.assertEqual(str(instance), "Wilcome Brownlock")

    def test_stringify_username(self):
        instance = UserModel(username="butime")
        self.assertEqual(str(instance), "butime")
