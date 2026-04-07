# Guía de Automatización y Reporting (BI DevOps)

Este documento detalla la infraestructura necesaria para asegurar que el reporte de ventas se actualice sin intervención humana y el negocio reciba alertas proactivas.

## 1. Configuración del On-premises Data Gateway

Para conectar la base de datos local `sales_data.db` con el **Power BI Service (Nube)**:
1. **Instalar el Gateway**: Descargar e instalar el "Standard Gateway" en el servidor donde resida la base de datos.
2. **Registro**: Iniciar sesión con la cuenta corporativa de Power BI.
3. **Configuración de Origen**:
   - Tipo de origen: **File** o **ODBC** (dependiendo del conector usado).
   - Ruta: `\\Ruta\Al\Archivo\sql\sales_data.db`.
4. **Credenciales**: Usar credenciales de Windows o Auth2 según el entorno.

---

## 2. Programación del Refresco (Scheduled Refresh)

Configurar el intervalo de actualización en el Power BI Service:
- **Frecuencia**: Diaria.
- **Zona Horaria**: (UTC-04:00) Georgetown, La Paz, Manaus, San Juan (Aplica para R.D.).
- **Horarios Estratégicos**: 
  - 06:00 AM (Preparación para inicio de jornada).
  - 02:00 PM (Cierre parcial de mediodía).
  - 08:00 PM (Análisis final del día).

---

## 3. Alertas de Datos Automáticas (Data Driven Alerts)

Diseñar alertas basadas en los KPIs críticos definidos en DAX:

| Métrica | Condición | Frecuencia de Alerta | Acción |
| :--- | :--- | :--- | :--- |
| **Total Sales** | < $500,000 | Al menos cada 24h | Email a Gerente de Ventas |
| **Target Achievement** | > 100% | Inmediata | Notificación Push a Móvil (Celebración) |
| **Anomalía (Z-Score)** | > 3 | Inmediata | Ticket a Soporte Técnico (Auditoría) |

### Proceso de Configuración:
1. Fijar una **Tarjeta (Card)** o **Indicador (Gauge)** en un Dashboard (no en el informe).
2. Seleccionar el menú `...` (Más opciones) → `Manage alerts`.
3. Definir la regla y el umbral correspondiente.
