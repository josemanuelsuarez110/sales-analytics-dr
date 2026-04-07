import sqlite3
import os

# --- Paths ---
DB_PATH = os.path.join('sql', 'sales_data.db')
SQL_PATH = os.path.join('sql', 'star_schema_setup.sql')

def apply_transformations():
    if not os.path.exists(DB_PATH):
        print(f"Error: Database {DB_PATH} not found.")
        return

    if not os.path.exists(SQL_PATH):
        print(f"Error: SQL script {SQL_PATH} not found.")
        return

    print(f"Applying transformations to {DB_PATH}...")
    
    try:
        # Read the SQL script
        with open(SQL_PATH, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        # Connect and execute
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # executescript allows multiple SQL statements separated by ;
        cursor.executescript(sql_script)
        
        conn.commit()
        print("SUCCESS: Star Schema and Business Views created.")
        
        # Verify tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"Tables in DB: {[t[0] for t in tables]}")
        
    except sqlite3.Error as e:
        print(f"DATABASE ERROR: {e}")
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    apply_transformations()
