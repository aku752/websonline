"""
WSGI config for panel_admin project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
#from dj_static import Cling
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'panel_admin.settings')

application = get_wsgi_application()

#application = Cling(get_wsgi_application()) 
