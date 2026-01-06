"""
WSGI config for sta_project.
Expone el callable WSGI como una variable a nivel de módulo llamada ``application``.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sta_project.settings')

application = get_wsgi_application()
