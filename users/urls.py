"""
Users application URL configuration

"""

from django.urls import path

from users import views

app_name = "users"
urlpatterns = [
    path("sign-up/", views.sign_up_view, name="sign-up"),
    path("sign-in/", views.sign_in_view, name="sign-in"),
    path("sign-out/", views.sign_out_view, name="sign-out"),
    path("profile/", views.user_profile_view, name="profile"),
]
