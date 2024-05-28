from datetime import timedelta
from django.utils import timezone

from rest_framework import serializers

from apps.shorturl.models import ShortURL
from commons.utils import Base62


class ShortURLSerializer(serializers.ModelSerializer):
    url = serializers.URLField(required=True)
    expired_at = serializers.DateTimeField(required=False)
    daily_count = serializers.JSONField(read_only=True)
    referrer_count = serializers.JSONField(read_only=True)
    key = serializers.CharField(read_only=True)


    class Meta:
        model = ShortURL
        fields = ["url", "expired_at", "count", "daily_count", "referrer_count", "key"]

    def validate_expired(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError("URL이 만료되었습니다.")
        return value
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    # def validate(self, data):
    #     expired_at = data.get("expired_at")
    #     if expired_at:
    #         self.validate_expired(expired_at)
    #     return data

    def delete_expired_url(self):
        instance = self.instance
        instance.delete()

    def create(self, validated_data):
        url = validated_data["url"]

        exist_url = ShortURL.objects.filter(url=url).first()
        if exist_url:
            return exist_url

        key = self.generate_key()
        validated_data["key"] = key
        instance = super().create(validated_data)
        return instance

    def generate_key(self):
        base62 = Base62()
        while True:
            key = base62.encode()
            if not ShortURL.objects.filter(key=key).exists():
                return key
            
    def increase_count(self, instance, referrer):
        self.increase_daily_count(instance)
        self.increase_referrer_count(instance, referrer)
        instance.count += 1
        instance.save()
        return instance
    
    def increase_daily_count(self, instance):
        # isoformat -> 'YYYY-MM-DD'
        today = timezone.now().date().isoformat()
        daily_count = instance.daily_count
        daily_count[today] = daily_count.get(today, 0) + 1

    def increase_referrer_count(self, instance, referrer):
        referrer_count = instance.referrer_count
        referrer_count[referrer] = referrer_count.get(referrer, 0) + 1
        instance.referrer_count = referrer_count

    def get_weekly_count(self, instance):
        today = timezone.now().date()
        seven_days = today - timedelta(days=7)
        result = {}
        
        for day in instance.daily_count:
            if day >= seven_days.isoformat():
                result[day] = instance.daily_count.get(day, 0) 

        return result
