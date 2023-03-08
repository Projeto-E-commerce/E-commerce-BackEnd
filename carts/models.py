from django.db import models

from products.models import Product


# Create your models here.
class Cart(models.Model):
    total_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
    )

    cart_products = models.ManyToManyField(
        Product, through="carts.CartProduct", related_name="shopping_cart"
    )


class CartProduct(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    product_count = models.PositiveIntegerField(default=1)
