from django.contrib.auth import get_user_model, login, authenticate, logout

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

AuthUser = get_user_model()


class SignUpAPIView(APIView):
    def post(self, request: Request) -> Response:
        try:
            AuthUser.objects.create_user(**request.data)
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SingOutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request) -> Response:
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginAPIView(APIView):
    def post(self, request: Request) -> Response:
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
