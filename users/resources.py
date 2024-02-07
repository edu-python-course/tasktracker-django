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
def users_resource(request: Request) -> Response:
    """
    Handle requests to users resource

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
