# Generated by Django 4.0.7 on 2023-03-14 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favorits', '0004_favoritlist_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritlist',
            name='favorite_products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
