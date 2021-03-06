from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """[Allows a particular custom Model to be serialized
        into JSON format as response]

    Args:
        serializers (ModelSerializer): [imported from serializers.ModelSerializer]
    """

    types = serializers.CharField(source="get_types_display")

    class Meta:
        model = Task
        fields = "__all__"
