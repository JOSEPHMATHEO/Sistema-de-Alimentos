"""
Configuración de URLs principales del proyecto STA.
Redirige las peticiones a la aplicación de presentación.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs de la capa de presentación
    path('', include('presentation.urls')),
]
