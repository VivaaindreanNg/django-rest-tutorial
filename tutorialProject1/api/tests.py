# Create your tests here.
from api.models import Task
from model_mommy import mommy
from rest_framework.test import APITestCase


class TestView(APITestCase):
    def setUp(self) -> None:
        self.task1 = mommy.make(Task, title="test1", completed=False)
        self.task2 = mommy.make(Task, title="test2", completed=True)

    def test_task_list_view(self) -> None:
        url = "/api/task-list/"
        response = self.client.get(url)
        response_data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data[0]["title"], "test1")
        self.assertFalse(response_data[0]["completed"])
        self.assertEqual(response_data[1]["title"], "test2")
        self.assertTrue(response_data[1]["completed"])

    # def test_task_detail_view(self) -> None:
    #     url = "/api/task-detail/"
    #     import pdb

    #     # pdb.set_trace()
