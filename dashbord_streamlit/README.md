# 📊 Dashboard de Análisis de Ventas (`app.py`)

Aplicación interactiva desarrollada con **Streamlit** y **Plotly** para el análisis exploratorio de ventas de una tienda retail en Estados Unidos. Permite filtrar datos dinámicamente y visualizar métricas clave de rendimiento comercial.

---

## 📂 Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `app.py` | Aplicación principal de Streamlit |
| `Sample - Superstore.csv` | Dataset de ventas (fuente: EDA_principiante_1) |

---

## 📊 Datos utilizados

**Archivo:** `Sample - Superstore.csv`  
**Encoding:** `latin-1`

| Propiedad | Detalle |
|---|---|
| Fuente | Sample Superstore – dataset público de Tableau/Kaggle |
| Tipo de negocio | Tienda retail de productos de oficina (EE.UU.) |
| Período cubierto | 2014 – 2017 (aprox.) |

### Columnas principales utilizadas:

| Columna | Descripción |
|---|---|
| `Order Date` | Fecha del pedido |
| `Ship Date` | Fecha de envío |
| `Region` | Región geográfica (East, West, Central, South) |
| `State` | Estado de EE.UU. |
| `Category` | Categoría del producto (Technology, Furniture, Office Supplies) |
| `Sub-Category` | Sub-categoría del producto |
| `Segment` | Segmento de cliente (Consumer, Corporate, Home Office) |
| `Customer Name` | Nombre del cliente |
| `Sales` | Ventas en USD |
| `Profit` | Beneficio en USD |
| `Discount` | Descuento aplicado |
| `Costs` | Columna calculada: `Sales - Profit` |

> Las columnas `Country` y `Postal Code` fueron eliminadas por no ser relevantes para el análisis.

---

## 🔄 Qué se hizo (resumen)

### Filtros interactivos (Sidebar)
- **Región**: multiselect con todas las regiones disponibles.
- **Categoría**: selectbox (Todas / Technology / Furniture / Office Supplies).
- **Rango de fechas**: range slider temporal sobre `Order Date`.
- **Segmento**: multiselect por tipo de cliente.

### Tab 1 – Ventas & Tiempo
- **KPIs**: Ventas Totales, Beneficio Total y Costos Totales.
- **Línea temporal**: Ventas vs Beneficio agrupados por mes.
- **Donut chart**: distribución de ventas por segmento de cliente.
- **Radar polar**: ventas por día de la semana.

### Tab 2 – Productos & Geografía
- **Barras agrupadas**: ventas y beneficio por categoría.
- **Barras horizontales**: Top 10 sub-categorías más rentables.
- **Scatter plot**: impacto del descuento en el beneficio por categoría.
- **Mapa choropleth**: ventas totales por estado en EE.UU.

### Tab 3 – Clientes & Eficiencia
- **Barras**: cantidad de envíos por día de la semana.
- **Barras horizontales**: Top 10 clientes VIP por volumen de ventas.
- **Heatmap**: concentración de ventas por Categoría × Región.

---

## ▶️ Cómo ejecutar

1. Instalar dependencias:
   ```bash
   pip install streamlit pandas plotly numpy statsmodels
   ```
2. Ejecutar la app:
   ```bash
   streamlit run app.py
   ```
3. Abrir en el navegador la URL que aparece en la terminal (por defecto `http://localhost:8501`).