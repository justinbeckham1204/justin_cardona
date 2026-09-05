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
