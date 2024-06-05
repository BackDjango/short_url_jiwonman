from django.contrib.auth import logout

from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema

from apps.users.serializers import (
    SignUpSerializer,
    EmptySerializer,
    LoginSerializer,
)


class SignUpAPIView(APIView):
    @extend_schema(
        tags=["Auth"],
        summary="회원가입",
        request=SignUpSerializer,
    )
    def post(self, request: Request) -> Response:
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    @extend_schema(
        tags=["Auth"],
        summary="로그인",
        request=LoginSerializer,
    )
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.login(request)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SingOutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["Auth"], summary="회원탈퇴", request=EmptySerializer)
    def delete(self, request: Request) -> Response:
        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["Auth"], summary="로그아웃", request=EmptySerializer)
    def get(self, request: Request) -> Response:
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
