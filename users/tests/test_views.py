from django import test
from django.urls import reverse


class TestUserProfileView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("users:profile")
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"user profile view")


class TestSignUpView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("users:sign-up")
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"auth sign up view")


class TestSignInView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("users:sign-in")
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"auth sign in view")


class TestSignOutView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = reverse("users:sign-out")
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"auth sign out view")
