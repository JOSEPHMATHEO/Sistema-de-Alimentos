"""
CAPA DE PRESENTACIÓN - Vistas
Controladores que manejan las peticiones HTTP y coordinan con la capa de negocio.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from business.services import (
    LoteService, TransformacionService, 
    LogisticaService, TrazabilidadService
)
from .forms import (
    LoteForm, TransformacionForm, 
    LogisticaForm, ConsultaTrazabilidadForm
)


def index(request):
    """
    Vista principal del sistema.
    Muestra el menú de opciones disponibles.
    """
    # Obtener estadísticas generales
    lote_service = LoteService()
    exito, lotes, _ = lote_service.listar_todos_lotes()
    
    context = {
        'total_lotes': len(lotes) if exito else 0
    }
    return render(request, 'index.html', context)


def registrar_lote(request):
    """
    Vista para registrar un nuevo lote (ORIGEN).
    Interactúa con LoteService de la capa de negocio.
    """
    if request.method == 'POST':
        form = LoteForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            codigo_lote = form.cleaned_data['codigo_lote']
            ubicacion_cultivo = form.cleaned_data['ubicacion_cultivo']
            fecha_cosecha = form.cleaned_data['fecha_cosecha']
            observaciones = form.cleaned_data.get('observaciones')
            
            # Llamar al servicio de la capa de negocio
            lote_service = LoteService()
            exito, lote, mensaje = lote_service.registrar_lote(
                codigo_lote=codigo_lote,
                ubicacion_cultivo=ubicacion_cultivo,
                fecha_cosecha=fecha_cosecha,
                observaciones=observaciones
            )
            
            if exito:
                messages.success(request, mensaje)
                return redirect('index')
            else:
                messages.error(request, mensaje)
    else:
        form = LoteForm()
    
    return render(request, 'lote_form.html', {'form': form})


def registrar_transformacion(request):
    """
    Vista para registrar una transformación.
    Interactúa con TransformacionService de la capa de negocio.
    """
    if request.method == 'POST':
        form = TransformacionForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            codigo_lote = form.cleaned_data['codigo_lote']
            proceso_lavado = form.cleaned_data['proceso_lavado']
            fecha_lavado = form.cleaned_data['fecha_lavado']
            proceso_empaquetado = form.cleaned_data['proceso_empaquetado']
            fecha_empaquetado = form.cleaned_data['fecha_empaquetado']
            control_calidad = form.cleaned_data['control_calidad']
            observaciones_calidad = form.cleaned_data.get('observaciones_calidad')
            
            # Llamar al servicio de la capa de negocio
            transformacion_service = TransformacionService()
            exito, transformacion, mensaje = transformacion_service.registrar_transformacion(
                codigo_lote=codigo_lote,
                proceso_lavado=proceso_lavado,
                fecha_lavado=fecha_lavado,
                proceso_empaquetado=proceso_empaquetado,
                fecha_empaquetado=fecha_empaquetado,
                control_calidad=control_calidad,
                observaciones_calidad=observaciones_calidad
            )
            
            if exito:
                messages.success(request, mensaje)
                return redirect('index')
            else:
                messages.error(request, mensaje)
    else:
        form = TransformacionForm()
    
    return render(request, 'transformacion_form.html', {'form': form})


def registrar_logistica(request):
    """
    Vista para registrar información logística.
    Interactúa con LogisticaService de la capa de negocio.
    """
    if request.method == 'POST':
        form = LogisticaForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            codigo_lote = form.cleaned_data['codigo_lote']
            temperatura_transporte = form.cleaned_data['temperatura_transporte']
            fecha_inicio_transporte = form.cleaned_data['fecha_inicio_transporte']
            fecha_entrega_supermercado = form.cleaned_data['fecha_entrega_supermercado']
            nombre_supermercado = form.cleaned_data['nombre_supermercado']
            direccion_supermercado = form.cleaned_data['direccion_supermercado']
            observaciones = form.cleaned_data.get('observaciones')
            
            # Llamar al servicio de la capa de negocio
            logistica_service = LogisticaService()
            exito, logistica, mensaje = logistica_service.registrar_logistica(
                codigo_lote=codigo_lote,
                temperatura_transporte=temperatura_transporte,
                fecha_inicio_transporte=fecha_inicio_transporte,
                fecha_entrega_supermercado=fecha_entrega_supermercado,
                nombre_supermercado=nombre_supermercado,
                direccion_supermercado=direccion_supermercado,
                observaciones=observaciones
            )
            
            if exito:
                # Mostrar mensaje de éxito (puede incluir advertencias)
                if "ADVERTENCIA" in mensaje:
                    messages.warning(request, mensaje)
                else:
                    messages.success(request, mensaje)
                return redirect('index')
            else:
                messages.error(request, mensaje)
    else:
        form = LogisticaForm()
    
    return render(request, 'logistica_form.html', {'form': form})


def consultar_trazabilidad(request):
    """
    Vista para consultar la trazabilidad completa de un lote.
    Interactúa con TrazabilidadService de la capa de negocio.
    """
    trazabilidad = None
    
    if request.method == 'POST':
        form = ConsultaTrazabilidadForm(request.POST)
        if form.is_valid():
            codigo_lote = form.cleaned_data['codigo_lote']
            
            # Llamar al servicio de trazabilidad
            trazabilidad_service = TrazabilidadService()
            exito, trazabilidad, mensaje = trazabilidad_service.obtener_trazabilidad_completa(codigo_lote)
            
            if not exito:
                messages.error(request, mensaje)
                trazabilidad = None
    else:
        form = ConsultaTrazabilidadForm()
    
    return render(request, 'trazabilidad_consulta.html', {
        'form': form,
        'trazabilidad': trazabilidad
    })
