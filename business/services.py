"""
CAPA DE LÓGICA DE NEGOCIO - Servicios
Contiene la lógica de negocio principal del sistema.
Coordina entre la capa de datos y la capa de presentación.
"""
from data.repositories import LoteRepository, TransformacionRepository, LogisticaRepository
from .validators import TrazabilidadValidator


class LoteService:
    """
    Servicio para la gestión de lotes.
    Aplica validaciones de negocio antes de persistir datos.
    """
    
    def __init__(self):
        self.repository = LoteRepository()
        self.validator = TrazabilidadValidator()
    
    def registrar_lote(self, codigo_lote, ubicacion_cultivo, fecha_cosecha, observaciones=None):
        """
        Registra un nuevo lote aplicando validaciones de negocio.
        Retorna: (éxito, resultado_o_error, mensaje)
        """
        # Validación 1: Código de lote
        es_valido, mensaje = self.validator.validar_codigo_lote(codigo_lote)
        if not es_valido:
            return False, None, mensaje
        
        # Validación 2: Verificar que el código no exista
        if self.repository.existe_codigo(codigo_lote):
            return False, None, f"El código de lote '{codigo_lote}' ya existe"
        
        # Validación 3: Fecha de cosecha
        es_valido, mensaje = self.validator.validar_fecha_cosecha(fecha_cosecha)
        if not es_valido:
            return False, None, mensaje
        
        # Si todas las validaciones pasan, crear el lote
        try:
            lote = self.repository.crear_lote(
                codigo_lote=codigo_lote,
                ubicacion_cultivo=ubicacion_cultivo,
                fecha_cosecha=fecha_cosecha,
                observaciones=observaciones
            )
            return True, lote, "Lote registrado exitosamente"
        except Exception as e:
            return False, None, f"Error al registrar el lote: {str(e)}"
    
    def obtener_lote_por_codigo(self, codigo_lote):
        """
        Obtiene un lote por su código.
        """
        lote = self.repository.obtener_por_codigo(codigo_lote)
        if lote:
            return True, lote, "Lote encontrado"
        return False, None, "Lote no encontrado"
    
    def listar_todos_lotes(self):
        """
        Obtiene todos los lotes registrados.
        """
        lotes = self.repository.obtener_todos()
        return True, lotes, f"{len(lotes)} lotes encontrados"


class TransformacionService:
    """
    Servicio para la gestión de procesos de transformación.
    """
    
    def __init__(self):
        self.repository = TransformacionRepository()
        self.lote_repository = LoteRepository()
        self.validator = TrazabilidadValidator()
    
    def registrar_transformacion(self, codigo_lote, proceso_lavado, fecha_lavado,
                                 proceso_empaquetado, fecha_empaquetado,
                                 control_calidad, observaciones_calidad=None):
        """
        Registra un proceso de transformación aplicando validaciones.
        """
        # Validación 1: Verificar que el lote existe
        lote = self.lote_repository.obtener_por_codigo(codigo_lote)
        if not lote:
            return False, None, f"El lote '{codigo_lote}' no existe"
        
        # Validación 2: Control de calidad
        es_valido, mensaje = self.validator.validar_control_calidad(control_calidad)
        if not es_valido:
            return False, None, mensaje
        
        # Validación 3: Secuencia de fechas
        es_valido, mensaje = self.validator.validar_secuencia_fechas(
            lote.fecha_cosecha, fecha_lavado.date(), fecha_empaquetado.date(), fecha_empaquetado.date()
        )
        if not es_valido:
            return False, None, mensaje
        
        # Si todas las validaciones pasan, crear la transformación
        try:
            transformacion = self.repository.crear_transformacion(
                lote=lote,
                proceso_lavado=proceso_lavado,
                fecha_lavado=fecha_lavado,
                proceso_empaquetado=proceso_empaquetado,
                fecha_empaquetado=fecha_empaquetado,
                control_calidad=control_calidad,
                observaciones_calidad=observaciones_calidad
            )
            return True, transformacion, "Transformación registrada exitosamente"
        except Exception as e:
            return False, None, f"Error al registrar la transformación: {str(e)}"
    
    def obtener_transformaciones_por_lote(self, codigo_lote):
        """
        Obtiene todas las transformaciones de un lote.
        """
        lote = self.lote_repository.obtener_por_codigo(codigo_lote)
        if not lote:
            return False, None, f"El lote '{codigo_lote}' no existe"
        
        transformaciones = self.repository.obtener_por_lote(lote)
        return True, transformaciones, f"{len(transformaciones)} transformaciones encontradas"


