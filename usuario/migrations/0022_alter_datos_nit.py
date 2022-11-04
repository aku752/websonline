# Generated by Django 4.1 on 2022-10-11 03:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0021_alter_datos_nit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos',
            name='nit',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
