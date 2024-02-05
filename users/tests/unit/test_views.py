from django import test
from django.contrib.auth import get_user, get_user_model
from django.urls import reverse

UserModel = get_user_model()
PROFILE_PATH_NAME = "users:profile"
SIGN_UP_PATH_NAME = "users:sign-up"
SIGN_IN_PATH_NAME = "users:sign-in"
SIGN_OUT_PATH_NAME = "users:sign-out"


class TestUserProfileView(test.TestCase):
    fixtures = ["users"]

    def setUp(self) -> None:
        self.url_path = reverse(PROFILE_PATH_NAME)
        self.template_name = "users/profile.html"
        self.client = test.Client()
        self.client.login(username="butime", password="Zeiriev1oo")

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_anonymous_user_redirected(self):
        self.client.logout()
        response = self.client.get(self.url_path)
        url = "".join([
            reverse(SIGN_IN_PATH_NAME),
            "?next=",
            reverse(PROFILE_PATH_NAME)
        ])
        self.assertRedirects(response, url)

    def test_user_updated(self):
        self.client.post(self.url_path, {
            "first_name": "John",
            "last_name": "Doe"
        })
        self.assertTrue(UserModel.objects.filter(
            first_name="John", last_name="Doe"
        ).exists())


class TestSignUpView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.data = {
            "username": "test",
            "email": "test@email.com",
            "password": "<PASSWORD>",
            "confirm_password": "<PASSWORD>",
        }

    def setUp(self) -> None:
        self.url_path = reverse(SIGN_UP_PATH_NAME)
        self.template_name = "auth/signup.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_restricted_methods(self):
        self.assertEqual(self.client.put(self.url_path).status_code, 405)
        self.assertEqual(self.client.patch(self.url_path).status_code, 405)
        self.assertEqual(self.client.delete(self.url_path).status_code, 405)

    def test_response_redirect(self):
        response = self.client.post(self.url_path, self.data)
        self.assertRedirects(response, reverse(SIGN_IN_PATH_NAME))

    def test_user_is_signed_up(self):
        self.client.post(self.url_path, self.data)
        self.assertTrue(
            UserModel.objects.filter(username=self.data["username"]).exists()
        )


class TestSignInView(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.data = {
            "username": "wheed1997",
            "password": "enohR4cog",
        }

    def setUp(self) -> None:
        self.url_path = reverse(SIGN_IN_PATH_NAME)
        self.template_name = "auth/signin.html"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_restricted_methods(self):
        self.assertEqual(self.client.put(self.url_path).status_code, 405)
        self.assertEqual(self.client.patch(self.url_path).status_code, 405)
        self.assertEqual(self.client.delete(self.url_path).status_code, 405)

    def test_response_redirect(self):
        response = self.client.post(self.url_path, self.data)
        self.assertRedirects(response, reverse(PROFILE_PATH_NAME))

    def test_user_is_signed_in(self):
        self.client.post(self.url_path, self.data)
        self.assertTrue(get_user(self.client).is_authenticated)


class TestSignOutView(test.TestCase):
    fixtures = ["users"]

    def setUp(self) -> None:
        self.url_path = reverse(SIGN_OUT_PATH_NAME)
        self.client = test.Client()

    def test_redirect(self):
        response = self.client.get(self.url_path)
        self.assertRedirects(response, reverse("tasks:list"))

    def test_user_is_signed_out(self):
        self.client.force_login(UserModel.objects.get(username="butime"))
        self.client.get(self.url_path)
        self.assertFalse(get_user(self.client).is_authenticated)
