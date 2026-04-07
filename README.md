# 📊 Senior Sales Analytics: República Dominicana (DWH & BI)

Proyecto de **Arquitectura de Datos y Analítica Avanzada** diseñado para la toma de decisiones estratégicas, integrando un Data Warehouse (DWH) robusto, detección de anomalías y visualización predictiva.

## 🏗️ Arquitectura del Sistema
Este proyecto implementa una infraestructura de datos de nivel empresarial (**Senior Level**):

### 🔄 Flujo de Datos Automatizado
```text
  [ FUENTES ]        [ ORQUESTACIÓN ]       [ DATA WAREHOUSE ]      [ REPORTING ]
  CSV / Excel  ──▶   Python (ETL)    ──▶   SQL (Staging/DW)   ──▶   Power BI 
  APIs / Logs  ──▶   Data Quality    ──▶   Incremental Load   ──▶   Gateways / Alertas
```

- **Capa ETL (Python Automation)**: Orquestador dinámico con **Logging profesional** y validación de calidad de datos.
- **Modelado DWH (Star Schema)**: Diseño optimizado con **Carga Incremental** e integridad referencial.
- **Analítica Avanzada**: Motor de detección de **anomalías (Outliers)** mediante **Z-Score** estadístico.
- **Consultas Optimistas**: Uso de **CTEs** y **Window Functions** para análisis estratégico.

## 🚀 Tecnologías Senior
- **Python**: Pandas, NumPy, SQLAlchemy (Pipeline & Anomaly Detection).
- **Escalabilidad SQL**: Estructura de tablas normalizadas y lógica de agregación avanzada.
- **BI Strategy**: Inteligencia de tiempo (YTD, Moving Averages 3M) y UX de alto impacto.

## 📁 Estructura del Repositorio
```bash
├── etl/
│   ├── etl_sales.py          # Extracción, Limpieza y Carga (ETL)
│   └── advanced_analytics.py   # Detección de anomalías y Series Temporales
├── people_analytics/         # NUEVO: Análisis de Capital Humano
│   ├── etl/
│   │   └── flight_risk_analysis.py # Predicción de Riesgo de Fuga
│   ├── sql/
│   │   └── hr_schema_setup.sql     # DWH de RRHH (Anonimizado)
│   └── powerbi/
│       └── hr_bi_specs.md          # Métricas de Talento (9-Box Grid)
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

## 📑 Ética de Datos y Privacidad (People Analytics)
Como **Especialista en People Analytics**, la integridad y privacidad son pilares innegociables:
- **Anonimización**: Se han eliminado identificadores personales (nombres, DNIs) sustituyéndolos por IDs únicos para el análisis masivo.
- **Cumplimiento**: El diseño de este ecosistema sigue principios de **GDPR** y leyes locales de protección de datos, asegurando que el análisis de desempeño sea justo, transparente y basado únicamente en méritos objetivos.

---
*Desarrollado con un enfoque en **optimización de procesos**, **ética de datos** y **escalabilidad estratégica**.*
