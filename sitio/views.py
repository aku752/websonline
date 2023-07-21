from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Create your views here.   
# Solamente lo principal no hay vistas generales



def index(request):   
    if not request.user.is_authenticated:        
        return redirect('login')
    #CONTEXT PROCESSOR 
    return redirect('resumen')
    #return render(request, 'resumen.html',{}) 

def login_view(request):
    if request.method == 'POST':  
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        datos=authenticate(username=usuario, password=password)      
        if datos:
            login(request, datos)      
            messages.success(request,'Bienvenido {}'.format(datos.first_name))
            return redirect('resumen')
        else:
            messages.error(request,'Usuario o password no valido')

    return render(request,'login.html', {}) 


def logout_view(request):    
    logout(request)
    messages.success(request,'Sesion cerrada exitosamente')
    return redirect('login')


def register_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = RegistroForm(request.POST or None)
    return render(request, 'registrar.html', {
                            'forms': form
    })


class Error404View(TemplateView):
    template_name= '404_error.html'

class Error500View(TemplateView):
    template_name= '500_error.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view






        
   


    



