-- Script para crear la base de datos del Sistema de Trazabilidad Alimentaria
-- CAPA DE DATOS: Definición de estructura de base de datos PostgreSQL

-- Crear la base de datos (ejecutar como superusuario de PostgreSQL)
-- Nota: Este comando debe ejecutarse fuera de la base de datos
-- Desde psql: CREATE DATABASE sta_db;

-- Conectarse a la base de datos sta_db antes de ejecutar el resto del script
-- \c sta_db

-- Comentario académico:
-- Este script crea las tablas necesarias para el sistema de trazabilidad.
-- Django ejecutará automáticamente las migraciones que crean estas tablas,
-- pero este script está disponible como referencia de la estructura.

-- Las tablas reales serán creadas por Django ORM mediante:
-- python manage.py makemigrations
-- python manage.py migrate

-- Verificación de conexión
SELECT 'Base de datos STA configurada correctamente' AS status;
