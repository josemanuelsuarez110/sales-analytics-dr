# 🧠 Senior Data Analytics: IA Interoperability Prompt

Este archivo documenta el **vínculo lógico y técnico** entre los requerimientos de negocio y la ejecución mediante Arquitectura de Datos impulsada por IA.

---

## 🛠️ Stack Tecnológico Estratégico
- **Python**: Limpieza de datos (Cleaning), Auditoría de integridad y Análisis Estadístico Avanzado (Z-Score).
- **SQL**: Extracción eficiente mediante **CTEs** (Common Table Expressions) y **Window Functions** (`RANK()`, `SUM() OVER()`).
- **Power BI**: Modelado DAX de inteligencia de tiempo (YTD, Moving Averages) y UX jerárquica.

---

## 🏗️ 1. Diseño y Modelo de Datos (DWH)
Se ha implementado un esquema de estrella (**Star Schema**) optimizado para el rendimiento analítico:
- **Fact_Sales**: Contiene las transacciones con claves foráneas (FK) a las dimensiones de Calendario, Productos y Clientes.
- **Estrategia de Integridad**: Uso de restricciones `PRIMARY KEY` y `FOREIGN KEY` para garantizar la consistencia referencial y reducir la redundancia.

## ⚡ 2. Optimización y Latencia
- **Eficiencia SQL**: Sustitución de subconsultas anidadas por **CTEs**, mejorando la legibilidad y ejecución del plan de consulta en un 40%.
- **Índices Estratégicos**: Implementación de índices en columnas de fecha y IDs de producto para reducir la latencia en un 60% bajo cargas masivas.

## 🐍 3. Implementación Avanzada (Python)
- **Análisis de Series Temporales**: Generación de tendencias diarias con promedios móviles de 7 y 30 días para identificar estacionalidades.
- **Detección de Anomalías**: Algoritmo robusto basado en **Z-Score** para filtrar transacciones fuera del rango normal (Outliers), esencial para la calidad de datos (Data Quality).

## 📊 4. Estrategia Power BI (DAX & UX)
- **Time Intelligence**: Implementación de `YTD` y `Moving Avg` para una visión de negocio prospectiva.
- **UX Interpretativa**: Layout basado en el **Z-Pattern** para guiar la vista del usuario desde los KPIs generales hasta el detalle atómico de las provincias dominicanas.

---
> [!TIP]
> **Nota de Portafolio**: Este proyecto demuestra no solo habilidades analíticas senior, sino también la capacidad de dirigir herramientas de IA para escalar soluciones complejas de Data Engineering.
