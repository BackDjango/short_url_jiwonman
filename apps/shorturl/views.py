from django.shortcuts import render, redirect
from django.utils import timezone

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
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
        summary="전체 URL 조회"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="단축 URL 생성",
    )
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        return Response({"key": instance.key}, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="URL Redirect",
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        referrer = request.META.get("HTTP_REFERER", 'direct')

        serializer = self.get_serializer(instance)

        if instance.expired_at:
            serializer.validate_expired(instance.expired_at)
            instance.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.increase_count(instance, referrer)
        redirect_url = instance.url
        return redirect(redirect_url)
    
    @extend_schema(
        summary="URL Referrer"
    )
    @action(detail=True, methods=["GET"])
    def referrer(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance)

        return Response({
            "count": instance.count,
            "daily_count": serializer.get_weekly_count(instance),
            "referrer_count": instance.referrer_count,
        }, status=status.HTTP_200_OK)