-- --- Arquitectura Senior: Data Warehouse Modeling ---

-- Habilitar claves foráneas (Práctica estándar en SQLite para DDL)
PRAGMA foreign_keys = ON;

-- 1. Dim_Productos (Dimension Table)
DROP TABLE IF EXISTS Dim_Productos;
CREATE TABLE Dim_Productos (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT NOT NULL,
    Category TEXT NOT NULL
);

INSERT INTO Dim_Productos (ProductID, ProductName, Category)
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
    END,
    CASE 
        WHEN ProductID in (101, 102) THEN 'Alimentos'
        WHEN ProductID in (103, 106) THEN 'Bebidas'
        WHEN ProductID in (104, 105) THEN 'Limpieza'
        WHEN ProductID = 107 THEN 'Embutidos'
        WHEN ProductID = 108 THEN 'Lácteos'
    END
FROM raw_sales;

-- 2. Dim_Clientes (Dimension Table)
DROP TABLE IF EXISTS Dim_Clientes;
CREATE TABLE Dim_Clientes (
    CustomerID INTEGER PRIMARY KEY,
    CustomerCity TEXT NOT NULL,
    Country TEXT DEFAULT 'República Dominicana'
);

INSERT INTO Dim_Clientes (CustomerID, CustomerCity)
SELECT 
    CustomerID,
    MAX(StoreLocation) -- Se toma una ubicación representativa por cliente
FROM raw_sales
GROUP BY 1;

-- 3. Dim_Calendario (Time Intelligence Table)
DROP TABLE IF EXISTS Dim_Calendario;
CREATE TABLE Dim_Calendario (
    Date TEXT PRIMARY KEY,
    Year INTEGER,
    Month INTEGER,
    Quarter INTEGER,
    DayOfWeek INTEGER
);

INSERT INTO Dim_Calendario
SELECT DISTINCT 
    Date,
    CAST(strftime('%Y', Date) AS INTEGER),
    CAST(strftime('%m', Date) AS INTEGER),
    (CAST(strftime('%m', Date) AS INTEGER) + 2) / 3,
    CAST(strftime('%w', Date) AS INTEGER)
FROM raw_sales;

-- 4. Fact_Sales (Fact Table - Senior Optimized)
DROP TABLE IF EXISTS Fact_Sales;
CREATE TABLE Fact_Sales (
    OrderID INTEGER PRIMARY KEY,
    Date TEXT,
    CustomerID INTEGER,
    ProductID INTEGER,
    Quantity REAL,
    UnitPrice REAL,
    Revenue REAL,
    FOREIGN KEY (Date) REFERENCES Dim_Calendario(Date),
    FOREIGN KEY (CustomerID) REFERENCES Dim_Clientes(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Dim_Productos(ProductID)
);

INSERT INTO Fact_Sales
SELECT 
    OrderID,
    Date,
    CustomerID,
    ProductID,
    Quantity,
    UnitPrice,
    (Quantity * UnitPrice)
FROM raw_sales;

-- --- Indexación para Optimización de Latencia ---
CREATE INDEX idx_fact_date ON Fact_Sales(Date);
CREATE INDEX idx_fact_customer ON Fact_Sales(CustomerID);
CREATE INDEX idx_fact_product ON Fact_Sales(ProductID);

-- 5. Business View Integrada (v_sales_performance)
DROP VIEW IF EXISTS v_sales_performance;
CREATE VIEW v_sales_performance AS
SELECT 
    f.OrderID,
    f.Date,
    f.Revenue,
    p.ProductName,
    p.Category,
    c.CustomerCity,
    (f.Revenue * 0.18) AS ITBIS_Amount,
    (f.Revenue * 1.18) AS Total_With_Tax
FROM Fact_Sales f
JOIN Dim_Productos p ON f.ProductID = p.ProductID
JOIN Dim_Clientes c ON f.CustomerID = c.CustomerID;
