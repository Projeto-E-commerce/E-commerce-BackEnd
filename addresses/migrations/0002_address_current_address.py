# Generated by Django 4.0.7 on 2023-03-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='current_address',
            field=models.BooleanField(default=False),
        ),
    ]
