from django import test
from django.contrib.auth import get_user, get_user_model
from django.urls import reverse

UserModel = get_user_model()


class TestUserProfileView(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:profile")
        cls.template_name = "users/profile.html"
        # noinspection PyUnresolvedReferences
        cls.url_sign_in = "".join(
            [reverse("users:sign-in"), "?next=", cls.url_path]
        )

    def setUp(self) -> None:
        self.client = test.Client()
        self.user = UserModel.objects.get(username="wheed1997")
        self.client.force_login(self.user)

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_anonymous_redirected(self):
        self.client.logout()
        response = self.client.get(self.url_path)
        self.assertRedirects(response, self.url_sign_in)


class TestSignUpView(test.TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-up")
        cls.template_name = "auth/signup.html"
        cls.payload = {
            "username": "butime",
            "email": "butime@example.com",
            "password": "Zeiriev1oo",
            "confirm_password": "Zeiriev1oo",
        }

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_user_creation(self):
        self.client.post(self.url_path, data=self.payload)
        qs = UserModel.objects.filter(email=self.payload["email"])
        self.assertTrue(qs.exists())


class TestSignInView(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-in")
        cls.template_name = "auth/signin.html"
        cls.payload = {
            "username": "wheed1997",
            "password": "enohR4cog",
        }

    def setUp(self) -> None:
        self.client = test.Client()

    def test_template_used(self):
        response = self.client.get(self.url_path)
        self.assertTemplateUsed(response, self.template_name)

    def test_user_authenticated(self):
        self.client.post(self.url_path, self.payload)
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_response_redirects(self):
        response = self.client.post(self.url_path, self.payload)
        self.assertRedirects(response, reverse("users:profile"))


class TestSignOutView(test.TestCase):
    fixtures = ["users"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_path = reverse("users:sign-out")
        cls.url_redirect = reverse("tasks:list")

    def setUp(self) -> None:
        self.client = test.Client()

    def test_user_signed_out(self):
        self.client.force_login(UserModel.objects.get(username="butime"))
        self.client.post(self.url_path)
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_redirects(self):
        response = self.client.post(self.url_path)
        self.assertRedirects(response, self.url_redirect)
