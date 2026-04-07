import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import time
import datetime
import logging
import os

# --- Configuración de Logging Corporativo ---
logging.basicConfig(
    filename='pipeline_execution.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

# --- Configuración de Base de Datos (Medallion DB) ---
DB_PATH = os.path.join('pipeline', 'sql', 'enterprise_sales.db')
engine = create_engine(f'sqlite:///{DB_PATH}')

def schema_validation(df, source_name):
    """
    Valida que los datos de entrada cumplan con el esquema esperado.
    """
    required_cols = ['OrderID', 'Date', 'Amount', 'Currency', 'Region']
    if not all(col in df.columns for col in required_cols):
        logging.error(f"FALLO DE ESQUEMA en fuente {source_name}")
        raise ValueError(f"Esquema inválido para {source_name}")
    return True

def ingest_source(name, currency, region, records=50):
    """
    Simula la ingesta desde una fuente heterogénea (API/DB Regional).
    """
    start_time = time.time()
    logging.info(f"Iniciando ingesta de fuente: {name} ({region})")
    
    # Simulación de datos multimoneda
    data = []
    base_date = datetime.date.today() - datetime.timedelta(days=1)
    
    for i in range(records):
        data.append({
            'OrderID': 70000 + i + (1000 if region == 'LATAM' else 2000),
            'Date': base_date,
            'Amount': np.random.uniform(50, 5000),
            'Currency': currency,
            'Region': region
        })
    
    df = pd.DataFrame(data)
    schema_validation(df, name)
    
    duration = time.time() - start_time
    logging.info(f"Fuente {name}: Procesadas {len(df)} filas en {duration:.2f}s")
    return df

def upsert_to_bronze(df):
    """
    Realiza un Upsert inteligente en la capa BRONCE.
    Actualiza si el OrderID existe, inserta si es nuevo.
    """
    logging.info("Iniciando UPSERT en Capa BRONZE (brz_sales)...")
    
    # 1. Cargar datos en tabla temporal
    df.to_sql('tmp_ingest', engine, if_exists='replace', index=False)
    
    with engine.connect() as conn:
        # 2. Borrar registros existentes para evitar duplicados en el INSERT (Lógica Upsert en SQLite)
        conn.execute(text("DELETE FROM brz_sales WHERE OrderID IN (SELECT OrderID FROM tmp_ingest)"))
        
        # 3. Insertar nuevos/actualizados
        conn.execute(text("INSERT INTO brz_sales SELECT * FROM tmp_ingest"))
        conn.commit()
    
    logging.info("SUCCESS: Upsert en Capa BRONZE completado.")

if __name__ == '__main__':
    # Creación de tablas base de ser necesario
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE IF NOT EXISTS brz_sales (OrderID INTEGER PRIMARY KEY, Date TEXT, Amount REAL, Currency TEXT, Region TEXT)"))
        conn.commit()

    logging.info("=== INICIO DE PIPELINE EMPRESARIAL ===")
    try:
        # Ingesta Multifuente (Simultánea/Secuencial)
        source_latam = ingest_source("API_Dominicana", "DOP", "LATAM")
        source_europe = ingest_source("ERP_España", "EUR", "EMEA")
        
        # Consolidación y Upsert
        consolidated_df = pd.concat([source_latam, source_europe])
        upsert_to_bronze(consolidated_df)
        
        logging.info("=== PIPELINE FINALIZADO CON ÉXITO ===")
        print("Pipeline ejecutado. Revisa 'pipeline_execution.log'.")
    except Exception as e:
        logging.critical(f"FALLO CRÍTICO EN PIPELINE: {e}")
        print(f"Error crítico: {e}")
