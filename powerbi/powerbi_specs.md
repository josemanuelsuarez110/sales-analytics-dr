# Power BI Strategy: Analytics Architect (Senior Level)

Este documento detalla la implementación lógica y visual para maximizar la interpretabilidad de los datos, siguiendo patrones de diseño **Z-Pattern** y **F-Pattern**.

## 1. Medidas DAX Críticas (Advanced Logic)

### Time Intelligence: YTD (Year-to-Date)
Calcula el acumulado de ventas desde el inicio del año actual hasta la fecha seleccionada.
```dax
Sales YTD = TOTALYTD([Total Sales], 'Dim_Calendario'[Date])
```

### Análisis de Tendencia: Moving Average (3 Meses)
Suaviza las fluctuaciones estacionales para identificar la tendencia real de crecimiento.
```dax
Moving Avg 3M = 
AVERAGEX(
    DATESINPERIOD('Dim_Calendario'[Date], MAX('Dim_Calendario'[Date]), -3, MONTH),
    [Total Sales]
)
```

### Rendimiento: % vs Q Prev (Análisis Intertrimestral)
Métrica clave para evaluar el momentum del negocio.
```dax
QoQ Growth % = 
VAR PreviousQuarterSales = CALCULATE([Total Sales], PREVIOUSQUARTER('Dim_Calendario'[Date]))
RETURN
DIVIDE([Total Sales] - PreviousQuarterSales, PreviousQuarterSales, 0)
```

---

## 2. Layout & UX (Arquitectura de Pantalla)

### Estructura de "Navegación Dinámica"
*   **Sección Superior (Banner de KPIs)**: Visualización inmediata de 4 tarjetas glassmorphism (Sales, Orders, YTD, YoY).
*   **Sección Central (Análisis de Momentum)**: Gráfico de áreas comparando `Total Sales` vs `Moving Avg 3M`.
*   **Sección Inferior (Desglose Atómico)**: Mapa de calor de provincias dominicanas y tabla resumida con formato condicional.

### Interpretación de Anomalías
*   Integra un **Highlight Visual** (Borde rojo o Icono de alerta) en las tablas de transacciones cuando `Z-Score > 3`, permitiendo al usuario identificar errores de facturación o picos de demanda inusuales de forma instantánea.

## 3. Paleta de Colores Estratégica
- **Primary**: #0891B2 (Cyan Profundo - Confianza/Estabilidad)
- **Secondary**: #F59E0B (Ámbar - Alertas de Anomalías)
- **Background**: #F8FAFC (Gris Azulado muy claro - Limpieza Visual)
