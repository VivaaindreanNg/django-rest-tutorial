# Create your tests here.
from api.models import Task
from django.test import Client, TestCase
from django.test.utils import setup_test_environment, teardown_test_environment
from model_mommy import mommy


class TestView(TestCase):
    def setUp(self) -> None:
        teardown_test_environment()
        setup_test_environment()
        self.client = Client()
        self.task1 = mommy.prepare(Task, title="test1", completed=False)
        self.task2 = mommy.prepare(Task, title="test2", completed=True)

    def test_task_list_view(self) -> None:
        response = self.client.get("/api/task-list/")
        self.assertEqual(response.status_code, 200)

    def test_task_list(self) -> None:
        self.assertFalse(self.task1.completed)
        self.assertTrue(self.task2.completed)
