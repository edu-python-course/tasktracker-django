"""
Tasks application mixins

"""

from django.contrib.auth.mixins import UserPassesTestMixin


class IsNotAdminMixin(UserPassesTestMixin):
    def test_func(self):
        # noinspection PyUnresolvedReferences
        return not self.request.user.is_superuser
