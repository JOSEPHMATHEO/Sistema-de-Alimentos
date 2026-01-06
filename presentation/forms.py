"""
CAPA DE PRESENTACIÓN - Formularios
Define los formularios web para captura de datos del usuario.
Usa Django Forms para validación de entrada.
"""
from django import forms
from data.models import Lote, Transformacion, Logistica


class LoteForm(forms.ModelForm):
    """
    Formulario para registro de lotes (ORIGEN).
    """
    class Meta:
        model = Lote
        fields = ['codigo_lote', 'ubicacion_cultivo', 'fecha_cosecha', 'observaciones']
        widgets = {
            'codigo_lote': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: MANGO-2024-001'
            }),
            'ubicacion_cultivo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Parcela 5, Sector Norte'
            }),
            'fecha_cosecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales (opcional)'
            }),
        }


class TransformacionForm(forms.ModelForm):
    """
    Formulario para registro de transformación.
    """
    codigo_lote = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Código del lote'
        }),
        label='Código del Lote'
    )
    
    class Meta:
        model = Transformacion
        fields = ['proceso_lavado', 'fecha_lavado', 'proceso_empaquetado', 
                 'fecha_empaquetado', 'control_calidad', 'observaciones_calidad']
        widgets = {
            'proceso_lavado': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del proceso de lavado'
            }),
            'fecha_lavado': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'proceso_empaquetado': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción del proceso de empaquetado'
            }),
            'fecha_empaquetado': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'control_calidad': forms.Select(attrs={
                'class': 'form-control'
            }),
            'observaciones_calidad': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Observaciones del control de calidad (opcional)'
            }),
        }


class LogisticaForm(forms.ModelForm):
    """
    Formulario para registro de logística.
    """
    codigo_lote = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Código del lote'
        }),
        label='Código del Lote'
    )
    
    class Meta:
        model = Logistica
        fields = ['temperatura_transporte', 'fecha_inicio_transporte', 
                 'fecha_entrega_supermercado', 'nombre_supermercado',
                 'direccion_supermercado', 'observaciones']
        widgets = {
            'temperatura_transporte': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Ej: 8.5'
            }),
            'fecha_inicio_transporte': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'fecha_entrega_supermercado': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'nombre_supermercado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Supermercado Central'
            }),
            'direccion_supermercado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Av. Principal 123'
            }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Observaciones del transporte (opcional)'
            }),
        }


class ConsultaTrazabilidadForm(forms.Form):
    """
    Formulario para consultar la trazabilidad de un lote.
    """
    codigo_lote = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el código del lote'
        }),
        label='Código del Lote'
    )
