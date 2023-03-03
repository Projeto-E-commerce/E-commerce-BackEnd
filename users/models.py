from django.db import models
from django.contrib.auth.models import AbstractUser


class ChoiceUser(models.TextChoices):
    CLIENT = "client"
    SALESMAN = "salesman"
    ADMIN = "admin"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    type_user = models.CharField(choices=ChoiceUser.choices, default=ChoiceUser.CLIENT)
