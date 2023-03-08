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
    total_order = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )

    salesman = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="salesman_product",
        null=True,
    )

    products_list = models.JSONField(default=dict)
