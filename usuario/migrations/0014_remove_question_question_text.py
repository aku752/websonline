# Generated by Django 4.1 on 2022-08-16 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_question_muestra_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
    ]