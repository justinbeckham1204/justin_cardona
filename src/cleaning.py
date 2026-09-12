import os
import sqlite3
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "src", "db", "ingestion.db")
XLSX_PATH = os.path.join(BASE_DIR, "src", "xlsx", "cleaned_data.xlsx")
AUDIT_PATH = os.path.join(BASE_DIR, "src", "static", "auditoria", "cleaning_report.txt")

def cargar_datos():
    conexion = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM paises", conexion)
    conexion.close()
    return df

def limpiar(df_raw):
    df_clean = df_raw.drop_duplicates(subset=['cca3']).copy()
    df_clean['capital'] = df_clean['capital'].fillna('Sin Capital Registrada')
    df_clean['poblacion'] = df_clean['poblacion'].fillna(df_clean['poblacion'].median()).astype(int)
    df_clean['area_km2'] = df_clean['area_km2'].fillna(df_clean['area_km2'].median()).astype(float)
    df_clean['densidad_poblacion'] = (df_clean['poblacion'] / df_clean['area_km2'].replace(0, 1)).round(2)
    return df_clean

if __name__ == "__main__":
    df_raw = cargar_datos()
    df_clean = limpiar(df_raw)
    df_clean.sort_values(by="poblacion", ascending=False).to_excel(XLSX_PATH, index=False)
    
    with open(AUDIT_PATH, "w", encoding="utf-8") as f:
        f.write(f"REPORTE DE AUDITORIA - EA2\nRegistros iniciales: {len(df_raw)}\nRegistros finales: {len(df_clean)}\nEstado: OK")
    print(f"Limpieza exitosa. Procesados: {len(df_clean)} paises")
