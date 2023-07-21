from django import forms
from .models import Datos
from django.forms import ValidationError 

class UsuarioForm(forms.ModelForm):

    def clean_carnet_identidad(self):
        carnet = self.cleaned_data["carnet_identidad"]
        if carnet >= 2147483647:
            raise ValidationError("Introduzca un numero de carnet valido")
        return carnet
        
    def clean_telefono(self):
        telefono = self.cleaned_data["telefono"]      
        if telefono >= 2147483647:
            raise ValidationError("Introduzca un numero de telefono valido")
        return telefono
    
    def clean_nit(self):       
        nit = self.cleaned_data["nit"]
        if nit >= 2147483647:
            raise ValidationError("Introduzca un numero de nit valido") 
        return nit
            
    
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
        