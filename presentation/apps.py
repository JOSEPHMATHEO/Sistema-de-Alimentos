"""
Configuración de la aplicación de la capa de presentación.
"""
from django.apps import AppConfig


class PresentationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'presentation'
    verbose_name = 'Capa de Presentación'
