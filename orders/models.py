from django.db import models


class OrderStatusChoices(models.TextChoices):
    PLACED = "placed"
    IN_PROGRESS = "in progress"
    DELIVERED = "delivered"


class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PLACED,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )
