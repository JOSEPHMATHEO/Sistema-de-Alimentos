-- Script para insertar datos de ejemplo en el Sistema de Trazabilidad Alimentaria
-- CAPA DE DATOS: Población de datos iniciales para pruebas

-- Nota: Ejecutar este script DESPUÉS de ejecutar las migraciones de Django
-- Los nombres de tabla siguen la convención de Django

-- Insertar lotes de ejemplo
INSERT INTO lotes (codigo_lote, ubicacion_cultivo, fecha_cosecha, observaciones, fecha_registro)
VALUES 
    ('MANGO-2024-001', 'Parcela 5, Sector Norte, Piura', '2024-01-15', 'Primera cosecha de la temporada, calidad excepcional', NOW()),
    ('MANGO-2024-002', 'Parcela 12, Sector Este, Lambayeque', '2024-01-18', 'Mangos orgánicos certificados', NOW()),
    ('MANGO-2024-003', 'Parcela 8, Sector Sur, Piura', '2024-01-20', NULL, NOW());

-- Insertar transformaciones de ejemplo
INSERT INTO transformaciones (
    lote_id, 
    proceso_lavado, 
    fecha_lavado, 
    proceso_empaquetado, 
    fecha_empaquetado, 
    control_calidad, 
    observaciones_calidad, 
    fecha_registro
)
SELECT 
    l.id,
    'Lavado con agua potable a presión controlada, desinfección con solución de hipoclorito de sodio 50ppm por 2 minutos',
    '2024-01-16 08:30:00',
    'Empaquetado en cajas de cartón corrugado de 5kg, con separadores individuales y papel parafinado',
    '2024-01-16 10:00:00',
    'APROBADO',
    'Control de calidad aprobado. Mangos sin defectos, tamaño uniforme, madurez óptima',
    NOW()
FROM lotes l
WHERE l.codigo_lote = 'MANGO-2024-001';

INSERT INTO transformaciones (
    lote_id, 
    proceso_lavado, 
    fecha_lavado, 
    proceso_empaquetado, 
    fecha_empaquetado, 
    control_calidad, 
    observaciones_calidad, 
    fecha_registro
)
SELECT 
    l.id,
    'Lavado automático con sistema de aspersión, desinfección orgánica con agua ozonizada',
    '2024-01-19 07:00:00',
    'Empaquetado en cajas biodegradables de 4kg con etiqueta de certificación orgánica',
    '2024-01-19 09:30:00',
    'APROBADO',
    'Certificación orgánica verificada. Producto cumple todos los estándares',
    NOW()
FROM lotes l
WHERE l.codigo_lote = 'MANGO-2024-002';

-- Insertar registros logísticos de ejemplo
INSERT INTO logisticas (
    lote_id,
    temperatura_transporte,
    fecha_inicio_transporte,
    fecha_entrega_supermercado,
    nombre_supermercado,
    direccion_supermercado,
    observaciones,
    fecha_registro
)
SELECT 
    l.id,
    8.5,
    '2024-01-16 14:00:00',
    '2024-01-17 08:00:00',
    'Supermercados Metro - Miraflores',
    'Av. Benavides 1555, Miraflores, Lima',
    'Transporte en cámara refrigerada, temperatura controlada durante todo el trayecto',
    NOW()
FROM lotes l
WHERE l.codigo_lote = 'MANGO-2024-001';

INSERT INTO logisticas (
    lote_id,
    temperatura_transporte,
    fecha_inicio_transporte,
    fecha_entrega_supermercado,
    nombre_supermercado,
    direccion_supermercado,
    observaciones,
    fecha_registro
)
SELECT 
    l.id,
    9.2,
    '2024-01-19 12:00:00',
    '2024-01-20 07:30:00',
    'Plaza Vea - San Isidro',
    'Av. Javier Prado Este 1234, San Isidro, Lima',
    'Producto orgánico certificado, entrega nocturna para mantener cadena de frío',
    NOW()
FROM lotes l
WHERE l.codigo_lote = 'MANGO-2024-002';

-- Verificación de datos insertados
SELECT 
    'Datos de ejemplo insertados correctamente' AS status,
    (SELECT COUNT(*) FROM lotes) AS total_lotes,
    (SELECT COUNT(*) FROM transformaciones) AS total_transformaciones,
    (SELECT COUNT(*) FROM logisticas) AS total_logisticas;
