# Generated by Django 4.1 on 2022-09-06 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuario', '0018_alter_ticket_numero_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificasion',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='notificasion',
            name='mensaje',
            field=models.TextField(max_length=200, verbose_name='Mensaje'),
        ),
        migrations.AlterField(
            model_name='notificasion',
            name='tipo',
            field=models.CharField(choices=[('Pago', 'Pago'), ('Retraso', 'Retraso'), ('Promocion', 'Promocion')], max_length=20, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='notificasion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
