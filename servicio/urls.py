from django.urls import path
from .views import add_servicio, servicio, send_mensaje
from usuario.views import detalles

urlpatterns = [
    path('', servicio, name='servicio'),
    path('add-servicio/', add_servicio, name='add_servicio'),
    path('mensaje/', send_mensaje, name='send_mensaje'),
    path('detalles/', detalles, name='detalles'),
]
