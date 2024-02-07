"""
Users application API routes

"""

from django.urls import path

from users import resources

urlpatterns = [
    path("users/", resources.users_resource),
]
