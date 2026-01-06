"""
CAPA DE DATOS - Modelos
Define la estructura de las tablas en la base de datos PostgreSQL.
Cada modelo representa una entidad del sistema de trazabilidad.
"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Lote(models.Model):
    """
    Modelo para ORIGEN del producto agrícola.
    Representa la información de cosecha y ubicación del cultivo.
    """
    # Código único del lote
    codigo_lote = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Código del Lote",
        help_text="Código único de identificación del lote"
    )
    
    # Ubicación geográfica del cultivo
    ubicacion_cultivo = models.CharField(
        max_length=200,
        verbose_name="Ubicación del Cultivo",
        help_text="Dirección o coordenadas del cultivo"
    )
    
    # Fecha en que se realizó la cosecha
    fecha_cosecha = models.DateField(
        verbose_name="Fecha de Cosecha",
        help_text="Fecha en que se cosechó el lote"
    )
    
    # Información adicional (opcional)
    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones",
        help_text="Información adicional sobre el lote"
    )
    
    # Metadatos
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Registro"
    )
    
    class Meta:
        db_table = 'lotes'
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
        ordering = ['-fecha_cosecha']
    
    def __str__(self):
        return f"Lote {self.codigo_lote}"


class Transformacion(models.Model):
    """
    Modelo para TRANSFORMACIÓN del producto.
    Registra los procesos de lavado, empaquetado y control de calidad.
    """
    # Opciones para el estado de control de calidad
    ESTADO_CALIDAD_CHOICES = [
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
    ]
    
    # Relación con el lote (un lote puede tener múltiples transformaciones)
    lote = models.ForeignKey(
        Lote,
        on_delete=models.CASCADE,
        related_name='transformaciones',
        verbose_name="Lote"
    )
    
    # Información del proceso de lavado
    proceso_lavado = models.TextField(
        verbose_name="Proceso de Lavado",
        help_text="Descripción del proceso de lavado aplicado"
    )
    
    # Fecha del proceso de lavado
    fecha_lavado = models.DateTimeField(
        verbose_name="Fecha de Lavado"
    )
    
    # Información del proceso de empaquetado
    proceso_empaquetado = models.TextField(
        verbose_name="Proceso de Empaquetado",
        help_text="Descripción del proceso de empaquetado"
    )
    
    # Fecha del proceso de empaquetado
    fecha_empaquetado = models.DateTimeField(
        verbose_name="Fecha de Empaquetado"
    )
    
    # Control de calidad: APROBADO o RECHAZADO
    control_calidad = models.CharField(
        max_length=20,
        choices=ESTADO_CALIDAD_CHOICES,
        verbose_name="Control de Calidad",
        help_text="Resultado del control de calidad"
    )
    
    # Observaciones del control de calidad
    observaciones_calidad = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones de Calidad"
    )
    
    # Metadatos
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Registro"
    )
    
    class Meta:
        db_table = 'transformaciones'
        verbose_name = 'Transformación'
        verbose_name_plural = 'Transformaciones'
        ordering = ['-fecha_empaquetado']
    
    def __str__(self):
        return f"Transformación de {self.lote.codigo_lote} - {self.control_calidad}"


class Logistica(models.Model):
    """
    Modelo para LOGÍSTICA y transporte del producto.
    Registra la temperatura durante el transporte y la fecha de entrega.
    """
    # Relación con el lote
    lote = models.ForeignKey(
        Lote,
        on_delete=models.CASCADE,
        related_name='logisticas',
        verbose_name="Lote"
    )
    
    # Temperatura registrada durante el transporte (en grados Celsius)
    temperatura_transporte = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(-20), MaxValueValidator(50)],
        verbose_name="Temperatura de Transporte (°C)",
        help_text="Temperatura promedio durante el transporte"
    )
    
    # Fecha y hora de inicio del transporte
    fecha_inicio_transporte = models.DateTimeField(
        verbose_name="Fecha de Inicio de Transporte"
    )
    
    # Fecha y hora de entrega al supermercado
    fecha_entrega_supermercado = models.DateTimeField(
        verbose_name="Fecha de Entrega al Supermercado"
    )
    
    # Nombre del supermercado de destino
    nombre_supermercado = models.CharField(
        max_length=200,
        verbose_name="Nombre del Supermercado",
        help_text="Nombre del supermercado de destino"
    )
    
    # Dirección del supermercado
    direccion_supermercado = models.CharField(
        max_length=300,
        verbose_name="Dirección del Supermercado"
    )
    
    # Observaciones del transporte
    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaciones"
    )
    
    # Metadatos
    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Registro"
    )
    
    class Meta:
        db_table = 'logisticas'
        verbose_name = 'Logística'
        verbose_name_plural = 'Logísticas'
        ordering = ['-fecha_entrega_supermercado']
    
    def __str__(self):
        return f"Logística de {self.lote.codigo_lote} - {self.nombre_supermercado}"
