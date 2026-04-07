import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import os

# --- Configuration ---
DB_PATH = os.path.join('sql', 'sales_data.db')
engine = create_engine(f'sqlite:///{DB_PATH}')

def detect_anomalies(df, column='Revenue', threshold=3):
    """
    Identifica anomalías utilizando el método estadístico Z-Score.
    Z = (X - Mean) / StdDev
    Valores con Z > 3 son considerados outliers (99.7% de confianza).
    """
    mean = df[column].mean()
    std = df[column].std()
    
    df['Z_Score'] = (df[column] - mean) / std
    df['Is_Anomaly'] = np.abs(df['Z_Score']) > threshold
    
    anomalies = df[df['Is_Anomaly'] == True]
    return anomalies

def time_series_analysis():
    """
    Analiza la tendencia de ventas y promedios móviles (Moving Averages).
    """
    query = """
    SELECT Date, SUM(Revenue) as DailySales
    FROM Fact_Sales
    GROUP BY Date
    ORDER BY Date ASC
    """
    df = pd.read_sql(query, engine)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Cálculo de Promedios Móviles (7 días y 30 días)
    df['MA_7'] = df['DailySales'].rolling(window=7).mean()
    df['MA_30'] = df['DailySales'].rolling(window=30).mean()
    
    print("\n--- Análisis de Tendencias Temporales ---")
    print(df[['Date', 'DailySales', 'MA_7', 'MA_30']].tail(10))
    
    return df

if __name__ == '__main__':
    print("Iniciando Análisis de Datos Avanzado (Arquitectura Senior)")
    
    # 1. Carga de datos de ventas
    try:
        sales_df = pd.read_sql("SELECT * FROM Fact_Sales", engine)
        
        # 2. Detección de Anomalías
        outliers = detect_anomalies(sales_df)
        print(f"\nSe detectaron {len(outliers)} transacciones anómalas (Z-Score > 3):")
        if not outliers.empty:
            print(outliers[['OrderID', 'Date', 'Revenue', 'Z_Score']].head())
        
        # 3. Análisis de Tendencias
        trend_df = time_series_analysis()
        
        print("\nSUCCESS: Análisis avanzado completado.")
        
    except Exception as e:
        print(f"Error durante el análisis: {e}")

