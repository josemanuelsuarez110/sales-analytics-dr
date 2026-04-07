-- --- Data Transformation & Modeling (Star Schema) ---
-- This script transforms 'raw_sales' into a professional Star Schema structure.

-- 1. Dim_Productos (Products Dimension)
DROP TABLE IF EXISTS Dim_Productos;
CREATE TABLE Dim_Productos AS
SELECT DISTINCT 
    ProductID,
    CASE 
        WHEN ProductID = 101 THEN 'Arroz Selecto 5lb'
        WHEN ProductID = 102 THEN 'Aceite Vegetal 1L'
        WHEN ProductID = 103 THEN 'Café Molido 454g'
        WHEN ProductID = 104 THEN 'Detergente en Polvo'
        WHEN ProductID = 105 THEN 'Jabón de Cuaba'
        WHEN ProductID = 106 THEN 'Refresco Gaseoso 2L'
        WHEN ProductID = 107 THEN 'Salami Súper Especial'
        WHEN ProductID = 108 THEN 'Queso Geo 1lb'
    END AS ProductName,
    CASE 
        WHEN ProductID in (101, 102) THEN 'Alimentos'
        WHEN ProductID in (103, 106) THEN 'Bebidas'
        WHEN ProductID in (104, 105) THEN 'Limpieza'
        WHEN ProductID = 107 THEN 'Embutidos'
        WHEN ProductID = 108 THEN 'Lácteos'
    END AS Category
FROM raw_sales;

-- 2. Dim_Clientes (Customers Dimension)
DROP TABLE IF EXISTS Dim_Clientes;
CREATE TABLE Dim_Clientes AS
SELECT DISTINCT 
    CustomerID,
    StoreLocation AS CustomerCity, -- Simulating City mapping
    'Dominican Republic' AS Country
FROM raw_sales;

-- 3. Dim_Calendario (Time Intelligence Dimension)
-- SQLite doesn't have a built-in calendar generator, so we extract from existing dates
DROP TABLE IF EXISTS Dim_Calendario;
CREATE TABLE Dim_Calendario AS
SELECT DISTINCT 
    Date,
    strftime('%Y', Date) AS Year,
    strftime('%m', Date) AS Month,
    (CAST(strftime('%m', Date) AS INT) + 2) / 3 AS Quarter,
    strftime('%w', Date) AS DayOfWeek
FROM raw_sales;

-- 4. Fact_Sales (Fact Table)
DROP TABLE IF EXISTS Fact_Sales;
CREATE TABLE Fact_Sales AS
SELECT 
    OrderID,
    Date,
    CustomerID,
    ProductID,
    Quantity,
    UnitPrice,
    (Quantity * UnitPrice) AS Revenue
FROM raw_sales;

-- 5. Business Metric View: v_sales_performance
-- Includes ITBIS (18%) calculation
DROP VIEW IF EXISTS v_sales_performance;
CREATE VIEW v_sales_performance AS
SELECT 
    f.*,
    p.ProductName,
    p.Category,
    c.CustomerCity,
    (f.Revenue * 0.18) AS ITBIS_Amount,
    (f.Revenue + (f.Revenue * 0.18)) AS Total_With_Tax
FROM Fact_Sales f
JOIN Dim_Productos p ON f.ProductID = p.ProductID
JOIN Dim_Clientes c ON f.CustomerID = c.CustomerID;
