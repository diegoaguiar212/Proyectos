# Analisis de Ventas - Sample Superstore

Proyecto de analisis exploratorio de datos (EDA) usando Python y Jupyter Notebook sobre el dataset `Sample - Superstore.csv`.

## Objetivo

Explorar informacion de ventas para:

- revisar la estructura y calidad inicial de los datos,
- inspeccionar las primeras filas del dataset,
- preparar la base para analisis de tendencias y visualizaciones.

## Estructura del proyecto

- `analisis.ipynb`: notebook principal con el flujo de analisis.
- `Sample - Superstore.csv`: dataset de entrada.
- `README.md`: documentacion del proyecto.

## Requisitos

- Python 3.10+ (recomendado)
- Jupyter Notebook o VS Code con soporte de notebooks
- Librerias Python:
	- `pandas`
	- `seaborn`
	- `matplotlib`

## Instalacion rapida

```bash
pip install pandas seaborn matplotlib jupyter
```

## Como ejecutar

1. Abre el proyecto en VS Code o en tu entorno local.
2. Abre `analisis.ipynb`.
3. Ejecuta las celdas en orden.

La carga de datos se realiza con:

```python
df = pd.read_csv("Sample - Superstore.csv")
```

## Estado actual del notebook

Actualmente incluye:

- importacion de librerias,
- lectura del CSV,
- vista previa con `head()`,
- revision de tipos y nulos con `info()`.

## Posibles errores comunes

- `FileNotFoundError`: verifica que el archivo `Sample - Superstore.csv` este en la raiz del proyecto.
- `ModuleNotFoundError`: instala las dependencias del apartado **Instalacion rapida**.

## Siguientes pasos sugeridos

- Analizar ventas por categoria y subcategoria.
- Comparar ventas y ganancia por region.
- Evaluar descuentos y su impacto en la rentabilidad.
- Crear visualizaciones con `seaborn` y `matplotlib`.