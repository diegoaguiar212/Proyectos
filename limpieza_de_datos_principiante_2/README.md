# Limpieza de Datos - FIFA 21

Este proyecto contiene un ejercicio de limpieza de datos usando un dataset de jugadores de FIFA 21 obtenido desde Kaggle.

Notebook principal: `limpieza_de_datos.ipynb`
Dataset: `fifa21 raw data v2.csv`

## Objetivo

Transformar columnas con formatos inconsistentes (texto, unidades, simbolos y fechas) en variables limpias y utiles para el analisis.

## Fuente de datos

- Dataset: FIFA 21 messy raw dataset for cleaning/exploring
- Kaggle: https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring?resource=download

## Problemas identificados

En el notebook se detectan y corrigen los siguientes puntos:

1. Columnas numericas guardadas como texto:
- Value
- Wage
- Release Clause
- Height
- Weight
- Hits

2. Columnas de fecha guardadas como texto:
- Joined
- Loan Date End (se analiza, pero se mantiene por alta presencia de NA)

3. Formato de valoraciones con estrella en:
- W/F
- SM
- IR

4. Columna Contract en formato compuesto (inicio~fin), que se separa en dos columnas.

## Limpieza aplicada

### 1) Conversion de monetarios, altura, peso y hits

Se crean funciones para parsear distintos formatos:

- `parse_money`: convierte valores como `€1.5M`, `€500K` o `-` a numero en EUR.
- `parse_height_cm`: convierte alturas de pies/pulgadas o cm a centimetros.
- `parse_weight_kg`: convierte peso desde `lbs` a kilogramos.
- `parse_hits`: convierte valores como `1.2K` a numerico.

Se generan columnas limpias:

- `Value_EUR`
- `Wage_EUR`
- `Release Clause_EUR`
- `Height_cm`
- `Weight_kg`
- `Hits` (convertida a numerica)

Luego se eliminan las columnas originales ya reemplazadas.

### 2) Separacion de Contract

La columna `Contract` se divide en:

- `contract_begins`
- `contract_ends`

Ambas quedan en formato entero anulable (`Int64`) extrayendo anios (`YYYY`).

### 3) Conversion de Joined

La columna `Joined` se convierte con `pd.to_datetime(..., errors='coerce')`, dejando como `NaT` los valores no parseables.

### 4) Limpieza de W/F, SM e IR

Se elimina el simbolo de estrella y se convierten a tipo numerico (`Int64`).

### 5) Estandarizacion final

Se normalizan nombres de columnas a:

- minusculas
- separacion por guion bajo (`_`)

## Resultado

El DataFrame final (`df_limpio`) queda listo para analisis, con tipos de datos consistentes y variables clave en formato adecuado.

## Requisitos

- Python 3.x
- pandas
- numpy
- Jupyter Notebook

Instalacion sugerida:

```bash
pip install pandas numpy notebook
```

## Como ejecutar

1. Abrir `limpieza_de_datos.ipynb`.
2. Verificar que `fifa21 raw data v2.csv` este en la misma carpeta.
3. Ejecutar las celdas en orden para reproducir todo el proceso de limpieza.

## Estructura de la carpeta

```text
limpieza_de_datos_principiante_2/
|-- fifa21 raw data v2.csv
|-- limpieza_de_datos.ipynb
|-- README.md
```
