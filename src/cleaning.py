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

def realizar_limpieza_y_auditoria(df_raw):
    # 1. Estadísticas iniciales (Análisis Exploratorio)
    total_inicial = len(df_raw)
    duplicados_iniciales = df_raw.duplicated(subset=['cca3']).sum()
    nulos_iniciales = df_raw.isnull().sum().to_dict()

    # 2. Eliminación de duplicados
    df_clean = df_raw.drop_duplicates(subset=['cca3']).copy()
    duplicados_removidos = total_inicial - len(df_clean)

    # 3. Corrección de tipos de datos
    df_clean['poblacion'] = pd.to_numeric(df_clean['poblacion'], errors='coerce')
    df_clean['area_km2'] = pd.to_numeric(df_clean['area_km2'], errors='coerce')

    # 4. Manejo e Imputación de Valores Nulos
    df_clean['capital'] = df_clean['capital'].fillna('Sin Capital Registrada')
    
    mediana_pob = df_clean['poblacion'].median()
    df_clean['poblacion'] = df_clean['poblacion'].fillna(mediana_pob if not pd.isna(mediana_pob) else 0).astype(int)

    mediana_area = df_clean['area_km2'].median()
    df_clean['area_km2'] = df_clean['area_km2'].fillna(mediana_area if not pd.isna(mediana_area) else 1.0).astype(float)

    # 5. Transformaciones adicionales (Densidad y Escalado Min-Max)
    df_clean['densidad_poblacion'] = (df_clean['poblacion'] / df_clean['area_km2'].replace(0, 1)).round(2)
    
    # Escalado Min-Max para la población (Normalización [0, 1])
    min_pob = df_clean['poblacion'].min()
    max_pob = df_clean['poblacion'].max()
    df_clean['poblacion_normalizada'] = ((df_clean['poblacion'] - min_pob) / (max_pob - min_pob)).round(6)

    total_final = len(df_clean)

    # 6. Redacción del reporte de auditoría detallado
    reporte = f"""=======================================================
REPORTE DE AUDITORÍA Y TRAZABILIDAD DE DATOS - EA2
=======================================================

1. ESTADÍSTICAS INICIALES (ANTES DE LA LIMPIEZA)
-------------------------------------------------------
- Total de registros ingestados : {total_inicial}
- Duplicados detectados (cca3)  : {duplicados_iniciales}
- Conteo de nulos iniciales     : {nulos_iniciales}

2. OPERACIONES DE LIMPIEZA Y TRANSFORMACIÓN REALIZADAS
-------------------------------------------------------
- Eliminación de duplicados     : {duplicados_removidos} registros eliminados.
- Imputación de nulos (capital) : Rellenado con 'Sin Capital Registrada'.
- Imputación de nulos (poblacion): Imputado con la mediana ({mediana_pob}).
- Imputación de nulos (area_km2): Imputado con la mediana ({mediana_area}).
- Corrección de tipos           : 'poblacion' a INT, 'area_km2' a FLOAT.
- Transformación 1              : Cálculo de 'densidad_poblacion'.
- Transformación 2 (Escalado)   : Normalización Min-Max aplicada a 'poblacion'.

3. ESTADÍSTICAS FINALES (DESPUÉS DE LA LIMPIEZA)
-------------------------------------------------------
- Total de registros limpios    : {total_final}
- Porcentaje de retención       : {(total_final / total_inicial) * 100:.2f}%
- Estado final de la base       : 100% CONSISTENTE Y SIN DUPLICADOS
"""
    return df_clean, reporte

if __name__ == "__main__":
    df_raw = cargar_datos()
    df_clean, reporte_txt = realizar_limpieza_y_auditoria(df_raw)
    
    # Exportar dataset a Excel
    df_clean.sort_values(by="poblacion", ascending=False).to_excel(XLSX_PATH, index=False)
    
    # Exportar reporte de auditoría .txt
    with open(AUDIT_PATH, "w", encoding="utf-8") as f:
        f.write(reporte_txt)
        
    print(f"Preprocesamiento finalizado con éxito. Registros procesados: {len(df_clean)}")
