"""
Users application API resources

"""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from users.serializers import UserModelSerializer

UserModel = get_user_model()


@api_view(["GET", "POST"])
def users_list_resource(request: Request) -> Response:
    """
    Handle requests to users (list) api

    This resource is used to retrieve a list of all users,
    or to register a new one.

    """

    if request.method == "GET":
        qs = UserModel.objects.all()
        serializer = UserModelSerializer(qs, many=True)

        return Response(serializer.data)

    serializer = UserModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT"])
def users_detail_resource(request: Request, pk: int) -> Response:
    """
    Handle requests to users (detail) api

    This resource is used to retrieve data on a single user,
    or to fully update it.

    """

    try:
        instance = UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserModelSerializer(instance)

        return Response(serializer.data)

    serializer = UserModelSerializer(instance, request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
