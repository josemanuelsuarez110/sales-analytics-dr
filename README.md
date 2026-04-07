# 📊 Sales Analytics - República Dominicana (End-to-End Project)

Proyecto profesional de **Data Engineering** y **Business Intelligence** diseñado para transformar datos transaccionales crudos en insights estratégicos mediante un stack moderno de datos.

## 🚀 Tecnologías Utilizadas
- **Lenguaje**: Python 3.10+
- **Librerías**: Pandas, SQLAlchemy
- **Base de Datos**: SQLite (Simulación local de DWH)
- **Transformación**: SQL (Consultas de modelado en Estrella)
- **Visualización**: Power BI & DAX

## 📂 Estructura del Proyecto
```bash
├── etl/
│   └── etl_sales.py         # Script de generación y limpieza de datos (Python)
├── sql/
│   ├── sales_data.db        # Almacén de Datos (DWH) resultante
│   ├── star_schema_setup.sql # Script SQL para el esquema en estrella
│   └── apply_schema.py      # Puente para aplicar SQL en la base de datos
├── powerbi/
│   └── powerbi_specs.md     # Documentación técnica de DAX y diseño UI
└── verify_data.py           # Auditoría de integridad de datos final
```

## 🛠️ Detalles del Pipeline
1. **Extracción y Carga**: Generación de un dataset sintético con **2,500 registros** enfocados en las provincias de la República Dominicana.
2. **Transformación**: Modelado de datos mediante un Esquema en Estrella (Star Schema) para optimizar el rendimiento de las consultas y la inteligencia de tiempo en Power BI.
3. **Métrica de Negocio**: Cálculo automatizado del **ITBIS (18%)** y métricas interanuales (YoY Growth).

## 📊 Medidas DAX Implementadas
- **Total Sales**: `SUM(Fact_Sales[Revenue])`
- **Sales LY**: `CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Dim_Calendario'[Date]))`
- **YoY Growth**: `DIVIDE([Total Sales] - [Sales LY], [Sales LY], 0)`

---
*Este proyecto es parte de mi portafolio profesional en el área de Datos.*
