# Create your tests here.
from api.models import Task
from model_mommy import mommy
from rest_framework.test import APITestCase


class TestView(APITestCase):
    def setUp(self) -> None:
        self.task1 = mommy.prepare(Task, title="test1", completed=False)
        self.task2 = mommy.prepare(Task, title="test2", completed=True)

    def test_task_list_view(self) -> None:
        url = "/api/task-list/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_task_list(self) -> None:
        self.assertFalse(self.task1.completed)
        self.assertTrue(self.task2.completed)
