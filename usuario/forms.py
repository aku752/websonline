from django import forms 
from .models import Datos

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = ['carnet_identidad',
                  'empresa',
                  'nit',
                  'telefono',
                  'pais',
                  'ciudad',
                  'direccion',
                  'imagen']
        