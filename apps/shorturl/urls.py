from django.urls import path
from . import views

short_url_list = views.ShortURLViewSet.as_view(
    {
        'get': 'list',
        "post": "create"
    }
)

short_url_detail = views.ShortURLViewSet.as_view(
    {
        "get": "retrieve",
        # 'put': 'update',
        # "delete": "destroy",
    }
)

short_url_referrer = views.ShortURLViewSet.as_view(
    {
        "get": "referrer"
    }
)

urlpatterns = [
    path("", short_url_list),
    path("<str:pk>/", short_url_detail),
    path("<str:pk>/+/", short_url_referrer)
]
