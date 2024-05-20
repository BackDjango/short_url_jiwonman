from django.shortcuts import render, redirect

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.shorturl.models import ShortURL
from apps.shorturl.serializers import ShortURLSerializer
from commons.utils import Base62

@extend_schema(
    tags=["URL"],
)
class ShortURLViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

    @extend_schema(
        summary="단축 URL 생성",
    )
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        key = instance["key"]
        return Response({"key": key}, status=status.HTTP_201_CREATED)
    
    @extend_schema(
        summary="URL Redirect",
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.count += 1
        instance.save()
        redirect_url = instance.url
        return redirect(redirect_url)