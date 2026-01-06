"""
CAPA DE LÓGICA DE NEGOCIO - Validadores
Contiene las reglas de validación del negocio.
Valida que los datos cumplan con los requisitos de trazabilidad.
"""
from datetime import datetime, date
from decimal import Decimal


class TrazabilidadValidator:
    """
    Validador para reglas de negocio de trazabilidad.
    Asegura que los datos cumplan con los estándares de calidad.
    """
    
    @staticmethod
    def validar_codigo_lote(codigo_lote):
        """
        Valida el formato del código de lote.
        Reglas:
        - No puede estar vacío
        - Debe tener entre 3 y 50 caracteres
        - Debe ser alfanumérico
        """
        if not codigo_lote or len(codigo_lote.strip()) == 0:
            return False, "El código de lote no puede estar vacío"
        
        if len(codigo_lote) < 3:
            return False, "El código de lote debe tener al menos 3 caracteres"
        
        if len(codigo_lote) > 50:
            return False, "El código de lote no puede exceder 50 caracteres"
        
        return True, "Código válido"
    
    @staticmethod
    def validar_fecha_cosecha(fecha_cosecha):
        """
        Valida que la fecha de cosecha sea lógica.
        Reglas:
        - No puede ser futura
        - No puede ser anterior a 1 año
        """
        if isinstance(fecha_cosecha, str):
            try:
                fecha_cosecha = datetime.strptime(fecha_cosecha, '%Y-%m-%d').date()
            except ValueError:
                return False, "Formato de fecha inválido. Use YYYY-MM-DD"
        
        hoy = date.today()
        
        if fecha_cosecha > hoy:
            return False, "La fecha de cosecha no puede ser futura"
        
        # Verificar que no sea más de 1 año en el pasado
        dias_diferencia = (hoy - fecha_cosecha).days
        if dias_diferencia > 365:
            return False, "La fecha de cosecha no puede ser mayor a 1 año"
        
        return True, "Fecha válida"
    
    @staticmethod
    def validar_control_calidad(control_calidad):
        """
        Valida el estado de control de calidad.
        Debe ser APROBADO o RECHAZADO.
        """
        estados_validos = ['APROBADO', 'RECHAZADO']
        if control_calidad not in estados_validos:
            return False, f"El control de calidad debe ser: {', '.join(estados_validos)}"
        return True, "Control de calidad válido"
    
    @staticmethod
    def validar_temperatura(temperatura):
        """
        Valida que la temperatura esté en un rango razonable.
        Reglas:
        - Debe estar entre -20°C y 50°C
        - Para productos perecederos, idealmente entre 0°C y 15°C
        """
        try:
            temp = float(temperatura)
        except (ValueError, TypeError):
            return False, "La temperatura debe ser un número válido"
        
        if temp < -20 or temp > 50:
            return False, "La temperatura debe estar entre -20°C y 50°C"
        
        # Advertencia para temperaturas fuera del rango óptimo
        if temp < 0 or temp > 15:
            return True, "ADVERTENCIA: Temperatura fuera del rango óptimo (0-15°C)"
        
        return True, "Temperatura válida"
    
    @staticmethod
    def validar_secuencia_fechas(fecha_cosecha, fecha_lavado, fecha_empaquetado, fecha_entrega):
        """
        Valida que las fechas sigan una secuencia lógica.
        Regla: cosecha < lavado < empaquetado < entrega
        """
        if fecha_cosecha >= fecha_lavado:
            return False, "La fecha de lavado debe ser posterior a la cosecha"
        
        if fecha_lavado >= fecha_empaquetado:
            return False, "La fecha de empaquetado debe ser posterior al lavado"
        
        if fecha_empaquetado >= fecha_entrega:
            return False, "La fecha de entrega debe ser posterior al empaquetado"
        
        return True, "Secuencia de fechas válida"
