# People Analytics Strategy: Senior Consultant Level

Este documento define la inteligencia de negocio aplicada al capital humano, centrada en la productividad, la eficiencia de atracción y la retención del talento.

## 1. Medidas DAX Estratégicas (Talent KPIs)

### Productividad: Revenue per Employee
Mide la eficiencia financiera de la fuerza laboral.
```dax
Revenue per Employee = 
DIVIDE(SUM(Fact_Sales[Revenue]), DISTINCTCOUNT(Dim_Employees[EmployeeID]), 0)
```
*(Requiere relación entre tablas de ventas y empleados)*

### Eficiencia: Time to Fill (Días promedio de vacante)
Mide la agilidad del equipo de Adquisición de Talento.
```dax
Avg Time to Fill = 
AVERAGE(Fact_Recruitment[DaysToHire])
```

### Impacto: Cost per Hire
Calcula la inversión necesaria para incorporar un nuevo colaborador.
```dax
Cost per Hire = 
DIVIDE(SUM(Fact_Recruitment[RecruitmentCosts]), COUNT(Fact_Recruitment[HiredID]), 0)
```

### Salud: Tasa de Rotación Voluntaria (Retention Rate)
```dax
Turnover Rate % = 
VAR TotalExits = COUNTROWS(FILTER(Dim_Employees, Dim_Employees[IsActive] = 0))
VAR TotalEmployees = COUNTROWS(Dim_Employees)
RETURN
DIVIDE(TotalExits, TotalEmployees, 0)
```

---

## 2. Dashboard Interface: "Executive Talent Overview"

### Estructura Visual
*   **KPI Scorecard (Panel Superior)**:
    - `Headcount Actual` (Número total de empleados).
    - `Turnover Rate` (Con indicador Rojo si > 5%).
    - `eNPS` (Salud del clima organizacional).
*   **Segmentación 9-Box Grid (Matriz 3x3)**:
    - Gráfico de burbujas que represente la distribución del talento (Potencial vs Desempeño).
*   **Riesgo de Fuga (Mapa de Calor)**:
    - Análisis por departamento y antigüedad para identificar focos de desvinculación proactiva.

### Filtros Senior (Slicers)
- **Departamento**: IT, Ventas, Operaciones, etc.
- **Diversidad**: Género (Análisis de brecha de participación).
- **Antigüedad**: <1 año, 1-3 años, 3-5 años, >5 años.

---

## 3. Notas de UX
- **Colores de People Analytics**: Tonos de Azul Sereno (#1E3A8A) para estabilidad y Verde Esmeralda (#10B981) para crecimiento de talento.
- **Alerta de Vuelo (Flight Risk)**: Sincronizar datos con alertas automáticas de Power BI Service cuando un colaborador de "Alto Potencial" tenga un `Risk_Score > 4`.
