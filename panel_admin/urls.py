"""panel_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from sitio import views
from sitio.views import Error404View, Error500View,login_view,logout_view,index
from django.conf.urls import handler404, handler500
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cuentas/login/', login_view, name='login'),
    path('cuentas/logout/', logout_view, name='logout'), 
    path('usuarios/', include(('usuario.urls'))),
    path('servicios/', include(('servicio.urls'))),
    path("i18n/", include("django.conf.urls.i18n")),

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = Error404View.as_view()
handler500 = Error500View.as_error_view()
# HABILITAR EN PRODUCCION
#static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
