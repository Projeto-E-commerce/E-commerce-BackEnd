from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, unique=True)
    storage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True)

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )
