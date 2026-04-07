-- --- Arquitectura de Medallón: Consolidación Multimoneda ---
-- Estructura corporativa dividida por capas de refinamiento del dato.

-- 1. Capa BRONZE (Crudo - Append/Upsert)
CREATE TABLE IF NOT EXISTS brz_sales (
    OrderID INTEGER PRIMARY KEY,
    Date TEXT,
    Amount REAL,
    Currency TEXT,
    Region TEXT
);

-- 2. Capa SILVER (Limpieza, Tipado y Conversión)
-- Esta capa normaliza los datos y realiza la conversión a USD base para reporteo global.
DROP TABLE IF EXISTS slv_sales;
CREATE TABLE slv_sales AS
SELECT 
    OrderID,
    Date,
    Amount as Original_Amount,
    Currency,
    Region,
    CASE 
        WHEN Currency = 'DOP' THEN Amount / 58.5
        WHEN Currency = 'EUR' THEN Amount / 0.92
        WHEN Currency = 'MXN' THEN Amount / 17.2
        WHEN Currency = 'CAD' THEN Amount / 1.35
        ELSE Amount 
    END AS Amount_USD,
    'Cleaned' AS Processing_Status
FROM brz_sales
WHERE Amount > 0;

-- 3. Capa GOLD (Modelado Agregado - Optimizado para Power BI)
-- Se crean tablas de hechos finales con índices de alto rendimiento.
DROP TABLE IF EXISTS gld_fact_sales;
CREATE TABLE gld_fact_sales (
    OrderID INTEGER PRIMARY KEY,
    Date TEXT,
    Amount_USD REAL,
    Region TEXT
);

INSERT INTO gld_fact_sales
SELECT OrderID, Date, Amount_USD, Region 
FROM slv_sales;

-- --- Indexación y Tuning Corporativo ---
CREATE INDEX idx_gld_date ON gld_fact_sales(Date);
CREATE INDEX idx_gld_region ON gld_fact_sales(Region);

-- 4. Script de Mantenimiento y Autocuración
-- Elimina registros huérfanos o datos de prueba que no tienen fecha válida.
DELETE FROM brz_sales WHERE Date IS NULL OR Date = '';
