"""
Tasks application API resources

"""

import uuid

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from tasks.models import TaskModel
from tasks.serializers import TaskModelReadSerializer, TaskModelWriteSerializer


@api_view(["GET", "POST"])
def tasks_list(request: Request) -> Response:
    """
    Handle requests to task list endpoint

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


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def tasks_detail(request: Request, pk: uuid.UUID) -> Response:
    """
    Handle requests to task detail endpoint

    """

    try:
        instance = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskModelReadSerializer(instance)

        return Response(serializer.data)  # HTTP_200_OK

    if request.method == "DELETE":
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "PATCH":
        serializer = TaskModelWriteSerializer(instance, request.data,
                                              partial=True)
    else:  # PUT
        serializer = TaskModelWriteSerializer(instance, request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
