from django.contrib import admin
from .models import (ServicioActivo, Datos, Notificasion, Ticket,
                     Respuesta, Pagos, Question, Choice)
# Register your models here.


class DatosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'carnet_identidad', 'empresa', 'nit', 'telefono', 'pais', 'ciudad', 'direccion', 'estado')
    list_filter = ('usuario', 'carnet_identidad', 'empresa', 'nit', 'telefono', 'pais', 'ciudad', 'direccion', 'estado')
    search_fields = ('usuario', 'carnet_identidad', 'empresa', 'nit', 'telefono', 'pais', 'ciudad', 'direccion', 'estado')
    ordering = ('usuario', 'carnet_identidad', 'empresa', 'nit', 'telefono', 'pais', 'ciudad', 'direccion', 'estado')
    list_editable =('estado',)
    list_per_page = 10

class ServicioActivoAdmin(admin.ModelAdmin):
    list_display=('usuario','proyecto','servicio','inicio','final','precio','estado')
    list_editable = ('estado',)
    exclude=('slug',)

class NotificasionAdmin(admin.ModelAdmin):
    list_display=('usuario','tipo','estado')
    list_editable = ('estado',)

class PagosAdmin(admin.ModelAdmin):
    list_display=('usuario','servicio','pago','acordado')

class TicketAdmin(admin.ModelAdmin):
    list_display=('usuario','numero_ticket','fecha','asunto','problema', 'estado')
    list_editable=('estado',)    

class RespuestaAdmin(admin.ModelAdmin):
    list_display=('numero_ticket','respuesta','estado')
    list_editable=('estado',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pub_date',)
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','choice_text')


admin.site.register(ServicioActivo, ServicioActivoAdmin)
admin.site.register(Notificasion, NotificasionAdmin)
admin.site.register(Datos, DatosAdmin)
admin.site.register(Pagos, PagosAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

# admin.site.site_header = 'Websonline'
# admin.site.index_title = 'Panel de control Websonline'
# admin.site.site_title = 'Websonline'
