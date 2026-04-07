# 📊 Senior Sales Analytics: República Dominicana (DWH & BI)

Proyecto de **Arquitectura de Datos y Analítica Avanzada** diseñado para la toma de decisiones estratégicas, integrando un Data Warehouse (DWH) robusto, detección de anomalías y visualización predictiva.

## 🏗️ Arquitectura del Sistema
Este proyecto implementa una infraestructura de datos de nivel empresarial (**Senior Level**):
- **Capa ETL (Python)**: Generación de **2,500 registros** sintéticos localizados en la República Dominicana, limpieza automatizada y carga eficiente.
- **Modelado DWH (Star Schema)**: Diseño optimizado con claves primarias/foráneas e índices para reducción de latencia.
- **Analítica Avanzada**: Motor de detección de **anomalías (Outliers)** mediante **Z-Score** estadístico.
- **Consultas Optimistas**: Uso de **CTEs** y **Window Functions** para análisis de **Pareto (80/20)** y Rankings mensuales.

## 🚀 Tecnologías Senior
- **Python**: Pandas, NumPy, SQLAlchemy (Pipeline & Anomaly Detection).
- **Escalabilidad SQL**: Estructura de tablas normalizadas y lógica de agregación avanzada.
- **BI Strategy**: Inteligencia de tiempo (YTD, Moving Averages 3M) y UX de alto impacto.

## 📁 Estructura del Repositorio
```bash
├── etl/
│   ├── etl_sales.py          # Extracción, Limpieza y Carga (ETL)
│   └── advanced_analytics.py   # Detección de anomalías y Series Temporales
├── sql/
│   ├── star_schema_setup.sql   # DWH: Esquema en Estrella (PK/FK, Indices)
│   ├── optimized_queries.sql   # Analítica SQL (CTEs, Window Functions)
│   └── sales_data.db           # Almacén de Datos (SQLite DWH)
├── powerbi/
│   └── powerbi_specs.md      # Estrategia DAX & UX Senior
├── PROMPT.md                 # Documentación de Arquitectura e IA
└── README.md                 # Visión General Profesional
```

## 📊 Medidas DAX Críticas
- **Sales YTD**: `TOTALYTD([Total Sales], 'Dim_Calendario'[Date])`
- **Moving Avg 3M**: Suavizado de tendencias temporales.
- **QoQ Growth**: Análisis dinámico intertrimestral.

---
*Desarrollado con un enfoque en **optimización de procesos**, **latencia cero** y **escalabilidad analítica**.*
