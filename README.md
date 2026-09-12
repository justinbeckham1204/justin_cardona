# Proyecto Integrador Big Data - EA1 y EA2
**Estudiante:** Justin Cardona | **IU Digital**

## EA1: Ingesta
- Ingesta desde API REST Countries (250 paises).
- Guardado en SQLite (`src/db/ingestion.db`).

## EA2: Preprocesamiento y Limpieza
- Proceso de limpieza e imputacion en `src/cleaning.py`.
- Generación de `src/xlsx/cleaned_data.xlsx` y `src/static/auditoria/cleaning_report.txt`.
- Workflow en `.github/workflows/bigdata.yml`.
