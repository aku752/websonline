from django import forms

class RegistroForm(forms.Form):
    usuario = forms.CharField(required=True,
                              min_length=4, max_length=50,
                              widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'id':'usuario',
                                'placeholder':'Usuario'
                              }))
    email= forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'id':'email',
                                'placeholder':'ejemplo@gmail.com'
                            }))
    password = forms.CharField(required=True,
                             widget=forms.PasswordInput(attrs={
                                'class':'form-control'
                             }))