class LogisticaService:
    """
    Servicio para la gestión de logística y transporte.
    """
    
    def __init__(self):
        self.repository = LogisticaRepository()
        self.lote_repository = LoteRepository()
        self.validator = TrazabilidadValidator()
    
    def registrar_logistica(self, codigo_lote, temperatura_transporte,
                           fecha_inicio_transporte, fecha_entrega_supermercado,
                           nombre_supermercado, direccion_supermercado, observaciones=None):
        """
        Registra información logística aplicando validaciones.
        """
        # Validación 1: Verificar que el lote existe
        lote = self.lote_repository.obtener_por_codigo(codigo_lote)
        if not lote:
            return False, None, f"El lote '{codigo_lote}' no existe"
        
        # Validación 2: Temperatura
        es_valido, mensaje = self.validator.validar_temperatura(temperatura_transporte)
        if not es_valido:
            return False, None, mensaje
        
        # Validación 3: Fecha de entrega debe ser posterior al inicio
        if fecha_inicio_transporte >= fecha_entrega_supermercado:
            return False, None, "La fecha de entrega debe ser posterior al inicio del transporte"
        
        # Si todas las validaciones pasan, crear el registro logístico
        try:
            logistica = self.repository.crear_logistica(
                lote=lote,
                temperatura_transporte=temperatura_transporte,
                fecha_inicio_transporte=fecha_inicio_transporte,
                fecha_entrega_supermercado=fecha_entrega_supermercado,
                nombre_supermercado=nombre_supermercado,
                direccion_supermercado=direccion_supermercado,
                observaciones=observaciones
            )
            
            # Retornar advertencia si la temperatura no es óptima
            if "ADVERTENCIA" in mensaje:
                return True, logistica, mensaje
            
            return True, logistica, "Logística registrada exitosamente"
        except Exception as e:
            return False, None, f"Error al registrar la logística: {str(e)}"
    
    def obtener_logistica_por_lote(self, codigo_lote):
        """
        Obtiene toda la información logística de un lote.
        """
        lote = self.lote_repository.obtener_por_codigo(codigo_lote)
        if not lote:
            return False, None, f"El lote '{codigo_lote}' no existe"
        
        logisticas = self.repository.obtener_por_lote(lote)
        return True, logisticas, f"{len(logisticas)} registros logísticos encontrados"


class TrazabilidadService:
    """
    Servicio principal de trazabilidad.
    Coordina la información completa de un lote desde origen hasta entrega.
    """
    
    def __init__(self):
        self.lote_repository = LoteRepository()
        self.transformacion_repository = TransformacionRepository()
        self.logistica_repository = LogisticaRepository()
    
    def obtener_trazabilidad_completa(self, codigo_lote):
        """
        Obtiene toda la trazabilidad de un lote:
        - Información de origen (lote)
        - Procesos de transformación
        - Información logística
        
        Retorna un diccionario con toda la información.
        """
        # Obtener el lote
        lote = self.lote_repository.obtener_por_codigo(codigo_lote)
        if not lote:
            return False, None, f"El lote '{codigo_lote}' no existe"
        
        # Obtener transformaciones
        transformaciones = self.transformacion_repository.obtener_por_lote(lote)
        
        # Obtener logística
        logisticas = self.logistica_repository.obtener_por_lote(lote)
        
        # Construir el diccionario de trazabilidad completa
        trazabilidad = {
            'lote': lote,
            'transformaciones': transformaciones,
            'logisticas': logisticas,
            'tiene_transformaciones': len(transformaciones) > 0,
            'tiene_logistica': len(logisticas) > 0,
            'estado_completo': len(transformaciones) > 0 and len(logisticas) > 0
        }
        
        return True, trazabilidad, "Trazabilidad obtenida exitosamente"
