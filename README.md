# EA1. Ingestión de Datos desde un API Objetivo - Proyecto Big Data

**Estudiante:** Justin Beckham Cardona Yepes  
**Asignatura:** Infraestructura y Arquitectura para Big Data — Proyecto integrador, Etapa 1  
**Institución:** Institución Universitaria Digital de Antioquia  

---

## 1. Descripción de la Solución
Este proyecto implementa el pipeline de **Ingesta de Datos** para la primera etapa del proyecto integrador. Se extraen los datos de países desde la API pública `REST Countries`, realizando una transformación a registros planos que se almacenan en una base de datos relacional analítica **SQLite** (`src/db/ingestion.db`).

Adicionalmente, se genera una muestra con los 50 países más poblados en formato Excel (`src/xlsx/ingestion.xlsx`) y un reporte de auditoría (`src/static/auditoria/ingestion.txt`) para verificar la conciliación de datos entre la API y la base de datos.

---

## 2. Estructura del Repositorio

```text
justin_cardona/
├── setup.py
├── .gitignore
├── README.md
├── .github/
│   └── workflows/
│       └── bigdata.yml
└── src/
    ├── static/
    │   └── auditoria/
    │       └── ingestion.txt
    ├── db/
    │   └── ingestion.db
    ├── xlsx/
    │   └── ingestion.xlsx
    └── ingestion.py 
```
---

## 3. Instrucciones de Instalación y Ejecución Local

1. **Clonar el repositorio:**

git clone https://github.com/justinbeckham1204/justin_cardona.git
cd justin_cardona


2. **Instalar dependencias:**

pip install requests pandas openpyxl


3. **Ejecutar el pipeline de ingesta:**

   python src/ingestion.py
---

## 4. Automatización con GitHub Actions
El flujo de trabajo automatizado se encuentra en `.github/workflows/bigdata.yml`. Se ejecuta automáticamente tras cada evento `push` o manualmente mediante `workflow_dispatch` desde la pestaña **Actions** en GitHub, generando los artefactos correspondientes.



# Proyecto Integrador Big Data - EA1 y EA2
**Estudiante:** Justin Cardona | **IU Digital**

## EA1: Ingesta
- Ingesta desde API REST Countries (250 países).
- Guardado en SQLite (`src/db/ingestion.db`).

## EA2: Preprocesamiento y Limpieza
- Proceso de limpieza e imputación en `src/cleaning.py`.
- Generación de `src/xlsx/cleaned_data.xlsx` y `src/static/auditoria/cleaning_report.txt`.
- Workflow en `.github/workflows/bigdata.yml`.


# EA2. Preprocesamiento y Limpieza de Datos en Plataforma de Big Data en la Nube

**Estudiante:** Justin Beckham Cardona Yepes  
**Asignatura:** Infraestructura y Arquitectura para Big Data — Proyecto integrador, Etapa 2  
**Institución:** Institución Universitaria Digital de Antioquia  

---

## 1. Descripción de la Solución
Este proyecto implementa la segunda etapa del pipeline de Big Data: **Preprocesamiento y Limpieza de Datos**. Se cargan los datos desde la base de datos relacional analítica SQLite (`src/db/ingestion.db`) simulando un entorno de procesamiento cloud.

Mediante el script `src/cleaning.py`, se realizan las siguientes validaciones y transformaciones:
* **Análisis Exploratorio:** Conteo inicial de registros, duplicados y valores nulos.
* **Eliminación de Duplicados:** Depuración por identificador único (`cca3`).
* **Imputación de Nulos:** Tratamiento de nulos mediante medianas en variables numéricas y valores por defecto en texto.
* **Corrección de Tipos y Escalado:** Conversión de tipos de datos y aplicación de normalización Min-Max.
* **Exportación de Evidencias:** Generación del Excel limpio (`src/xlsx/cleaned_data.xlsx`) y reporte de auditoría (`src/static/auditoria/cleaning_report.txt`).

---

## 2. Estructura del Repositorio

```text
justin_cardona/
├── setup.py
├── .gitignore
├── README.md
├── .github/
│   └── workflows/
│       └── bigdata.yml
└── src/
    ├── static/
    │   └── auditoria/
    │       ├── ingestion.txt
    │       └── cleaning_report.txt
    ├── db/
    │   └── ingestion.db
    ├── xlsx/
    │   ├── ingestion.xlsx
    │   └── cleaned_data.xlsx
    ├── ingestion.py
    └── cleaning.py
```

## 3. Instrucciones de Instalación y Ejecución Local

1. **Clonar el repositorio:**

git clone [https://github.com/justinbeckham1204/justin_cardona.git](https://github.com/justinbeckham1204/justin_cardona.git)
cd justin_cardona


2. **Instalar dependencias:**

pip install pandas openpyxl requests


3. **Ejecutar el script de preprocesamiento y limpieza (EA2):**

  python src/cleaning.py

  
## 4. Automatización con GitHub Actions

El flujo de trabajo automatizado se encuentra en .github/workflows/bigdata.yml. Se ejecuta automáticamente tras cada evento push a la rama main o de forma manual mediante workflow_dispatch, realizando la extracción, limpieza de datos y generación de artefactos de auditoría de forma 100% autónoma.
