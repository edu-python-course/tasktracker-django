"""
Users application admin site

"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    ordering = ("last_name", "first_name", "username")
