"""
Users application API routes

"""

from django.urls import path

from users.resources import AuthTokenAPIView

app_name = "users"
urlpatterns = [
    path("auth-token/", AuthTokenAPIView.as_view(), name="auth-token"),
]
