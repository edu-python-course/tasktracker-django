import uuid

from rest_framework import test
from rest_framework.reverse import reverse

from tasks.resources import TaskModelViewSet
from tasks.serializers import TaskModelReadSerializer, TaskModelWriteSerializer

PK_EXISTS = uuid.UUID("1b79ca87-203a-4944-ada0-a6a8b9b154be")
PK_NOT_EXISTS = uuid.uuid4()


class TestTaskModelViewSet(test.APITestCase):
    fixtures = ["users", "tasks"]

    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_list = reverse("api:tasks-list")
        cls.url_detail = reverse("api:tasks-detail", args=(PK_EXISTS,))
        cls.data = {
            "summary": "Test task model view set",
            "reporter": 2,
        }

    def setUp(self) -> None:
        self.factory = test.APIRequestFactory()
        self.viewset = TaskModelViewSet()

    def test_get_serializer_class_list(self):
        self.viewset.request = self.factory.get(self.url_list)
        serializer_class = self.viewset.get_serializer_class()
        self.assertIs(serializer_class, TaskModelReadSerializer)

    def test_get_serializer_class_create(self):
        self.viewset.request = self.factory.post(self.url_list, self.data)
        serializer_class = self.viewset.get_serializer_class()
        self.assertIs(serializer_class, TaskModelWriteSerializer)

    def test_get_serializer_class_retrieve(self):
        self.viewset.request = self.factory.get(self.url_detail)
        serializer_class = self.viewset.get_serializer_class()
        self.assertIs(serializer_class, TaskModelReadSerializer)

    def test_get_serializer_class_update(self):
        self.viewset.request = self.factory.put(self.url_detail, self.data)
        serializer_class = self.viewset.get_serializer_class()
        self.assertIs(serializer_class, TaskModelWriteSerializer)

    def test_get_serializer_class_partial_update(self):
        self.viewset.request = self.factory.patch(self.url_detail, self.data)
        serializer_class = self.viewset.get_serializer_class()
        self.assertIs(serializer_class, TaskModelWriteSerializer)
