-- --- Arquitectura de Automatización: Staging e Incremento ---
-- Este script define la lógica para la carga incremental y el área de staging.

-- 1. Crear Tabla de Staging (Área Temporal)
-- Esta tabla recibe los datos crudos del motor de orquestación en Python.
DROP TABLE IF EXISTS stg_sales;
CREATE TABLE stg_sales (
    OrderID INTEGER,
    Date TEXT,
    CustomerID INTEGER,
    ProductID INTEGER,
    Quantity REAL,
    UnitPrice REAL,
    StoreLocation TEXT
);

-- 2. "Carga Incremental": Lógica de Automatización
-- Este procedimiento inserta solo registros nuevos que no existan en Fact_Sales 
-- comparando el OrderID y la fecha.
INSERT INTO Fact_Sales (OrderID, Date, CustomerID, ProductID, Quantity, UnitPrice, Revenue)
SELECT 
    s.OrderID,
    s.Date,
    s.CustomerID,
    s.ProductID,
    s.Quantity,
    s.UnitPrice,
    (s.Quantity * s.UnitPrice) AS Revenue
FROM stg_sales s
WHERE NOT EXISTS (
    SELECT 1 FROM Fact_Sales f 
    WHERE f.OrderID = s.OrderID
);

-- 3. Actualización de Dimensiones (Sincronización Automática)
-- Asegura que nuevos clientes de la carga incremental se registren en Dim_Clientes.
INSERT INTO Dim_Clientes (CustomerID, CustomerCity)
SELECT DISTINCT 
    s.CustomerID,
    s.StoreLocation
FROM stg_sales s
WHERE NOT EXISTS (
    SELECT 1 FROM Dim_Clientes c 
    WHERE c.CustomerID = s.CustomerID
);

-- 4. Limpieza de Staging (Opcional, usualmente se conserva para auditoría)
-- DELETE FROM stg_sales;
