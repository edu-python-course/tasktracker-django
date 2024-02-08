from http import HTTPStatus

from django import test
from django.urls import reverse
from users import views


class TestUserProfileView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("profile")
        cls.response_content = b"user profile"
        cls.view = views.user_profile_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.content, self.response_content)


class TestSignUpView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("sign-up")
        cls.response_content = b"sign up"
        cls.view = views.sign_up_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.content, self.response_content)


class TestSignInView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("sign-in")
        cls.response_content = b"sign in"
        cls.view = views.sign_in_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.content, self.response_content)


class TestSignOutView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("sign-out")
        cls.response_content = b"sign out"
        cls.view = views.sign_out_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_content(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.content, self.response_content)
