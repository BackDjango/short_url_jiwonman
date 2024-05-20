from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from apps.users.manager import UserManager
from commons.models import BaseModel


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
