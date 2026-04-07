-- --- Arquitectura de Datos de Impacto Social (Open Data Layer) ---
-- Este script unifica fuentes públicas para el análisis de desarrollo humano.

-- 1. Tabla de Datos Abiertos (Capa de Staging Social)
DROP TABLE IF EXISTS stg_social_indicators;
CREATE TABLE stg_social_indicators (
    Provincia TEXT,
    Region TEXT,
    Internet_Access_Pct REAL,
    Avg_Years_Education REAL,
    Public_Investment_USDm REAL,
    Date TEXT
);

-- 2. Consolidación de Histórico (Series Temporales Simuladas)
-- Esta vista permite observar la evolución de la brecha digital por región.
DROP VIEW IF EXISTS v_social_evolution;
CREATE VIEW v_social_evolution AS
SELECT 
    Region,
    AVG(Internet_Access_Pct) as Avg_Internet,
    AVG(Avg_Years_Education) as Avg_Education,
    SUM(Public_Investment_USDm) as Total_Investment,
    strftime('%Y', Date) as Year
FROM stg_social_indicators
GROUP BY Region, Year;

-- 3. Análisis de Desigualdad (Hidden Story)
-- Muestra las provincias con menor inversión pero mayor potencial educativo.
DROP VIEW IF EXISTS v_social_inequality_index;
CREATE VIEW v_social_inequality_index AS
SELECT 
    Provincia,
    Internet_Access_Pct,
    Avg_Years_Education,
    Public_Investment_USDm,
    (Avg_Years_Education / NULLIF(Public_Investment_USDm, 0)) as Efficiency_Score
FROM stg_social_indicators
ORDER BY Efficiency_Score DESC;

-- 4. Cumplimiento Ético (Anonimización Social)
-- En Datos Abiertos Públicos no suele haber IDs de personas, 
-- pero nos aseguramos de no agregar datos de nivel micro-población.
DELETE FROM stg_social_indicators WHERE Provincia IS NULL;
