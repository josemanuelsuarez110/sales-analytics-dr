# 🚀 Master Data Solutions Platform: Full-Stack Architect

Proyecto de **Arquitectura de Datos y Analítica Avanzada** diseñado para la toma de decisiones estratégicas, integrando un Data Warehouse (DWH) robusto, detección de anomalías y visualización predictiva.

## 🏗️ Arquitectura del Sistema (Full-Stack)
Este ecosistema integra todo el ciclo de vida del dato bajo una infraestructura de **Arquitecto de Soluciones**:

### 🔄 Integrated Data Journey
```text
  [ SOURCES ]       [ PIPELINE / ETL ]       [ DWH (Medallion) ]      [ PRESENTATION ]
  APIs Global  ──▶   Master Orchestrator ──▶   Layer Bronze    ──▶   Next.js Dash
  HRIS Talent  ──▶   Data Quality (PD)   ──▶   Layer Silver    ──▶   Recharts / UX
  Open Data RD ──▶   Predictive Models   ──▶   Layer Gold      ──▶   Vercel Cloud
```

- **Master Orchestration (Python)**: Sistema centralizado con lógica de **Upsert**, manejo de errores y generación de JSON para el Frontend.
- **Unified Medallion (SQL)**: Consolidación de Ventas, People Analytics e Impacto Social en capas de refinamiento.
- **Analytics Dashboard (Next.js)**: Capa de visualización premium desplegada en **Vercel** con métricas en tiempo real.
- **Storytelling Proactivo**: Enfoque en narrativa de impacto social y ética de datos.

## 🚀 Tecnologías Senior
- **Python**: Pandas, NumPy, SQLAlchemy (Pipeline & Anomaly Detection).
- **Escalabilidad SQL**: Estructura de tablas normalizadas y lógica de agregación avanzada.
- **BI Strategy**: Inteligencia de tiempo (YTD, Moving Averages 3M) y UX de alto impacto.

├── frontend/                 # NUEVO: Dashboard de Visualización (Next.js)
│   ├── src/app/              # UI Components & Page Layout
│   └── public/data/          # Fuente de la Verdad (Master JSON)
├── master_solution/          # Arquitectura Integrada y Orquestación
│   ├── scripts/              # MASTER_ORCHESTRATOR.py & Unified SQL
│   └── docs/                 # Diccionario de KPIs Maestro
├── etl/                      # Módulos de Ventas y Analítica
├── people_analytics/         # Análisis de Capital Humano
├── social_impact/            # Análisis de Impacto Social
├── pipeline/                 # Ingeniería de Pipelines
├── sql/                      # DWH Schemas & Optimized Queries
├── vercel.json               # Configuración de Despliegue Cloud
└── README.md                 # Visión Master del Proyecto

## 📊 Medidas DAX Críticas
- **Sales YTD**: `TOTALYTD([Total Sales], 'Dim_Calendario'[Date])`
- **Moving Avg 3M**: Suavizado de tendencias temporales.
- **QoQ Growth**: Análisis dinámico intertrimestral.

## 📑 Ética de Datos y Privacidad (People Analytics)
Como **Especialista en People Analytics**, la integridad y privacidad son pilares innegociables:
- **Anonimización**: Se han eliminado identificadores personales (nombres, DNIs) sustituyéndolos por IDs únicos para el análisis masivo.
- **Cumplimiento**: El diseño de este ecosistema sigue principios de **GDPR** y leyes locales de protección de datos, asegurando que el análisis de desempeño sea justo, transparente y basado únicamente en méritos objetivos.

## 🌍 Open Data & Social Responsibility
Este proyecto integra una capa de **Impacto Social** utilizando Datos Abiertos para transformar números en narrativas accionables:
- **Transparencia (Open Science)**: Uso de fuentes confiables como la [ONE RD](https://www.one.gob.do/) y el [Banco Mundial](https://data.worldbank.org/).
- **Hallazgo Clave**: Se identificó una brecha de **4 años de escolaridad** promedio entre provincias rurales y urbanas correlacionada a la falta de conectividad.
- **Propuesta**: Los datos sugieren que un incremento del 1% en infraestructura TIC rural eleva proactivamente la escolaridad en un 5% interanual.

## 🛠️ Manejo de Errores y Autocuración
El ecosistema de automatización corporativo cuenta con mecanismos de **High Availability (HA)**:
- **Reintentos (Retries)**: El orquestador Python reintenta la conexión hasta 3 veces antes de disparar un error fatal.
- **Logs de Auditoría**: Cada carga registra el éxito o fallo en `pipeline_execution.log`.
- **Integridad Transaccional**: Las transformaciones SQL se ejecutan bajo lógica transaccional, evitando que fallos de red dejen datos inconsistentes en las capas finales.

---
*Desarrollado con un enfoque en **arquitectura de datos empresarial**, **optimización masiva** y **gobernanza estratégica**.*
