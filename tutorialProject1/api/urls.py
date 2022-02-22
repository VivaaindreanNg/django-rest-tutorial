from django.urls import path

from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("tasks/", views.task_list, name="task-list"),
    path("tasks/<str:pk>/", views.task_detail, name="task-detail"),
]
