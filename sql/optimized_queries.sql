-- --- SQL Optimizado: CTEs & Window Functions ---
-- Proyecto: Sales Analytics DR - Senior Data Architect

-- 1. Análisis de Crecimiento Mensual y Rank de Productos
-- Esta consulta utiliza un CTE para consolidar ingresos y Window Functions 
-- para calcular el ranking de ventas sin subconsultas pesadas.

WITH MonthlyRevenue AS (
    SELECT 
        p.Category,
        p.ProductName,
        strftime('%Y-%m', f.Date) AS SalesMonth,
        SUM(f.Revenue) AS MonthlyTotal
    FROM Fact_Sales f
    JOIN Dim_Productos p ON f.ProductID = p.ProductID
    GROUP BY 1, 2, 3
)
SELECT 
    SalesMonth,
    Category,
    ProductName,
    MonthlyTotal,
    -- Ranking de producto más vendido por categoría en cada mes
    RANK() OVER (PARTITION BY SalesMonth, Category ORDER BY MonthlyTotal DESC) as Rank_Category,
    -- Acumulado de ventas por categoría mediante Window Function
    SUM(MonthlyTotal) OVER (PARTITION BY Category ORDER BY SalesMonth) as Running_Total_Category
FROM MonthlyRevenue
WHERE SalesMonth >= '2024-01'
ORDER BY SalesMonth DESC, MonthlyTotal DESC;


-- 2. Análisis de Pareto (Regla del 80/20) para Clientes
-- Identifica el 20% de los clientes que generan el 80% de los ingresos.
WITH CustomerSales AS (
    SELECT 
        CustomerID,
        SUM(Revenue) as TotalCustomerRev
    FROM Fact_Sales
    GROUP BY CustomerID
),
CumulativeSales AS (
    SELECT 
        CustomerID,
        TotalCustomerRev,
        SUM(TotalCustomerRev) OVER (ORDER BY TotalCustomerRev DESC) as RunningTotal,
        SUM(TotalCustomerRev) OVER () as GrandTotal
    FROM CustomerSales
)
SELECT 
    CustomerID,
    TotalCustomerRev,
    ROUND((RunningTotal / GrandTotal) * 100, 2) as CumulativePercentage
FROM CumulativeSales
WHERE CumulativePercentage <= 80
ORDER BY TotalCustomerRev DESC;
