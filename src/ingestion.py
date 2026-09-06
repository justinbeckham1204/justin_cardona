
import os
import sqlite3
import requests
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "src", "db", "ingestion.db")
XLSX_PATH = os.path.join(BASE_DIR, "src", "xlsx", "ingestion.xlsx")
AUDIT_PATH = os.path.join(BASE_DIR, "src", "static", "auditoria", "ingestion.txt")

# Usamos v2 de la API que responde de forma inmediata en servidores cloud
API_URL = "https://restcountries.com/v2/all"

def extraer_datos():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        respuesta = requests.get(API_URL, headers=headers, timeout=20)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            if isinstance(datos, list) and len(datos) > 0:
                return datos
    except Exception as e:
        print(f"Error en la petición API: {e}")
    return []

def transformar(datos_api):
    registros = []
    for pais in datos_api:
        if isinstance(pais, dict):
            # Formato compatible para API v2 / v3
            capital = pais.get("capital")
            if isinstance(capital, list) and len(capital) > 0:
                capital_val = capital[0]
            elif isinstance(capital, str):
                capital_val = capital
            else:
                capital_val = None

            nombre_comun = pais.get("name")
            if isinstance(nombre_comun, dict):
                nombre_comun = nombre_comun.get("common")

            registros.append({
                "cca3": pais.get("alpha3Code") or pais.get("cca3"),
                "nombre_comun": nombre_comun,
                "nombre_oficial": pais.get("nativeName") or nombre_comun,
                "capital": capital_val,
                "region": pais.get("region"),
                "subregion": pais.get("subregion"),
                "poblacion": pais.get("population"),
                "area_km2": pais.get("area"),
            })
    return registros

def cargar_en_sqlite(registros):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute("DROP TABLE IF EXISTS paises")
    cursor.execute('''
        CREATE TABLE paises (
            cca3            TEXT PRIMARY KEY,
            nombre_comun    TEXT NOT NULL,
            nombre_oficial  TEXT,
            capital         TEXT,
            region          TEXT,
            subregion       TEXT,
            poblacion       INTEGER,
            area_km2        REAL
        )
    ''')
    cursor.executemany('''
        INSERT OR REPLACE INTO paises
        (cca3, nombre_comun, nombre_oficial, capital, region,
         subregion, poblacion, area_km2)
        VALUES (:cca3, :nombre_comun, :nombre_oficial, :capital,
                :region, :subregion, :poblacion, :area_km2)
    ''', registros)
    conexion.commit()
    conexion.close()

def generar_muestra():
    os.makedirs(os.path.dirname(XLSX_PATH), exist_ok=True)
    conexion = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(
        "SELECT * FROM paises ORDER BY poblacion DESC", conexion
    )
    conexion.close()
    df.head(50).to_excel(XLSX_PATH, index=False)
    return df

def generar_auditoria(registros_api, df_bd):
    os.makedirs(os.path.dirname(AUDIT_PATH), exist_ok=True)
    claves_api = {r["cca3"] for r in registros_api if r.get("cca3")}
    claves_bd = set(df_bd["cca3"])
    faltantes = claves_api - claves_bd
    sobrantes = claves_bd - claves_api
    poblacion_api = sum(r["poblacion"] or 0 for r in registros_api)
    poblacion_bd = int(df_bd["poblacion"].fillna(0).sum())

    lineas = [
        "REPORTE DE AUDITORIA - ETAPA DE INGESTA",
        "=" * 55,
        f"Registros extraidos del API      : {len(registros_api)}",
        f"Registros almacenados en SQLite  : {len(df_bd)}",
        f"Claves en API y no en BD         : {sorted(faltantes) or 'ninguna'}",
        f"Claves en BD y no en API         : {sorted(sobrantes) or 'ninguna'}",
        f"Suma de poblacion (API)          : {poblacion_api}",
        f"Suma de poblacion (BD)           : {poblacion_bd}",
        f"Integridad de conteo             : "
        f"{'OK' if len(registros_api) == len(df_bd) else 'DIFERENCIA DETECTADA'}",
        f"Integridad de campo clave        : "
        f"{'OK' if not faltantes and not sobrantes else 'DIFERENCIA DETECTADA'}",
    ]
    with open(AUDIT_PATH, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas))

if __name__ == "__main__":
    datos = extraer_datos()
    registros = transformar(datos)
    cargar_en_sqlite(registros)
    df = generar_muestra()
    generar_auditoria(registros, df)
    print(f"Ingesta completada: {len(registros)} países procesados exitosamente.")
