import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import statsmodels.api as sm

# Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

# Título del Dashboard
st.title("📊 Dashboard de Análisis de Ventas")

# Carga de datos (Simulada)
@st.cache_data # Para que no recargue el CSV en cada click
def load_data():
    df = pd.read_csv("/workspaces/Proyectos/EDA_principiante_1/Sample - Superstore.csv", encoding = 'latin-1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    return df

df = load_data()
df = df.drop(columns=['Country', 'Postal Code'], errors='ignore')
df['Costs'] = df['Sales'] - df['Profit']
state_full_to_code = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY', 'District of Columbia': 'DC'
}

state_to_code_lower = {state.lower(): code for state, code in state_full_to_code.items()}

state_aliases = {
    'washington dc': 'district of columbia',
    'washington d c': 'district of columbia',
}

# --- SIDEBAR / FILTROS ---
st.sidebar.header("Filtros")
region = st.sidebar.multiselect("Selecciona Región:", options=df["Region"].unique(), default=df["Region"].unique())
categorias = sorted(df["Category"].dropna().unique())
categoria = st.sidebar.selectbox("Selecciona Categoría:", options=["Todas"] + categorias)

df_selection = df[df["Region"].isin(region)]

if categoria != "Todas":
    df_selection = df_selection[df_selection["Category"] == categoria]

# Filtro de fecha
# 1. Obtenemos las fechas extremas del dataset original
min_date = df["Order Date"].min().to_pydatetime()
max_date = df["Order Date"].max().to_pydatetime()

# 2. Creamos el Slider (la línea recta)
# Al pasarle una lista/tupla de dos valores, se convierte automáticamente en un "Range Slider"
date_range = st.sidebar.slider(
    "Selecciona el rango de fechas:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date), # Valor inicial (todo el rango)
    format="DD/MM/YY"            # Formato visual
)

# 3. Aplicamos el filtro al dataframe actual (sin perder filtros previos)
# date_range[0] es la fecha de inicio, date_range[1] es la fecha de fin
df_selection = df_selection[
    (df_selection["Order Date"] >= date_range[0]) &
    (df_selection["Order Date"] <= date_range[1])
]

# Filtro de Segmento
segmento = st.sidebar.multiselect("Segmento:", options=df["Segment"].unique(), default=df["Segment"].unique())

# Aplicar filtro adicional de segmento
df_selection = df_selection[
    (df_selection["Segment"].isin(segmento))
]

# --- MAIN PAGE: KPIs ---
tab1, tab2, tab3 = st.tabs(["Ventas & Tiempo", "Productos & Geografía", "Clientes & Eficiencia"])

with tab1:
     st.subheader("KPIs Clave")
     col1, col2, col3 = st.columns(3)
     total_sales = df_selection["Sales"].sum()
     col1.metric("Ventas Totales", f"US$ {total_sales:,.2f}")
     total_profit = df_selection["Profit"].sum()
     col2.metric("Beneficio Total", f"US$ {total_profit:,.2f}")
     total_costs = df_selection["Costs"].sum()
     col3.metric("Costos Totales", f"US$ {total_costs:,.2f}")

