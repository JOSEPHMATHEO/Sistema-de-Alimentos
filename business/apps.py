"""
Configuración de la aplicación de la capa de lógica de negocio.
"""
from django.apps import AppConfig


class BusinessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'business'
    verbose_name = 'Capa de Lógica de Negocio'
