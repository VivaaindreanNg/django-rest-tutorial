from api.models import Task
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    """[This function is meant to return a list of overviews for different
        API based on urls patterns defined in api_urls variable below.]

    Args:
        request [object]: [Takes argument from HTTP request]

    Returns:
        [JSON Response]: [Returns list of urls for our API]
    """
    api_urls = {
        "Create [POST]": "/tasks/",
        "List [GET]": "/tasks/",
        "Detail View [GET]": "/tasks/<str:pk>/",
        "Update [PUT]": "/tasks/<str:pk>/",
        "Delete [DELETE]": "/tasks/<str:pk>/",
    }
    return Response(api_urls)


@api_view(["GET", "POST"])
def task_list(request):
    """[List all code tasks if GET request,
    or create a new task if POST request.]

    Args:
        request [object]: [Takes argument from HTTP request]

    Returns:
        [JSON Response]: [Returns all Tasks data queried from db, which
        has been serialized in format of JSON.]
    """
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def task_detail(request, pk) -> Response:
    """[Display, Update or Delete a single Task object based on the ID given (aka primary key)]

    Args:
        request [object]: [Takes argument from HTTP request]
        pk [str]: [Primary key of a Task's ID]

    Returns:
        [JSON Response]: [Returns a single Task from DB in format of JSON.]
    """

    # first, get task from db based on supplied pk
    task = Task.objects.get(id=pk)

    if request.method == "GET":
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    elif request.method == "PUT" or request.method == "PATCH":
        # Get the updated data from request and update said task
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == "DELETE":
        # Delete said task
        task.delete()
        return Response("Task deleted")
