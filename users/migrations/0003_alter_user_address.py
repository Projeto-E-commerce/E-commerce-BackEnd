# Generated by Django 4.0.7 on 2023-03-06 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
        ('users', '0002_alter_user_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_user', to='addresses.address'),
        ),
    ]
