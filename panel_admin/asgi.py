"""
ASGI config for panel_admin project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
#from dj_static import Cling
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panel_admin.settings')

application = get_asgi_application()
 
#application = Cling(get_asgi_application()) 