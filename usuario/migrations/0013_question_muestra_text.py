# Generated by Django 4.1 on 2022-08-16 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0012_question_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='muestra_text',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
    ]