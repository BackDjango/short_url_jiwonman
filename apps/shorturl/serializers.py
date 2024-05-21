from django.utils import timezone
from rest_framework import serializers

from apps.shorturl.models import ShortURL
from commons.utils import Base62


class ShortURLSerializer(serializers.ModelSerializer):
    url = serializers.URLField(required=True, write_only=True)
    expired_at = serializers.DateTimeField(required=False, write_only=True)

    class Meta:
        model = ShortURL
        fields = ["url", "expired_at", "deleted_at", "count"]

    def validate_expired(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError("만료일시는 현재 날짜보다 늦어야 합니다.")
        
    def delete_expired_url(self):
        instance = self.instance
        instance.delete()
    
    def create(self, validated_data):
        url = validated_data['url']

        exist_url = ShortURL.objects.filter(url=url).first()
        if exist_url:
            return {"key": exist_url.key}

        key = self.generate_key()
        validated_data['key'] = key
        return super().create(validated_data)
    
    def generate_key(self):
        base62 = Base62()
        while True:
            key = base62.encode()
            if not ShortURL.objects.filter(key=key).exists():
                return key