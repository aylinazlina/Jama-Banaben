# Generated by Django 5.1.2 on 2024-10-31 14:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamaZZZ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
