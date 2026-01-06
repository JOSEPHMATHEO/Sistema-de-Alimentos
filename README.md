# Sistema de Trazabilidad Alimentaria (STA)
## Cooperativa Agrícola - Mangos Orgánicos

### 📋 Descripción del Proyecto
Sistema de trazabilidad completo que permite rastrear productos agrícolas desde la cosecha hasta la entrega en el supermercado, cumpliendo con estándares de control y seguimiento.

### 🏗️ Arquitectura de 3 Capas Estricta

**CAPA 1: PRESENTACIÓN** (carpeta `presentation/`)
- Responsabilidad: Interfaz de usuario y manejo de peticiones HTTP
- Componentes: Views, Templates, Forms
- Tecnologías: Django Views, HTML, CSS (Bootstrap), JavaScript

**CAPA 2: LÓGICA DE NEGOCIO** (carpeta `business/`)
- Responsabilidad: Validaciones, reglas de negocio, coordinación
- Componentes: Services, Validators, Business Rules
- Tecnologías: Python (clases de servicio puras)

**CAPA 3: DATOS** (carpeta `data/`)
- Responsabilidad: Persistencia y acceso a datos
- Componentes: Models, Repositories, Database Access
- Tecnologías: Django ORM, PostgreSQL

### 📦 Estructura del Proyecto

```
sta_project/
├── manage.py                          # Script de gestión de Django
├── requirements.txt                   # Dependencias del proyecto
├── sta_project/                       # Configuración principal
│   ├── __init__.py
│   ├── settings.py                    # Configuración de Django
│   ├── urls.py                        # URLs principales
│   └── wsgi.py
├── data/                              # CAPA DE DATOS
│   ├── __init__.py
│   ├── models.py                      # Modelos de base de datos
│   └── repositories.py                # Repositorios para acceso a datos
├── business/                          # CAPA DE LÓGICA DE NEGOCIO
│   ├── __init__.py
│   ├── services.py                    # Servicios de negocio
│   └── validators.py                  # Validadores de reglas de negocio
└── presentation/                      # CAPA DE PRESENTACIÓN
    ├── __init__.py
    ├── views.py                       # Controladores de vistas
    ├── forms.py                       # Formularios
    ├── urls.py                        # URLs de la aplicación
    └── templates/                     # Plantillas HTML
        ├── base.html
        ├── index.html
        ├── lote_form.html
        ├── transformacion_form.html
        ├── logistica_form.html
        └── trazabilidad_consulta.html
```

### 🚀 Instalación y Configuración

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Configurar PostgreSQL:**
   - Crear base de datos: `CREATE DATABASE sta_db;`
   - Actualizar credenciales en `settings.py`

3. **Ejecutar migraciones:**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Crear superusuario (opcional):**
```bash
python manage.py createsuperuser
```

5. **Ejecutar servidor:**
```bash
python manage.py runserver
```

6. **Acceder al sistema:**
   - URL: http://localhost:8000/

### 📊 Funcionalidades Principales

1. **Gestión de Lotes**
   - Registro de código de lote
   - Ubicación del cultivo
   - Fecha de cosecha

2. **Gestión de Transformación**
   - Registro de proceso de lavado
   - Registro de proceso de empaquetado
   - Control de calidad (aprobado/rechazado)

3. **Gestión de Logística**
   - Registro de temperatura de transporte
   - Fecha de entrega al supermercado

### 🔍 Consulta de Trazabilidad

El sistema permite consultar toda la trazabilidad de un lote específico, mostrando:
- Información de origen
- Procesos de transformación aplicados
- Información logística

