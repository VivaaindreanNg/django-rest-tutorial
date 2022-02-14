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

    def test_task_list_view(self) -> None:
        response = self.client.get(self.list_all_url)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data[0]["title"], "test1")
        self.assertFalse(response_data[0]["completed"])
        self.assertEqual(response_data[1]["title"], "test2")
        self.assertTrue(response_data[1]["completed"])

    def test_task_detail_view(self) -> None:
        response = self.client.get(self.list_all_url)
        response_data = response.json()
        id_0 = response_data[0]["id"]

        detail_url = f"/api/task-detail/{id_0}/"
        get_response = self.client.get(detail_url)
        get_response_data = get_response.json()

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response_data["title"], "test1")
        self.assertFalse(get_response_data["completed"])
