"""
Users application admin site

"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import UserModel

admin.site.register(UserModel, UserAdmin)
