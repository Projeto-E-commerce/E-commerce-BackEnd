# Generated by Django 4.0.7 on 2023-03-14 14:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorits', '0006_rename_favorite_products_favoritlist_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavoritList',
            new_name='FavoriteList',
        ),
    ]