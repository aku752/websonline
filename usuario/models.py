from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import random
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Datos(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)   
    carnet_identidad = models.IntegerField()
    empresa = models.CharField(max_length=50)
    nit = models.IntegerField()
    telefono = models.IntegerField()
    pais = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='perfil', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Datos'
        
    def __str__(self):
        return "{}".format(self.usuario)    

SERVICIO = (
    ("Marketing", "Marketing"),
    ("Diseño web", "Diseño web"),
    ("Hosting profesional", "Hosting profesional"),
    ("Inscripcion de dominio", "Inscripcion de dominio"),
)

class ServicioActivo(models.Model): 
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)
    proyecto = models.CharField(max_length=50)   
    servicio = models.CharField(max_length=50,choices=SERVICIO)
    inicio = models.DateField()
    final = models.DateField()
    precio = models.IntegerField()
    progreso = models.CharField(max_length=200)
    detalle = models.TextField(max_length=2000)
    slug= models.SlugField(null=False,blank=False,unique=True)
    estado = models.BooleanField(default=True) 

    class Meta:
        verbose_name_plural = 'Servicios Activos'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto) + slugify(self.inicio)
        super(ServicioActivo, self).save(*args, **kwargs)    

    def __str__(self):
        return "{}".format(self.usuario)

TIPO =(
    ("Pago", "Pago"),
    ("Retraso", "Retraso"),
    ("Promocion", "Promocion"),
)

class Notificasion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO)
    mensaje = models.TextField(max_length=200)
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Notificasiones'

    def __str__(self):
        return "{}".format(self.tipo)
    
ESTADO_PAGO=(
    ('Impago','Impago'),
    ('Pago','Pago'),
)
class Pagos(models.Model):  
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=50, choices=SERVICIO)
    pago = models.IntegerField()
    acordado = models.IntegerField()   
    situacion = models.CharField(max_length=50, choices=ESTADO_PAGO)
    nro_factura= models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Pagos'
       
    def __str__(self):
        return "{}".format(self.usuario)

AREA=(
    ('Ventas','Ventas'),
    ('Soporte Tecnico','Soporte Tecnico'),
)


def numero():
    numero = random.randint(1000, 9999)
    return str(numero)

#Ahora puedo llamar a mi funcion en mi modelo

class Ticket(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  
    numero_ticket = models.CharField(max_length=5, default=numero)
    fecha = models.DateField(auto_now_add=True)
    departamento = models.CharField(max_length=50, choices=AREA)
    asunto = models.CharField(max_length=100)    
    problema = models.TextField(max_length=200)
    estado = models.BooleanField(default=True)
    

    #Sobreeescribimos el metodo para que me muestre numeor de ticket
    def __str__(self):
        return '{}'.format(self.numero_ticket,self.fecha)

    

class Respuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    respuesta = models.TextField(max_length=200)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.numero_ticket,self.fecha)


class Question(models.Model):
    top_text = models.CharField(max_length=200)
    bottom_text = models.CharField(max_length=200)
    tree_text = models.CharField(max_length=200)
    four_text = models.CharField(max_length=200)
   # segundo_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{},{}".format(self.four)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.question)
