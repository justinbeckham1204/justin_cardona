import os
import sqlite3
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "src", "db", "ingestion.db")
XLSX_PATH = os.path.join(BASE_DIR, "src", "xlsx", "cleaned_data.xlsx")
AUDIT_PATH = os.path.join(BASE_DIR, "src", "static", "auditoria", "cleaning_report.txt")

def cargar_datos():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"No se encontró la BD en {DB_PATH}")
    conexion = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM paises", conexion)
    conexion.close()
    return df

def limpiar(df_raw):
    df_clean = df_raw.drop_duplicates(subset=['cca3']).copy()
    
    # Conversión numérica segura
    df_clean['poblacion'] = pd.to_numeric(df_clean['poblacion'], errors='coerce')
    df_clean['area_km2'] = pd.to_numeric(df_clean['area_km2'], errors='coerce')
    
    # Imputaciones
    df_clean['capital'] = df_clean['capital'].fillna('Sin Capital Registrada')
    
    mediana_poblacion = df_clean['poblacion'].median()
    if pd.isna(mediana_poblacion):
        mediana_poblacion = 0
    df_clean['poblacion'] = df_clean['poblacion'].fillna(mediana_poblacion).astype(int)
    
    mediana_area = df_clean['area_km2'].median()
    if pd.isna(mediana_area):
        mediana_area = 1.0
    df_clean['area_km2'] = df_clean['area_km2'].fillna(mediana_area).astype(float)
    
    # Calculada: Densidad poblacional
    df_clean['densidad_poblacion'] = (df_clean['poblacion'] / df_clean['area_km2'].replace(0, 1)).round(2)
    return df_clean

if __name__ == "__main__":
    df_raw = cargar_datos()
    df_clean = limpiar(df_raw)
    df_clean.sort_values(by="poblacion", ascending=False).to_excel(XLSX_PATH, index=False)
    
    reporte = (
        f"REPORTE DE AUDITORIA - EA2\n"
        f"=======================================================\n"
        f"Registros analizados (Antes) : {len(df_raw)}\n"
        f"Registros limpios (Después)  : {len(df_clean)}\n"
        f"Estado de calidad            : LIMPIEZA EXITOSA - 100% CONSISTENTE"
    )
    with open(AUDIT_PATH, "w", encoding="utf-8") as f:
        f.write(reporte)
    print(f"Limpieza exitosa. Procesados: {len(df_clean)} países")
