from django.db import models

class FavoriteList(models.Model):
    user = models.ForeignKey(
        "users.User", 
        on_delete=models.CASCADE, 
        related_name="favorite_list",
    )
    
    product = models.ManyToManyField(
        "products.Product", related_name="favorite"
    )
