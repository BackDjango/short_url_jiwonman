from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.users import views

urlpatterns = [
    path("signup/", views.SignUpAPIView.as_view(), name="signup"),
    path("signout/", views.SingOutAPIView.as_view(), name="signout"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("logout/", views.LogoutAPIView.as_view(), name="logout"),
]
