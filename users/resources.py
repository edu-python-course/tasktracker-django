"""
Users application API resources

"""

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class AuthTokenAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        ctx = {"request": request}
        serializer = self.serializer_class(data=request.data, context=ctx)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "user_pk": user.pk,
            "token": token.key,
        })
