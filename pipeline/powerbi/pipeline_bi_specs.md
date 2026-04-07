# Enterprise BI Layer: Lead Architect Strategy

Este documento describe la capa semántica diseñada para la consolidación global de ventas, con enfoque en seguridad (RLS) y monitoreo proactivo de la salud del dato.

## 1. DAX Inteligente (Business Intelligence Avanzado)

### Detección de Datos Faltantes (Stale Data Detection)
Métrica que avisa visualmente si no han entrado datos en las últimas 24 horas.
```dax
Data Health Alert = 
VAR LastDataDate = MAX(gld_fact_sales[Date])
VAR CurrentDate = TODAY()
VAR DateGap = DATEDIFF(LastDataDate, CurrentDate, DAY)
RETURN 
IF(DateGap >= 1, "❗ REVISAR: Brecha de Datos de " & DateGap & " días", "✅ Datos Actualizados")
```

### Crecimiento Interperiodo WoW (Week-over-Week)
Cálculo automatizado a nivel de semana para identificar cambios bruscos en el rendimiento regional.
```dax
Sales WoW % = 
VAR CurrentWeekSales = [Total Sales USD]
VAR PreviousWeekSales = CALCULATE([Total Sales USD], DATEADD('Dim_Calendario'[Date], -7, DAY))
RETURN
DIVIDE(CurrentWeekSales - PreviousWeekSales, PreviousWeekSales, 0)
```

---

## 2. Row Level Security (RLS) - Seguridad Regional
Para filtrar los datos financieros según la región del usuario:

| Role Name | Filter Logic (DAX) |
| :--- | :--- |
| **Manager LATAM** | `gld_fact_sales[Region] = "LATAM"` |
| **Manager EMEA** | `gld_fact_sales[Region] = "EMEA"` |
| **Global Auditor** | *(Sin filtros, acceso total)* |

---

## 3. Actualización Incremental (Incremental Refresh)

Para optimizar datasets masivos, se recomienda configurar:
1. **RangeStart / RangeEnd**: Crear parámetros en Power Query.
2. **Filtrado**: Aplicar filtros de fecha a la tabla `gld_fact_sales` usando estos parámetros.
3. **Política**:
   - Conservar datos de los últimos **5 años**.
   - Actualizar datos de los últimos **15 días** (ventana de cambios).

---

## 4. Power BI Gateway (Gobernanza)
El ecosistema de automatización depende de un **Cluster de Gateways** para alta disponibilidad:
- Integración con el orquestador Python para refrescar solo tras el éxito del Pipeline.
- Notificaciones de error de refresco dirigidas al equipo de Data Engineering.
