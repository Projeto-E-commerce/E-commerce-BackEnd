from django.db import models


class ChoiceCategory(models.TextChoices):
    ALIMENTOS = "alimentos"
    BEBIDAS = "bebidas"
    BRINQUEDOS = "brinquedos"
    JOGOS = "jogos"
    ELETRONICO = "eletronicos"
    CELULARES = "celulares"
    AUTOMOTIVO = "automotivo"
    INFORMATICA = "informatica"
    LIVROS = "livros"
    PET_SHOP = "pet shop"
    DEFAULT = ""


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(
        max_length=50,
        choices=ChoiceCategory.choices,
        default=ChoiceCategory.DEFAULT
    )
    storage = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True)

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )
