# 📧 Clasificación de Correos en SPAM / NOT SPAM

Proyecto de Machine Learning que entrena un modelo **Random Forest** para clasificar correos electrónicos como **SPAM** o **NOT SPAM**, usando el dataset **Spambase** de la UCI. Incluye además una función para predecir sobre textos nuevos ingresados manualmente.

---

## 📂 Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `clasificacion_spam.ipynb` | Notebook principal con todo el flujo |
| `spambase.data` | Dataset de entrenamiento (UCI Spambase) |

---

## 📊 Datos utilizados

**Dataset:** [Spambase – UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Spambase)

| Propiedad | Detalle |
|---|---|
| Archivo | `spambase.data` |
| Total de registros | 4.601 correos electrónicos |
| Variables predictoras | 57 |
| Variable objetivo | `is_spam` (1 = spam, 0 = no spam) |

### Variables predictoras (57):

| Grupo | Cantidad | Descripción |
|---|---|---|
| `word_freq_*` | 48 | % de aparición de palabras clave como `free`, `money`, `credit`, `business`, etc. |
| `char_freq_*` | 6 | % de aparición de caracteres: `;` `(` `[` `!` `$` `#` |
| `capital_run_length_average` | 1 | Longitud promedio de secuencias en mayúsculas |
| `capital_run_length_longest` | 1 | Secuencia más larga en mayúsculas |
| `capital_run_length_total` | 1 | Total de caracteres en mayúsculas |

---

## 🔄 Flujo del proyecto

1. **Carga de datos**: lectura del CSV con 58 columnas asignadas manualmente.
2. **Preparación**: separación de features (`X`) y variable objetivo (`y = is_spam`).
3. **División**: 80% entrenamiento / 20% prueba (`random_state=42`).
4. **Entrenamiento**: `RandomForestClassifier(n_estimators=100, random_state=42)`.
5. **Evaluación**:
   - `classification_report` (precision, recall, f1-score por clase)
   - `accuracy_score` global
6. **Importancia de variables**: top 10 features más relevantes del modelo.
7. **Predicción sobre texto libre**:
   - `extract_features(text)`: convierte texto crudo en vector de 57 features.
   - `predict_spam(text)`: devuelve `"SPAM"` o `"NOT SPAM"`.

---

## 🧪 Ejemplos de predicción

**Email SPAM:**
```
SUBJECT: URGENT BUSINESS PROPOSAL
FREE MONEY NOW! Click here to receive your credit today.
Do not miss this limited technology offer !!! $$$
→ Predicción: SPAM
```

**Email legítimo:**
```
SUBJECT: Question about your product
I am interested in learning more about the IPhone 15 you are offering...
→ Predicción: NOT SPAM
```

---

## ▶️ Cómo ejecutar

1. Instalar dependencias:
   ```bash
   pip install pandas numpy scikit-learn jupyter
   ```
2. Abrir el notebook:
   ```bash
   jupyter notebook clasificacion_spam.ipynb
   ```
3. Ejecutar las celdas en orden de arriba hacia abajo.