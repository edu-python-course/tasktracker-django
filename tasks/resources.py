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
def tasks_list_resource(request: Request) -> Response:
    """
    Handle requests to tasks (list) api

    This resource is used to retrieve a list of all tasks,
    or to create a new one.

    """

    if request.method == "GET":
        qs = TaskModel.objects.all()
        serializer = TaskModelReadSerializer(qs, many=True)

        return Response(serializer.data)

    serializer = TaskModelWriteSerializer(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        # because of RandomUUID usage the task should be fetched from DB
        instance = TaskModel.objects.filter(
            summary=instance.summary,
            description=instance.description,
            completed=instance.completed,
            reporter=instance.reporter,
            assignee=instance.assignee,
            created_at=instance.created_at,
            updated_at=instance.updated_at,
        ).first()
        serializer = TaskModelReadSerializer(instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def tasks_detail_resource(request: Request, pk: uuid.UUID) -> Response:
    """
    Handle requests to tasks (detail) api

    This resource is used to retrieve details on a single tasks,
    delete it, or update (full or partial).

    Success requests to update or delete task will respond with 200 OK,
    to support HTMX operations.

    """

    try:
        instance = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskModelReadSerializer(instance)

        return Response(serializer.data)

    if request.method == "DELETE":
        instance.delete()

        return Response(status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = TaskModelWriteSerializer(instance, request.data)
    else:
        serializer = TaskModelWriteSerializer(
            instance, request.data, partial=True
        )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
