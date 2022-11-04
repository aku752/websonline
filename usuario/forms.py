from django import forms 
from .models import Datos

class UsuarioForm(forms.ModelForm):
   # nit=forms.IntegerField(min_value=1,max_value=99999999)
    class Meta:
        model = Datos
        #fields = '__all__'
        fields = ['carnet_identidad',
                  'empresa',
                  'nit',
                  'telefono',
                  'pais',
                  'ciudad',
                  'direccion',
                  'imagen']
    #     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    # carnet_identidad = models.IntegerField()
    # empresa = models.CharField(max_length=50)
    # nit = models.IntegerField()
    # telefono = models.IntegerField()
    # pais = models.CharField(max_length=50)
    # ciudad = models.CharField(max_length=50)
    # direccion = models.CharField(max_length=50)
    # estado = models.BooleanField(default=True)
    # imagen = models.ImageField(upload_to='perfil', null=True, blank=True)
        