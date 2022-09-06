from django.shortcuts import render
from django.contrib.auth.models import User

from usuario.models import ServicioActivo

# Create your views here.  
    

def add_servicio(request):    
    return render(request, 'add-servicio.html',{})

def servicio(request):    
    usuario = request.user   
    servicio = ServicioActivo.objects.filter(usuario=User.objects.get(username=usuario))
    servicio_activo = servicio.all()  
    return render(request, 'servicio.html',{'servicios_activos':servicio_activo})

def send_mensaje(request):    
    return render(request, 'mensaje-envio.html',{})
