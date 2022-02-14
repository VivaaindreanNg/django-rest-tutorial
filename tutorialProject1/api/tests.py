# Create your tests here.
from api.models import Task
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase


class TestView(APITestCase):
    def setUp(self) -> None:
        self.task1 = mommy.make(Task, title="test1", completed=False)
        self.task2 = mommy.make(Task, title="test2", completed=True)
        self.list_all_url = "/api/task-list/"

    def test_list_view(self) -> None:
        response = self.client.get(self.list_all_url)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data[0]["title"], "test1")
        self.assertFalse(response_data[0]["completed"])
        self.assertEqual(response_data[1]["title"], "test2")
        self.assertTrue(response_data[1]["completed"])

    def test_detail_view(self) -> None:
        response = self.client.get(self.list_all_url)
        response_data = response.data
        id_0 = response_data[0]["id"]

        detail_url = f"/api/task-detail/{id_0}/"
        response = self.client.get(detail_url)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["title"], "test1")
        self.assertFalse(response_data["completed"])

    def test_create_view(self) -> None:
        payload_title = "Testing Post"
        payload = {"title": payload_title, "completed": True}

        response = self.client.post(self.list_all_url, payload)
        response_data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(response_data["title"], payload_title)
        self.assertTrue(response_data["completed"])
