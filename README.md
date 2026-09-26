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



# EA3. Enriquecimiento de Datos en Plataforma de Big Data en la Nube - Proyecto Integrador Big Data - Pipeline de Procesamiento, Limpieza y Enriquecimiento (EA1, EA2 y EA3)

**Estudiante:** Justin Beckham Cardona Yepes  
**Asignatura:** Infraestructura y Arquitectura para Big Data  
**Institución:** Institución Universitaria Digital de Antioquia (IU Digital)  
**Repositorio:** [justin_cardona](https://github.comjustinbeckham1204/justin_cardona)  

---

## 📌 Resumen General del Proyecto
Este proyecto integrador consolida un pipeline de Big Data dividido en tres fases secuenciales y autónomas (**EA1, EA2 y EA3**), abarcando desde la ingesta inicial de una API pública hasta el preprocesamiento, limpieza y cruzado heterogéneo multiformato usando el estándar **`cca3`**.

---

## 🛠️ Estructura del Repositorio
El repositorio incluye los scripts de ingesta (`EA1`), limpieza (`EA2`) y enriquecimiento (`EA3`), además de las carpetas de bases de datos, fuentes raw, auditoría y los entregables en Excel.

---

## 🚀 Fases del Pipeline (Entregables Autónomos)
- **EA1. Ingestión de Datos:** Extracción desde la API `REST Countries`, persistencia en SQLite (`src/db/ingestion.db`) y generación de reportes.
- **EA2. Preprocesamiento y Limpieza:** Depuración de duplicados por `cca3`, imputación de nulos y normalización Min-Max.
- **EA3. Enriquecimiento Heterogéneo:** Integración relacional (Left Join por `cca3`) de 6 fuentes multiformato (JSON, CSV, XML, HTML, TXT, XLSX).

---


# Instrucciones de Clonación y Ejecución

### 1. Clonar el repositorio:
```bash
git clone https://github.com/justinbeckham1204/justin_cardona.git
cd justin_cardona
```

### 2. Instalar dependencias necesarias:
```bash
pip install requests pandas openpyxl lxml html5lib
```

### 3. Ejecutar los scripts de manera secuencial:
```bash
python src/ingestion.py   # Ingesta inicial (EA1)
python src/cleaning.py    # Limpieza y normalización (EA2)
python src/enrichment.py  # Enriquecimiento multiformato (EA3)
```

---

# Workflow Automatizado mediante GitHub Actions

El repositorio cuenta con una integración continua (CI/CD) configurada en `.github/workflows/bigdata.yml`.

### Funcionamiento del Workflow:

1. **Disparador (Trigger):** Se activa automáticamente con cada evento `push` sobre la rama `main` o mediante ejecución manual (`workflow_dispatch`).
2. **Entorno de Ejecución:** Aprovisiona una máquina virtual `ubuntu-latest` con Python 3.10.
3. **Instalación de Entorno:** Actualiza `pip` e instala las librerías `pandas`, `openpyxl`, `requests`, `lxml` y `html5lib`.
4. **Ejecución:** Ejecuta de forma autónoma el script `src/enrichment.py`.
5. **Persistencia:** Si se generan cambios en el archivo Excel unificado (`enriched_data.xlsx`) o en el reporte de trazabilidad (`enriched_report.txt`), el bot de GitHub Actions realiza un `commit` y un `push` automático reservando los artefactos actualizados en el repositorio.
Usa el código con precaución.

"""

# Escribir el nuevo contenido en el archivo README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_completo)

# Configurar Git y enviar los cambios al repositorio remoto
!git config user.email "{EMAIL}"
!git config user.name "{USER}"
!git remote set-url origin https://{TOKEN}@://github.com{USER}/{REPO}.git

!git add README.md
!git commit -m "Docs: Actualizacion completa y unificada del README.md incluyendo EA3"
!git push origin main --force







# EA4. Documentación de la Arquitectura y Modelo de Datos
Esta etapa consolida y documenta la arquitectura completa del proyecto (EA1, EA2 y EA3), explicando el flujo de datos desde la ingesta hasta el enriquecimiento, junto con el modelo de datos resultante del proceso de integración (esquema, relaciones y diagrama ER).

El documento completo se encuentra en:

 [`docs/arquitectura_modelo.pdf`]

Incluye:
- Descripción general de la arquitectura y sus componentes principales.
- Diagramas de flujo de ingesta, preprocesamiento y enriquecimiento.
- Modelo de datos (tablas, campos, relaciones PK/FK) y diagrama ER.
- Justificación de las herramientas utilizadas (SQLite, Pandas, PySpark, GitHub Actions).
- Explicación del flujo de datos y la automatización del pipeline.
- Conclusiones y recomendaciones para un entorno real de nube.

---

## Estructura del Repositorio

```text
justin_cardona/
├── setup.py
├── .gitignore
├── README.md
├── .github/
│   └── workflows/
│       └── bigdata.yml
├── src/
│   ├── static/
│   │   └── auditoria/
│   │       ├── ingestion.txt
│   │       ├── cleaning_report.txt
│   │       └── enriched_report.txt
│   ├── db/
│   │   └── ingestion.db
│   ├── xlsx/
│   │   ├── ingestion.xlsx
│   │   ├── cleaned_data.xlsx
│   │   └── enriched_data.xlsx
│   ├── ingestion.py
│   ├── cleaning.py
│   └── enrichment.py
└── docs/
    └── arquitectura_modelo.pdf
```

---

## ⚙️ Instrucciones de Instalación y Ejecución Local

1. **Clonar el repositorio:**

```bash
git clone https://github.com/justinbeckham1204/justin_cardona.git
cd justin_cardona
```

2. **Instalar dependencias necesarias:**

```bash
pip install requests pandas openpyxl lxml html5lib
```

3. **Ejecutar los scripts de manera secuencial:**

```bash
python src/ingestion.py   # Ingesta inicial (EA1)
python src/cleaning.py    # Limpieza y normalización (EA2)
python src/enrichment.py  # Enriquecimiento multiformato (EA3)
```

---

## 🤖 Workflow Automatizado mediante GitHub Actions

El repositorio cuenta con una integración continua (CI/CD) configurada en `.github/workflows/bigdata.yml`.

### Funcionamiento del Workflow:

1. **Disparador (Trigger):** Se activa automáticamente con cada evento `push` sobre la rama `main` o mediante ejecución manual (`workflow_dispatch`).
2. **Entorno de Ejecución:** Aprovisiona una máquina virtual `ubuntu-latest` con Python 3.10.
3. **Instalación de Entorno:** Actualiza `pip` e instala las librerías `pandas`, `openpyxl`, `requests`, `lxml` y `html5lib`.
4. **Ejecución:** Ejecuta de forma autónoma los scripts de ingesta, limpieza y enriquecimiento (`src/enrichment.py`, que depende del resultado de las etapas anteriores).
5. **Persistencia:** Si se generan cambios en los archivos Excel (`ingestion.xlsx`, `cleaned_data.xlsx`, `enriched_data.xlsx`) o en los reportes de trazabilidad, el bot de GitHub Actions realiza un `commit` y un `push` automático, dejando los artefactos actualizados en el repositorio sin intervención manual.
