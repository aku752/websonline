from django.contrib.auth.models import User
from .models import Datos, Notificasion

def procesador(request):
    #sino sabes que usaurio hay, entonces salta
    if request.user.is_authenticated:     
        usuario = request.user
        dato = Datos.objects.filter(usuario=User.objects.get(username=usuario))
        campana = Notificasion.objects.filter(usuario=User.objects.get(username=usuario))
        notificasion = campana.filter(estado=True)
        notificasion_cantidad = notificasion.count()

        return {'datos': dato,
                'notificasiones': notificasion,
                'notificasion_cantidades': notificasion_cantidad}
    # es requerido que vote el contexto vacio, porque es requerido por context processor
    return {}