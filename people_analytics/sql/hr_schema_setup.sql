-- --- Arquitectura de People Analytics: HR Data Infrastructure ---
-- Este script define la capa de persistencia para el análisis de capital humano.

PRAGMA foreign_keys = ON;

-- 1. Dim_Employees (Colaboradores - Anonimizado)
-- Solo conservamos IDs y demografía general para reporteo ético.
DROP TABLE IF EXISTS Dim_Employees;
CREATE TABLE Dim_Employees (
    EmployeeID INTEGER PRIMARY KEY,
    Department TEXT NOT NULL,
    Gender TEXT,
    Age INTEGER,
    MaritalStatus TEXT,
    JoinDate TEXT NOT NULL,
    IsActive INTEGER DEFAULT 1 -- 1: Activo, 0: Baja
);

-- 2. Fact_Payroll (Historial Salarial)
DROP TABLE IF EXISTS Fact_Payroll;
CREATE TABLE Fact_Payroll (
    RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER,
    Salary REAL NOT NULL,
    LastIncreaseDate TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES Dim_Employees(EmployeeID)
);

-- 3. Fact_Performance_Reviews (Evaluaciones de Desempeño)
DROP TABLE IF EXISTS Fact_Performance_Reviews;
CREATE TABLE Fact_Performance_Reviews (
    ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER,
    PerformanceRating INTEGER, -- 1 a 5
    PotentialRating INTEGER,    -- 1 a 5 (Para 9-Box Grid)
    ReviewDate TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES Dim_Employees(EmployeeID)
);

-- 4. eNPS (Employee Net Promoter Score) & Calidad de Clima
DROP TABLE IF EXISTS Fact_Climate_Surveys;
CREATE TABLE Fact_Climate_Surveys (
    SurveyID INTEGER PRIMARY KEY AUTOINCREMENT,
    EmployeeID INTEGER,
    RecommendationScore INTEGER, -- 0 a 10
    SatisfactionScore INTEGER,
    SurveyDate TEXT,
    FOREIGN KEY (EmployeeID) REFERENCES Dim_Employees(EmployeeID)
);

-- --- Consultas Estratégicas para People Analytics ---

-- A. Cálculo de eNPS (Employee Net Promoter Score)
DROP VIEW IF EXISTS v_hr_enps_metrics;
CREATE VIEW v_hr_enps_metrics AS
WITH Scores AS (
    SELECT 
        COUNT(*) as TotalResponses,
        SUM(CASE WHEN RecommendationScore >= 9 THEN 1 ELSE 0 END) as Promoters,
        SUM(CASE WHEN RecommendationScore <= 6 THEN 1 ELSE 0 END) as Detractors
    FROM Fact_Climate_Surveys
)
SELECT 
    Promoters,
    Detractors,
    TotalResponses,
    ((Promoters * 1.0 / TotalResponses) - (Detractors * 1.0 / TotalResponses)) * 100 as eNPS_Score
FROM Scores;

-- B. Tasa de Rotación Voluntaria Mensual
DROP VIEW IF EXISTS v_hr_turnover_rate;
CREATE VIEW v_hr_turnover_rate AS
SELECT 
    strftime('%Y-%m', JoinDate) as Month,
    COUNT(CASE WHEN IsActive = 0 THEN 1 END) as TotalExits,
    COUNT(*) as Headcount,
    (COUNT(CASE WHEN IsActive = 0 THEN 1 END) * 1.0 / COUNT(*)) * 100 as TurnoverRate
FROM Dim_Employees
GROUP BY 1;
