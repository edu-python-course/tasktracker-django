from http import HTTPStatus

from django import test
from django.urls import reverse

from users import views


class TestUserProfileView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:profile")
        cls.view = views.user_profile_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestSignUpView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-up")
        cls.view = views.sign_up_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_response_405(self):
        # put method not allowed
        request = self.request_factory.put(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

        # patch method not allowed
        request = self.request_factory.patch(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)

        # delete method not allowed
        request = self.request_factory.delete(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)


class TestSignInView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-in")
        cls.view = views.sign_in_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class TestSignOutView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-out")
        cls.view = views.sign_out_view
        cls.request_factory = test.RequestFactory()

    def test_response_200(self):
        request = self.request_factory.get(self.url_path)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
