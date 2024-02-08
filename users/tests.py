from http import HTTPStatus

from django import test

from users import views


class TestUserProfileView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = "/profile/"
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
        cls.url_path = "/sign-up/"
        cls.response_content = b"sign up"
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


class TestSignInView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = "/sign-out/"
        cls.response_content = b"sign in"
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


class TestSignOutView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = "/sign-out/"
        cls.response_content = b"sign out"
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
