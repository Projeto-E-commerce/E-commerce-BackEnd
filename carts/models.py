from django.db import models

# Create your models here.
class Cart(models.Model):
    total_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        read_only=True,
        # read only pois a logica do total sera feita pelo serializer
    )


class Cart_product(models.Model):
    cart = models.ForeignKey(
        "carts.Cart",
        on_delete=models.CASCADE,
        related_name="products",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="cart",
    )
