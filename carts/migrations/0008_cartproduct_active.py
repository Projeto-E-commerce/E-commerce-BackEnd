# Generated by Django 4.0.7 on 2023-03-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0007_cartproduct_total_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartproduct",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
