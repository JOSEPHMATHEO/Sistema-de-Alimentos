"""
CAPA DE DATOS - Repositorios
Clases que encapsulan el acceso a la base de datos.
Patrón Repository: separa la lógica de acceso a datos de la lógica de negocio.
"""
from django.db.models import Q
from .models import Lote, Transformacion, Logistica


class LoteRepository:
    """
    Repositorio para operaciones con la tabla Lote.
    Proporciona métodos para crear, leer, actualizar y eliminar lotes.
    """
    
    @staticmethod
    def crear_lote(codigo_lote, ubicacion_cultivo, fecha_cosecha, observaciones=None):
        """
        Crea un nuevo lote en la base de datos.
        """
        lote = Lote.objects.create(
            codigo_lote=codigo_lote,
            ubicacion_cultivo=ubicacion_cultivo,
            fecha_cosecha=fecha_cosecha,
            observaciones=observaciones
        )
        return lote
    
    @staticmethod
    def obtener_por_codigo(codigo_lote):
        """
        Obtiene un lote por su código único.
        Retorna None si no existe.
        """
        try:
            return Lote.objects.get(codigo_lote=codigo_lote)
        except Lote.DoesNotExist:
            return None
    
    @staticmethod
    def obtener_todos():
        """
        Obtiene todos los lotes registrados.
        """
        return Lote.objects.all()
    
    @staticmethod
    def existe_codigo(codigo_lote):
        """
        Verifica si existe un lote con el código dado.
        """
        return Lote.objects.filter(codigo_lote=codigo_lote).exists()


class TransformacionRepository:
    """
    Repositorio para operaciones con la tabla Transformacion.
    """
    
    @staticmethod
    def crear_transformacion(lote, proceso_lavado, fecha_lavado, proceso_empaquetado,
                            fecha_empaquetado, control_calidad, observaciones_calidad=None):
        """
        Crea un nuevo registro de transformación.
        """
        transformacion = Transformacion.objects.create(
            lote=lote,
            proceso_lavado=proceso_lavado,
            fecha_lavado=fecha_lavado,
            proceso_empaquetado=proceso_empaquetado,
            fecha_empaquetado=fecha_empaquetado,
            control_calidad=control_calidad,
            observaciones_calidad=observaciones_calidad
        )
        return transformacion
    
    @staticmethod
    def obtener_por_lote(lote):
        """
        Obtiene todas las transformaciones de un lote específico.
        """
        return Transformacion.objects.filter(lote=lote)
    
    @staticmethod
    def obtener_todas():
        """
        Obtiene todas las transformaciones registradas.
        """
        return Transformacion.objects.all()


class LogisticaRepository:
    """
    Repositorio para operaciones con la tabla Logistica.
    """
    
    @staticmethod
    def crear_logistica(lote, temperatura_transporte, fecha_inicio_transporte,
                       fecha_entrega_supermercado, nombre_supermercado,
                       direccion_supermercado, observaciones=None):
        """
        Crea un nuevo registro de logística.
        """
        logistica = Logistica.objects.create(
            lote=lote,
            temperatura_transporte=temperatura_transporte,
            fecha_inicio_transporte=fecha_inicio_transporte,
            fecha_entrega_supermercado=fecha_entrega_supermercado,
            nombre_supermercado=nombre_supermercado,
            direccion_supermercado=direccion_supermercado,
            observaciones=observaciones
        )
        return logistica
    
    @staticmethod
    def obtener_por_lote(lote):
        """
        Obtiene todos los registros logísticos de un lote específico.
        """
        return Logistica.objects.filter(lote=lote)
    
    @staticmethod
    def obtener_todas():
        """
        Obtiene todos los registros logísticos.
        """
        return Logistica.objects.all()
