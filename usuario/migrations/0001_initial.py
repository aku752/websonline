# Generated by Django 4.1 on 2022-08-16 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ticket', models.CharField(max_length=10)),
                ('departamento', models.CharField(choices=[('Ventas', 'Ventas'), ('Soporte Tecnico', 'Soporte Tecnico')], max_length=50)),
                ('asunto', models.CharField(max_length=100)),
                ('problema', models.TextField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServicioActivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proyecto', models.CharField(max_length=50)),
                ('servicio', models.CharField(choices=[('Marketing', 'Marketing'), ('Diseño web', 'Diseño web'), ('Hosting profesional', 'Hosting profesional'), ('Inscripcion de dominio', 'Inscripcion de dominio')], max_length=50)),
                ('inicio', models.DateField()),
                ('final', models.DateField()),
                ('precio', models.IntegerField()),
                ('progreso', models.CharField(max_length=200)),
                ('detalle', models.TextField(max_length=2000)),
                ('slug', models.SlugField(unique=True)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(choices=[('Marketing', 'Marketing'), ('Diseño web', 'Diseño web'), ('Hosting profesional', 'Hosting profesional'), ('Inscripcion de dominio', 'Inscripcion de dominio')], max_length=50)),
                ('pago', models.IntegerField()),
                ('acordado', models.IntegerField()),
                ('situacion', models.CharField(choices=[('Impago', 'Impago'), ('Pago', 'Pago')], max_length=50)),
                ('nro_factura', models.CharField(max_length=100)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notificasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Pago', 'Pago'), ('Retraso', 'Retraso'), ('Promocion', 'Promocion')], max_length=20)),
                ('mensaje', models.TextField(max_length=200)),
                ('estado', models.BooleanField(default=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet_identidad', models.IntegerField()),
                ('empresa', models.CharField(max_length=50)),
                ('nit', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('pais', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='perfil')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
