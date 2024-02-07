"""
Tasks application API resources

"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from tasks.models import TaskModel
from tasks.serializers import TaskModelReadSerializer, TaskModelWriteSerializer


@api_view(["GET", "POST"])
def tasks_list_resource(request: Request) -> Response:
    """
    Handle requests to tasks (list) api

    """

    if request.method == "GET":
        qs = TaskModel.objects.all()
        serializer = TaskModelReadSerializer(qs, many=True)

        return Response(serializer.data)

    serializer = TaskModelWriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
