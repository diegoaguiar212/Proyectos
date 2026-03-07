# Analisis de Ventas - Sample Superstore

Proyecto de analisis exploratorio de datos (EDA) con Python en `analisis.ipynb`, usando el dataset `Sample - Superstore.csv`.

## Objetivo

Entender los factores que explican las perdidas y la rentabilidad del negocio, con foco en:

- impacto de descuentos sobre volumen y ganancia,
- categorias y subcategorias con peor desempeno,
- estados con ventas relevantes pero resultado negativo,
- recomendaciones accionables a partir de evidencia.

## Estructura del proyecto

- `analisis.ipynb`: notebook principal con todo el flujo de analisis y dashboard final.
- `Sample - Superstore.csv`: dataset de entrada.
- `README.md`: documentacion del proyecto.

## Requisitos

- Python 3.10+ (recomendado)
- Jupyter Notebook o VS Code con soporte de notebooks
- Librerias:
	- `pandas`
	- `seaborn`
	- `matplotlib`

## Instalacion rapida

```bash
pip install pandas seaborn matplotlib jupyter
```

## Como ejecutar

1. Abre la carpeta `EDA_principiante_1` en VS Code.
2. Abre `analisis.ipynb`.
3. Ejecuta las celdas en orden.

La carga de datos usa una ruta robusta para soportar cambios de directorio:

```python
from pathlib import Path

possible_paths = [
		Path("Sample - Superstore.csv"),
		Path("EDA_principiante_1") / "Sample - Superstore.csv"
]

csv_path = next((p for p in possible_paths if p.exists()), None)
if csv_path is None:
		raise FileNotFoundError("No se encontro 'Sample - Superstore.csv' en las rutas esperadas.")

df = pd.read_csv(csv_path, encoding="latin1")
```

## Contenido del analisis

El notebook incluye:

- limpieza de columnas y validacion inicial,
- matriz de correlacion de variables cuantitativas,
- analisis de descuentos vs cantidad vendida,
- analisis de descuentos vs ganancia promedio,
- analisis por categoria/subcategoria para detectar focos de perdida,
- analisis especifico de `Tables`:
	- linea de ganancia promedio por descuento,
	- tamano de puntos proporcional a cantidad vendida,
	- tabla resumen de ventas con descuento `<= 20%` vs `> 20%`,
- analisis geografico de estados con perdida,
- dashboard ejecutivo final con KPIs y visualizaciones resumen,
- conclusiones finales y recomendaciones.

## Hallazgos clave

- Los descuentos altos se asocian con menor rentabilidad.
- `Tables` es la subcategoria con mayor impacto negativo en ganancia.
- En `Tables`, niveles de descuento altos combinan volumen y margen negativo.
- Existen estados con ventas importantes pero ganancias negativas, consistentes con politicas de descuento agresivas.

## Conclusiones y acciones recomendadas

1. Limitar descuentos altos (especialmente por encima de 20%) en subcategorias sensibles al margen como `Tables`.
2. Definir topes de descuento por categoria/subcategoria usando historico de margen.
3. Revisar estrategia comercial y logistica en estados con perdida persistente.
4. Priorizar decisiones por utilidad, no solo por volumen de ventas.

## Errores comunes

- `FileNotFoundError`: verifica que exista `Sample - Superstore.csv` dentro de `EDA_principiante_1`.
- `ModuleNotFoundError`: instala dependencias del apartado **Instalacion rapida**.