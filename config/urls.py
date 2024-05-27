from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("auth/", include("apps.users.urls")),
    path("url/", include("apps.shorturl.urls")),
]

from config.swagger.setup import SwaggerSetup

urlpatterns = SwaggerSetup.do_urls(urlpatterns=urlpatterns)
