from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UsuarioForm
from .models import ServicioActivo, Datos, Notificasion, Pagos, Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.template import loader, RequestContext
# Create your views here.
# PARA FUNCIONES Funcion autenticar
# CONTEXT PROCESSOR

# llamamos al usuario con request
@login_required(login_url='login')
def usuario(request):         
    return render(request, 'perfil.html', {})   

def crear_usuario(request):
    # enviar datos
    if request.method=='POST':
        usuario_form= UsuarioForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()
            return redirect('resumen')
    else:
        # Si no hay formulario pintarme los campos
        usuario_form = UsuarioForm()
    return render(request,'crear-usuario.html', {'usuario_form':usuario_form})

def editar_usuario(request,id):
    usuario = Datos.objects.get(id=id)
    if request.method == 'GET':
        usuario_form=UsuarioForm(instance=usuario)
    else:
        usuario_form=UsuarioForm(request.POST,instance=usuario)
        if usuario_form.is_valid():
            usuario_form.save()
        return redirect('index')

    return render(request,'modal/modal-editar-datos.html',{'usuario_form':usuario_form})

def actualizar_usuario(request):
    pass

@login_required(login_url='login')
def pagos(request):    
    usuario = request.user   
    adeuda = Pagos.objects.filter(usuario=User.objects.get(username=usuario))
    tipo_pago = adeuda.filter(situacion='Impago')
    resultado = 0
    for total in tipo_pago:
        resultado=total.pago+resultado
    iva = resultado * 0.13 
    total = iva + resultado  
    deuda = adeuda.all() 

    return render(request, 'pagos.html', {'deudas': deuda,
                                          'resultados':resultado,
                                          'ivas':iva,
                                          'totales':total})



@login_required(login_url='login')
def soporte(request):
    usuario = request.user
    activos = Ticket.objects.filter(usuario=User.objects.get(username=usuario))
    ticket_activo = activos.filter(estado=True)

    return render(request, 'soporte.html', {'ticket_activos': ticket_activo})
    
  


@login_required(login_url='login')
def detalles(request, slug):
    usuario = request.user
    servicio = ServicioActivo.objects.filter(usuario=User.objects.get(username=usuario)) 
    serv_web = servicio.get(slug=slug)    
    return render(request, 'detalle.html', {'serv_webs':serv_web})

@login_required(login_url='login')
def resumen(request):
    usuario = request.user  
    filtro_servicio_activo = ServicioActivo.objects.filter(usuario=User.objects.get(username=usuario))    
    serv_web = filtro_servicio_activo
    web_activa = serv_web.filter(servicio__iexact='Diseño web')
    web_cantidad = serv_web.filter(servicio__iexact='Diseño web').count()    
    serv_hosting = filtro_servicio_activo
    hosting_activa = serv_hosting.filter(servicio__iexact='Hosting profesional')
    hosting_cantidad = serv_hosting.filter(servicio__iexact='Hosting profesional').count()
    serv_marketing = filtro_servicio_activo
    marketing_activa = serv_marketing.filter(servicio__iexact='Marketing')
    marketing_cantidad = serv_marketing.filter(servicio__iexact='Marketing').count()
    serv_inscripcion = filtro_servicio_activo
    inscripcion_activa = serv_inscripcion.filter(servicio__iexact='Inscripcion de dominio')
    inscripcion_cantidad = serv_inscripcion.filter(servicio__iexact='Inscripcion de dominio').count()
    
    return render(request, 'resumen.html', {'serv_webs': web_activa,
                                            'web_cantidades':web_cantidad,
                                            'serv_hostings':hosting_activa,
                                            'hosting_cantidades':hosting_cantidad,
                                            'serv_marketings':marketing_activa,
                                            'marketing_cantidades':marketing_cantidad,
                                            'serv_inscripciones':inscripcion_activa,
                                            'inscripcion_cantidades':inscripcion_cantidad                                        
                                            })


@login_required(login_url='login')
def campana(request):
    return render(request, 'notificasiones/campana.html',{})


@login_required(login_url='login')
def leer_campana(request,id):
    leer = Notificasion.objects.get(id=id)
    leer.estado = False 
    leer.save()

    return render(request, 'notificasiones/campana.html', {})

@login_required(login_url='login')
def ticket(request):
    return render(request, 'crear-ticket.html',{})


@login_required(login_url='login')
def crear_ticket(request):
    usuario = request.user    
    asunto = request.POST['asunto']
    departamento = request.POST['departamento']
    mensaje = request.POST['mensaje']
    ticket = Ticket.objects.create(usuario=request.user,asunto=asunto, departamento=departamento, problema=mensaje) 
    activos = Ticket.objects.filter(usuario=User.objects.get(username=usuario))
    ticket_activo = activos.filter(estado=True) 

    return render(request, 'soporte.html', {'ticket_activos':ticket_activo})


def guia_tutorial(request):  

    return render(request, 'guia-tutorial.html', {})

class DetalleSoporteView(TemplateView):
    template_name='detalle-soporte.html'

# class UsuarioUpdate(UpdateView):
#     model = Datos
#     template_name = 'perfil.html'
#     form_class = UsuarioForm
#     success_url = reverse_lazy('resumen')
    



