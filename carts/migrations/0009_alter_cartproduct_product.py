# Generated by Django 4.0.7 on 2023-03-09 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_category'),
        ('carts', '0008_cartproduct_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
