# 📊 Senior Sales Analytics: República Dominicana (DWH & BI)

Proyecto de **Arquitectura de Datos y Analítica Avanzada** diseñado para la toma de decisiones estratégicas, integrando un Data Warehouse (DWH) robusto, detección de anomalías y visualización predictiva.

## 🏗️ Arquitectura del Sistema
Este proyecto implementa una infraestructura de datos de nivel empresarial (**Lead Architect Level**):

### 🔄 System Architecture (Data Pipeline)
```text
  [ SOURCES ]         [ PYTHON ETL ]         [ SQL DWH ]          [ POWER BI ]
  APIs Region A ──▶   Ingesta (Upsert)  ──▶   Capa Bronze  ──▶   Capa Semántica
  ERPs Region B ──▶   Schema Validator  ──▶   Capa Silver  ──▶   RLS / DAX WoW
  CSV / Excels  ──▶   Perform. Logging  ──▶   Capa Gold    ──▶   Inc. Refresh
```

- **Pipeline Architect (Python)**: Orquestador modular con lógica de **Upsert inteligente** y registro de latencia por fuente.
- **Medallion Architecture (SQL)**: Estructura Bronze, Silver y Gold para consolidación multimoneda (DOP, USD, EUR, MXN, CAD).
- **Analítica Predictiva**: Motor de detección de **anomalías (Outliers)** mediante **Z-Score** estadístico.
- **Consultas Optimistas**: Uso de **CTEs**, **Window Functions** e índices de alto rendimiento.

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

## 🛠️ Manejo de Errores y Autocuración
El ecosistema de automatización corporativo cuenta con mecanismos de **High Availability (HA)**:
- **Reintentos (Retries)**: El orquestador Python reintenta la conexión hasta 3 veces antes de disparar un error fatal.
- **Logs de Auditoría**: Cada carga registra el éxito o fallo en `pipeline_execution.log`.
- **Integridad Transaccional**: Las transformaciones SQL se ejecutan bajo lógica transaccional, evitando que fallos de red dejen datos inconsistentes en las capas finales.

---
*Desarrollado con un enfoque en **arquitectura de datos empresarial**, **optimización masiva** y **gobernanza estratégica**.*
