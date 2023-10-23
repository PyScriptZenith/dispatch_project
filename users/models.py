from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser




NULLABLE = {"null": True, "blank": True}
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []