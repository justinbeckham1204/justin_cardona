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


4. Haz clic en el botón verde **Commit changes...** arriba a la derecha para guardar.

---



