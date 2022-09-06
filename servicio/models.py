from django.db import models


# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='servicios', null=True, blank=True)

    def __str__(self):
        return self.nombre
