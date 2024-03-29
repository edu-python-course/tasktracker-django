"""
Users application URL configuration

"""

from django.urls import path

from users import views

app_name = "users"
urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name="sign-up"),
    path("sign-in/", views.SignInView.as_view(), name="sign-in"),
    path("sign-out/", views.SignOutView.as_view(), name="sign-out"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
]
