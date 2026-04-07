import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime
import random
import os
import logging

# --- Configuración de Logging ---
logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# --- Configuración de Bases de Datos ---
DB_PATH = os.path.join('sql', 'sales_data.db')
engine = create_engine(f'sqlite:///{DB_PATH}')

def extract_multi_source():
    """
    Simula la extracción de múltiples fuentes (API, CSV, Generación Dinámica).
    """
    logging.info("Iniciando fase de EXTRACCIÓN (Multi-source)...")
    try:
        # Fuente 1: Generación Dinámica (Ventas del día actual)
        today = datetime.date.today()
        new_records = 20
        data = []
        for i in range(new_records):
            data.append({
                'OrderID': 9000 + i + random.randint(1, 1000),
                'Date': today,
                'CustomerID': random.randint(1000, 1500),
                'ProductID': random.randint(101, 108),
                'Quantity': random.randint(1, 5),
                'UnitPrice': random.choice([100, 250, 500]),
                'StoreLocation': random.choice(['Santo Domingo', 'Santiago'])
            })
        df = pd.DataFrame(data)
        logging.info(f"F1: Generados {new_records} registros dinámicos.")
        return df
    except Exception as e:
        logging.error(f"Fallo en la extracción: {e}")
        raise

def data_quality_validation(df):
    """
    Reglas de Calidad de Datos (Data Quality) antes de la carga.
    """
    logging.info("Iniciando fase de VALIDACIÓN (Data Quality)...")
    
    # 1. Detección de Nulos
    if df.isnull().values.any():
        null_rows = df[df.isnull().any(axis=1)]
        logging.warning(f"Se detectaron {len(null_rows)} registros con nulos. Limpiando...")
        df = df.dropna()
        
    # 2. Detección de Duplicados
    df = df.drop_duplicates(subset=['OrderID'])
    
    logging.info("Validación completada sin errores críticos.")
    return df

def load_to_staging(df):
    """
    Carga de datos crudos en la Capa de Staging (SQL).
    """
    logging.info("Iniciando fase de CARGA (Staging Layer)...")
    try:
        df.to_sql('stg_sales', engine, if_exists='replace', index=False)
        logging.info("SUCCESS: Datos cargados en 'stg_sales' exitosamente.")
    except Exception as e:
        logging.error(f"Error en la carga a Staging: {e}")
        raise

if __name__ == '__main__':
    logging.info("=== INICIO DE ORQUESTACIÓN DIARIA ===")
    try:
        raw_data = extract_multi_source()
        clean_data = data_quality_validation(raw_data)
        load_to_staging(clean_data)
        logging.info("=== ORQUESTACIÓN FINALIZADA CON ÉXITO ===")
        print("Automatización ejecutada. Revisa 'automation.log' para detalles.")
    except Exception as e:
        logging.critical(f"ORQUESTACIÓN FALLIDA: {e}")
        print("Error en el proceso. Revisa los logs.")
