import sqlite3
import os

# --- Configuración ---
DB_PATH = os.path.join('sql', 'sales_data.db')

def verify_database():
    """
    Realiza una auditoría rápida de las tablas y vistas creadas.
    """
    if not os.path.exists(DB_PATH):
        print(f"Error: Base de datos {DB_PATH} no encontrada.")
        return

    print("--- INICIO DE AUDITORÍA DE DATOS ---")
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # 1. Conteo de tablas
        tabs_to_check = ['raw_sales', 'Dim_Productos', 'Dim_Clientes', 'Dim_Calendario', 'Fact_Sales']
        for table in tabs_to_check:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"- Tabla [{table}]: {count} registros.")
            
        # 2. Verificación de Vista y Cálculo de ITBIS
        print("\n--- Verificando cálculos en Vista: v_sales_performance ---")
        cursor.execute("""
            SELECT OrderID, ProductName, Revenue, ITBIS_Amount, Total_With_Tax 
            FROM v_sales_performance 
            LIMIT 3
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(f"Order: {row[0]} | Prod: {row[1]} | Rev: {row[2]} | ITBIS: {row[3]} | Total: {row[4]}")
            # Verificación rápida del 18%
            calc_itbis = round(row[2] * 0.18, 2)
            if abs(calc_itbis - row[3]) < 0.01:
                print("  [OK] Cálculo de ITBIS correcto.")
            else:
                print(f"  [Error] Desajuste en ITBIS. Calc: {calc_itbis}, BD: {row[3]}")

        print("\n--- Auditoría Completa ---")
        
    except sqlite3.Error as e:
        print(f"ERROR DE BASE DE DATOS: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    verify_database()
