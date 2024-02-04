from django import test
from django.urls import reverse

ADMINISTRATION = "Administration"
CREATE_NEW = "Create new"
PROFILE = "Profile"
SIGN_UP = "Sign Up"
SIGN_IN = "Sign In"
SIGN_OUT = "Sign Out"


class TestNavbarRender(test.TestCase):
    fixtures = ["users"]

    def setUp(self) -> None:
        self.url_path = reverse("tasks:list")
        self.client = test.Client()

    def test_superuser(self):
        self.client.login(username="butime", password="Zeiriev1oo")
        response = self.client.get(self.url_path)
        self.assertContains(response, ADMINISTRATION)
        self.assertContains(response, PROFILE)
        self.assertContains(response, SIGN_OUT)
        self.assertNotContains(response, CREATE_NEW)
        self.assertNotContains(response, SIGN_UP)
        self.assertNotContains(response, SIGN_IN)

    def test_authenticated(self):
        self.client.login(username="prombery87", password="ieZeiSh5k")
        response = self.client.get(self.url_path)
        self.assertContains(response, CREATE_NEW)
        self.assertContains(response, PROFILE)
        self.assertContains(response, SIGN_OUT)
        self.assertNotContains(response, ADMINISTRATION)
        self.assertNotContains(response, SIGN_UP)
        self.assertNotContains(response, SIGN_IN)

    def test_anonymous(self):
        response = self.client.get(self.url_path)
        self.assertContains(response, SIGN_UP)
        self.assertContains(response, SIGN_IN)
        self.assertNotContains(response, ADMINISTRATION)
        self.assertNotContains(response, CREATE_NEW)
        self.assertNotContains(response, PROFILE)
        self.assertNotContains(response, SIGN_OUT)
