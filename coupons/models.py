from django.db import models


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateField(auto_now_add=True)
    valid_to = models.DateField()
    discount = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="coupons",
    )
