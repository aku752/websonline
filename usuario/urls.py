from django.urls import path
from .views import (soporte, pagos, resumen, detalles, campana,
                    leer_campana, ticket, crear_ticket,guia_tutorial, DetalleSoporteView,
                    UsuarioUpdate, UsuarioList)
# siempre poner la barra / al final de la url y el name es al html
from django.views.generic import TemplateView
urlpatterns = [
    # path('', usuario, name='usuario'),
    path('usuario-lista/', UsuarioList.as_view(), name='usuario-list'),
    path('editar-datos/<int:pk>', UsuarioUpdate.as_view(), name='usuario_actualizar'),
    path('detalle-soporte/', DetalleSoporteView.as_view(), name='detalle-soporte'),
    path('pagos/', pagos, name='pagos'),
    path('soporte/', soporte, name='soporte'),
    path('resumen/', resumen, name='resumen'),
    path('campana/', campana, name='campana'),
    path('ticket/', ticket, name='ticket'),  
    path('guia-tutorial/', guia_tutorial, name ='guia_tutorial'),
    path('crear-ticket/', crear_ticket, name='crear_ticket'),  
    path('<slug:slug>/', detalles, name='detalles'),
    path('leercampana/<int:id>/', leer_campana , name='leer_campana'), 
] 
