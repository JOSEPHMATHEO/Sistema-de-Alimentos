"""
Configuración de la aplicación de la capa de datos.
"""
from django.apps import AppConfig


class DataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data'
    verbose_name = 'Capa de Datos'
