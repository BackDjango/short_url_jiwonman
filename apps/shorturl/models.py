from django.db import models

from commons.models import BaseModel


class ShortURL(BaseModel):
    key = models.CharField(max_length=6, primary_key=True)
    url = models.URLField(unique=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    count = models.IntegerField(default=0)
    daily_count = models.JSONField(default=dict)
    referrer_count = models.JSONField(default=dict)
    # deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "short_url"
