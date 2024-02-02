"""
Test project views

"""

from django import test


class TestUserProfileView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/profile/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"user profile view")


class TestSignUpView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/sign-up/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"auth sign up view")


class TestSignInView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/sign-in/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"auth sign in view")


class TestSignOutView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/sign-out/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"auth sign out view")


class TestTaskListView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"task list view")


class TestTaskCreateView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/create/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.content, b"task create view")


class TestTaskDetailView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/42/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertRegex(response.content, rb"task detail view: \d+")


class TestTaskUpdateView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/42/update/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertRegex(response.content, rb"task update view: \d+")


class TestTaskDeleteView(test.TestCase):
    def setUp(self) -> None:
        self.url_path = "/42/delete/"
        self.client = test.Client()

    def test_response_200(self):
        response = self.client.get(self.url_path)
        self.assertEqual(response.status_code, 200)

    def test_response(self):
        response = self.client.get(self.url_path)
        self.assertRegex(response.content, rb"task delete view: \d+")
