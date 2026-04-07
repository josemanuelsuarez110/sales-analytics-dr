import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import datetime
import random
import os

# --- Configuration ---
# Using SQLite for portability as requested
DB_NAME = 'sales_data.db'
DB_PATH = os.path.join(os.getcwd(), 'sql', DB_NAME)
TABLE_NAME = 'raw_sales'

def generate_synthetic_data(num_records=2000):
    """
    Generates a synthetic dataset of sales records focused on Dominican Republic cities.
    Includes intentional noise (nulls) to demonstrate cleaning logic.
    """
    cities = [
        'Santo Domingo', 'Santiago', 'La Romana', 'Punta Cana', 
        'Puerto Plata', 'San Cristóbal', 'Higüey', 
        'San Francisco de Macorís', 'La Vega', 'San Pedro de Macorís'
    ]
    
    product_catalog = {
        101: {'Name': 'Arroz Selecto 5lb', 'Category': 'Alimentos', 'Price': 185.00},
        102: {'Name': 'Aceite Vegetal 1L', 'Category': 'Alimentos', 'Price': 240.00},
        103: {'Name': 'Café Molido 454g', 'Category': 'Bebidas', 'Price': 320.00},
        104: {'Name': 'Detergente en Polvo', 'Category': 'Limpieza', 'Price': 155.00},
        105: {'Name': 'Jabón de Cuaba', 'Category': 'Limpieza', 'Price': 45.00},
        106: {'Name': 'Refresco Gaseoso 2L', 'Category': 'Bebidas', 'Price': 90.00},
        107: {'Name': 'Salami Súper Especial', 'Category': 'Embutidos', 'Price': 210.00},
        108: {'Name': 'Queso Geo 1lb', 'Category': 'Lácteos', 'Price': 485.00}
    }
    
    data = []
    start_date = datetime.date(2024, 1, 1) # Full year 2024 + Q1 2025
    
    print(f"Generating {num_records} synthetic records...")
    
    for i in range(num_records):
        order_id = 5000 + i
        date = start_date + datetime.timedelta(days=random.randint(0, 450))
        customer_id = random.randint(1000, 1500)
        product_id = random.choice(list(product_catalog.keys()))
        quantity = random.randint(1, 12)
        unit_price = product_catalog[product_id]['Price']
        store_location = random.choice(cities)
        
        # Simulating data quality issues (Nulls in Quantity)
        if random.random() < 0.03: # 3% null rate
            quantity = None
            
        data.append({
            'OrderID': order_id,
            'Date': date,
            'CustomerID': customer_id,
            'ProductID': product_id,
            'Quantity': quantity,
            'UnitPrice': unit_price,
            'StoreLocation': store_location
        })
        
    return pd.DataFrame(data)

def clean_and_load(df):
    """
    Executes the cleaning logic and loads the data into the SQL database.
    """
    print("--- Starting Pipeline Logic ---")
    
    # 1. Verification of missing values
    null_count = df['Quantity'].isnull().sum()
    print(f"Detected {null_count} records with null Quantity.")
    
    # 2. Cleaning: Fill nulls with median quantity (Standard DE practice)
    df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())
    
    # 3. Create database engine
    engine = create_engine(f'sqlite:///{DB_PATH}')
    
    # 4. Load into 'raw_sales'
    try:
        df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)
        print(f"SUCCESS: Data loaded into '{TABLE_NAME}' in {DB_NAME}")
    except Exception as e:
        print(f"ERROR during loading: {e}")

if __name__ == '__main__':
    # Execute Pipeline
    raw_df = generate_synthetic_data(2500)
    clean_and_load(raw_df)
    print("ETL script execution finished.")
