# Power BI Technical Specifications & BI Design

This document provides the necessary business logic and UI/UX guidelines to implement the Dashboard in Power BI, using the Star Schema from `sales_data.db`.

## 1. Data Modeling & Relationships
To ensure optimal performance and use of Time Intelligence, configure the following relationships in the **Model View** (1:N, Single direction):

- **Dim_Calendario[Date]** → **Fact_Sales[Date]** (One-to-Many)
- **Dim_Productos[ProductID]** → **Fact_Sales[ProductID]** (One-to-Many)
- **Dim_Clientes[CustomerID]** → **Fact_Sales[CustomerID]** (One-to-Many)

---

## 2. DAX Measures (Business Intelligence Logic)
Create a new table named `_Measures` and add the following formulas:

### Core Metrics
- **Total Sales**
  ```dax
  Total Sales = SUM(Fact_Sales[Revenue])
  ```
- **Total Orders**
  ```dax
  Total Orders = DISTINCTCOUNT(Fact_Sales[OrderID])
  ```

### Time Intelligence (Growth YoY)
- **Sales LY (Last Year)**
  ```dax
  Sales LY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Dim_Calendario'[Date]))
  ```
- **YoY Growth %**
  ```dax
  YoY Growth = DIVIDE([Total Sales] - [Sales LY], [Sales LY], 0)
  ```
  *(Format this as Percentage)*

### Performance & Targets
- **Target Achievement**
  ```dax
  Target Achievement = DIVIDE([Total Sales], 1000000, 0) 
  -- Assuming a defined target of 1M for the current period
  ```

---

## 3. Dashboard UI/UX Design

### Page 1: Executive Overview (Resumen Ejecutivo)
**Goal:** High-level performance tracking for decision-makers.

- **KPI Cards (Top):**
  - [Total Sales] with YoY Growth (Green/Red indicator).
  - [Total Orders] and [Average Ticket].
- **Sales Trend (Line Chart):**
  - X-Axis: `Dim_Calendario[Month]`
  - Y-Axis: `[Total Sales]`
  - *Tip: Use 'Year' as a slicer to compare seasons.*
- **Geographic Performance (Map/Choropleth):**
  - Location: `Dim_Clientes[CustomerCity]`
  - Bubble Size: `[Total Sales]`
  - *Context: Dominican provinces heatmap.*

### Page 2: Product Performance (Detalle de Productos)
**Goal:** Identifying best-sellers and inventory optimization.

- **Pareto Analysis (Combo Chart):**
  - Bars: `[Total Sales]` by `Dim_Productos[ProductName]`
  - Line: Cumulative % of Sales.
- **Category Breakdown (Donut Chart):**
  - Legend: `Dim_Productos[Category]`
  - Values: `[Total Sales]`
- **Detail Table (Matrix):**
  - Rows: `Category` > `ProductName`
  - Values: `Sales`, `Quantity`, `YoY Growth`.
  - *Conditional Formatting: Apply 'Data Bars' to the Sales column.*

---

## 4. Visual Styles
- **Color Palette:** Dark Emerald and Slate Gray (#064E3B, #1E293B).
- **Typography:** Inter or Outfit (Clean Sans Serif).
- **Theme:** Use "Neutral" backgrounds with "Glassmorphism" effect for modern cards.
