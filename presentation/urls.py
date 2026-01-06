"""
CAPA DE PRESENTACIÓN - URLs
Define las rutas web de la aplicación.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lote/registrar/', views.registrar_lote, name='registrar_lote'),
    path('transformacion/registrar/', views.registrar_transformacion, name='registrar_transformacion'),
    path('logistica/registrar/', views.registrar_logistica, name='registrar_logistica'),
    path('trazabilidad/consultar/', views.consultar_trazabilidad, name='consultar_trazabilidad'),
]
