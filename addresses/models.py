from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=127)
    number = models.PositiveIntegerField()
    zip_code = models.CharField(max_length=9)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=3)
    aditional_info = models.TextField(null=True)
