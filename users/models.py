from django.db import models
from django.contrib.auth.models import AbstractUser


class ChoiceUser(models.TextChoices):
    CLIENT = "client"
    SALESMAN = "salesman"
    ADMIN = "admin"


class User(AbstractUser):
    email = models.EmailField(unique=True)
    type_user = models.CharField(
        max_length=20,
        choices=ChoiceUser.choices,
        default=ChoiceUser.CLIENT,
    )

    cart = models.OneToOneField(
        "carts.Cart",
        on_delete=models.CASCADE,
        related_name="cart_user",
        null=True,
    )

    def __repr__(self) -> str:
        return f"{self.cart} --- {self.username}"