# --- GRÁFICOS ---
with tab1:
    ventas_tiempo = df_selection.groupby(df_selection["Order Date"].dt.to_period("M")).agg({"Sales":"sum", "Profit":"sum"}).reset_index()
    ventas_tiempo["Order Date"] = ventas_tiempo["Order Date"].dt.to_timestamp()
    fig1 = px.line(ventas_tiempo, x="Order Date", y=["Sales", "Profit"], title="Ventas vs Beneficio a lo largo del tiempo")
    st.plotly_chart(fig1, use_container_width=True)
    st.write("Vemos un comportamiento cíclico, en donde las ventas aumentan en la segunda mitad del año (sobre todo a partir de agosto con picos en " \
    "noviembre y diciembre). Esto se debe a que el dataset es de una tienda de retail, y en esta industria es común que las ventas aumenten en la " \
    "temporada navideña. Además se puede observar que el beneficio se comporta de acuerdo a las ventas, como es de esperarse."
    "El único momento en donde se vio pérdida es en enero de 2015")
    fig2 = px.pie(df_selection, values="Sales", names="Segment", hole=0.5, title="Ventas por Segmento de Cliente")
    st.plotly_chart(fig2, use_container_width=True)
    st.write("El segmento Consumer es el que más aporta a las ventas, seguido por el segmento Corporate. El segmento Home Office es el que menos " \
    "aporta, aunque no es un segmento despreciable. Vemos que si englobamos al sector Home Office y al Corporativo, tenemos que la mitad de las" \
    "ventas van para el sector profesional y la otra mitad para consumidores individuales")
    df_selection['Day_Name'] = df_selection['Order Date'].dt.day_name()
    ventas_dia = df_selection.groupby('Day_Name')['Sales'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']).reset_index()
    fig3 = px.line_polar(ventas_dia, r='Sales', theta='Day_Name', line_close=True, title="Ventas por Día de la Semana")
    st.plotly_chart(fig3, use_container_width=True)
    st.write("Los días de la semana con más actividad se concentran entre los viernes y los lunes. El miércoles es por distancia el día con menos " \
    "ventas. Se podría analizar acortar los horarios de los miércoles y extender los de los lunes y viernes para optimizar el tiempo de trabajo y" \
    "los salarios")

with tab2:
    ventas_categoria = df_selection.groupby("Category").agg({"Sales":"sum", "Profit":"sum"}).reset_index()
    fig4 = px.bar(ventas_categoria, x="Category", y=["Sales", "Profit"], title="Ventas y Beneficio por Categoría")
    st.plotly_chart(fig4, use_container_width=True)
    st.write(
        "La categoría de Tecnología es la que más aporta a las ventas, seguida por Muebles y luego por Oficina. "
        "La categoría de tecnología es a su vez la que más aporta al beneficio. Podemos ver que los Muebles "
        "tienen mas ventas pero menos ganancias que Oficina, lo que da a entender que es la categoría menos rentable."
    )
    ventas_subcategoria = df_selection.groupby("Sub-Category").agg({"Sales":"sum", "Profit":"sum"}).reset_index()
    top_sub = (
        df_selection.groupby(["Category", "Sub-Category"], as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
        .head(10)
        .sort_values("Profit", ascending=True)
    )
    fig5 = px.bar(
        top_sub,
        x="Profit",
        y="Sub-Category",
        color="Category",
        orientation='h',
        title="Top 10 Sub-Categorías más Rentables",
        labels={"Profit": "Beneficio", "Sub-Category": "Sub-Categoría", "Category": "Categoría"},
    )
    fig5.update_yaxes(categoryorder="total ascending")
    st.plotly_chart(fig5, use_container_width=True)
    st.write("Vemos que en las 10 subcategorías con más beneficios predominan las correspondientes a la categoría de " \
             "Oficina, aunque las que generan más beneficios son las de Tecnología. De Mubles solo hay dos que no generan" \
             "tanto beneficio")
    ventas_estado = df_selection.groupby("State")["Sales"].sum().reset_index()
    fig6 = px.scatter(df_selection, x="Discount", y="Profit", color="Category", hover_data=["Product Name"], title="Impacto de los Descuentos en el Beneficio")
    st.plotly_chart(fig6, use_container_width=True)
    st.write("Vemos que a medida que aumentan los descuentos, el beneficio tiende a disminuir. Se observa también que se" \
        "empiezan a manifestar beneificios negativos a partir de un descuento de 20% ")
    
    # 1. Agrupamos y reseteamos index
    ventas_estado = df_selection.groupby("State", as_index=False)["Sales"].sum()

    # 2. Normalizamos nombres y creamos códigos de estado de forma robusta
    ventas_estado["State_Key"] = (
        ventas_estado["State"]
        .astype(str)
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.lower()
        .replace(state_aliases)
    )
    ventas_estado["State_Code"] = ventas_estado["State_Key"].map(state_to_code_lower)

    # 3. Consolidamos por código y completamos estados sin ventas con 0 para que también se pinten
    ventas_estado = ventas_estado.dropna(subset=["State_Code"]).groupby("State_Code", as_index=False)["Sales"].sum()
    all_states = pd.DataFrame({"State_Code": sorted(state_full_to_code.values())})
    ventas_estado = all_states.merge(ventas_estado, on="State_Code", how="left").fillna({"Sales": 0})
    
    # 4. Creamos el mapa usando los códigos (State_Code)
    fig7 = px.choropleth(
        ventas_estado, 
        locations="State_Code",  # <-- Ahora usamos el código de 2 letras
        locationmode="USA-states", 
        scope="usa", 
        color="Sales", 
        color_continuous_scale="Viridis", # Un color más "pro"
        title="Ventas Totales por Estado",
        labels={'Sales': 'Ventas Totales (USD)', 'State_Code': 'Estado'}
    )
    
    st.plotly_chart(fig7, use_container_width=True)
    st.write("Los estados con más ventas son California, Nueva York, Texas y Washington. También se observa que los estados" \
    "en el oeste suelen tener más ventas y los céntricos menos ventas.")

with tab3:
    dias_orden = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dias_es = {
        "Monday": "Lunes",
        "Tuesday": "Martes",
        "Wednesday": "Miércoles",
        "Thursday": "Jueves",
        "Friday": "Viernes",
        "Saturday": "Sábado",
        "Sunday": "Domingo",
    }
    envios_por_dia = (
        df_selection.assign(Dia_Semana=df_selection["Ship Date"].dt.day_name())
        .groupby("Dia_Semana", as_index=False)
        .size()
    )
    envios_por_dia["Dia_Semana"] = pd.Categorical(envios_por_dia["Dia_Semana"], categories=dias_orden, ordered=True)
    envios_por_dia = envios_por_dia.sort_values("Dia_Semana")
    envios_por_dia["Dia_Semana_ES"] = envios_por_dia["Dia_Semana"].astype(str).map(dias_es)

    fig8 = px.bar(
        envios_por_dia,
        x="Dia_Semana_ES",
        y="size",
        title="Cantidad de Envíos por Día de la Semana",
        labels={"Dia_Semana_ES": "Día de la Semana", "size": "Cantidad de Envíos"},
    )
    st.plotly_chart(fig8, use_container_width=True)
    st.write("La carga logística alcanza sus picos de operación los martes, miércoles y viernes, mientras que el domingo registra la actividad mínima, posicionándose como el día ideal para realizar tareas de mantenimiento técnico sin afectar el flujo de salida de pedidos.")
    top_clientes = (
        df_selection.groupby("Customer Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .sort_values(ascending=True)
        .reset_index()
    )
    fig9 = px.bar(top_clientes, x="Sales", y="Customer Name", orientation='h', title="Top 10 Clientes VIP")
    st.plotly_chart(fig9, use_container_width=True)
    st.write("Se identifica una fuerte dependencia de ingresos en un grupo selecto de clientes VIP, liderado por Sean Miller con compras superiores a los veinticinco mil dólares, lo que hace indispensable implementar programas de fidelización para proteger estos activos críticos del negocio.")
    heatmap_data = df_selection.pivot_table(index='Category', columns='Region', values='Sales', aggfunc='sum')
    fig10 = px.imshow(heatmap_data, text_auto=True, title="Concentración de Ventas: Categoría vs Región")
    st.plotly_chart(fig10, use_container_width=True)
    st.write("El motor de ingresos se concentra en la tecnología del este y los muebles del oeste, contrastando con el bajo desempeño sistemático de la región sur, donde es prioritario investigar barreras de mercado para equilibrar el crecimiento geográfico de la empresa.")