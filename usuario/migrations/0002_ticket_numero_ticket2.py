# Generated by Django 4.1 on 2022-08-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='numero_ticket2',
            field=models.CharField(default='123ma', max_length=10),
            preserve_default=False,
        ),
    ]