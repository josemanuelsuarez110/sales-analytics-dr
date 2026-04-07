import pandas as pd
import numpy as np
import json
import os
import datetime
import logging

# --- Configuración Master Solution ---
LOG_FILE = 'master_execution.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

# --- Fuentes de Datos (Simuladas / Integradas) ---
def get_integrated_data():
    """
    Consolidación de métricas de los 3 dominios principales.
    """
    logging.info("Iniciando consolidación de datos maestros...")
    
    # 1. Métricas de Ventas (Económico)
    sales_metrics = {
        'total_revenue_usd': 1250000,
        'revenue_growth_wow': 12.5,
        'top_region': 'LATAM',
        'sales_history': [
            {'month': 'Jan', 'amount': 150000},
            {'month': 'Feb', 'amount': 220000},
            {'month': 'Mar', 'amount': 280000},
            {'month': 'Apr', 'amount': 240000},
            {'month': 'May', 'amount': 360000},
        ]
    }
    
    # 2. Métricas de Talento (Capital Humano)
    talent_metrics = {
        'headcount': 250,
        'turnover_rate': 4.2,
        'high_potential_pct': 18,
        'talent_grid': [
            {'segment': 'Top Talent', 'count': 45},
            {'segment': 'Solid Prof', 'count': 120},
            {'segment': 'Underperf', 'count': 15},
            {'segment': 'Enigma', 'count': 70},
        ]
    }
    
    # 3. Métricas de Impacto Social (Open Data)
    social_metrics = {
        'internet_gap_years': 4.1,
        'social_correlation': 0.82,
        'impact_recommendation': 'Invertir 1% en TICs rurales incrementa 5% escolaridad.',
        'education_by_region': [
            {'region': 'Urban', 'years': 12.4},
            {'region': 'Rural', 'years': 8.3},
        ]
    }
    
    return {
        'last_updated': str(datetime.datetime.now()),
        'sales': sales_metrics,
        'talent': talent_metrics,
        'social': social_metrics
    }

def export_for_dashboard(data):
    """
    Exporta la fuente de la verdad para el frontend de Next.js.
    """
    try:
        # Ruta para que el frontend pueda leerlo (Public Assets)
        export_path = os.path.join('frontend', 'public', 'data', 'dashboard_data.json')
        
        # Aseguramos que el directorio exista
        os.makedirs(os.path.dirname(export_path), exist_ok=True)
        
        with open(export_path, 'w') as f:
            json.dump(data, f, indent=4)
        
        logging.info(f"SUCCESS: Datos exportados exitosamente en {export_path}")
        print(f"Datos maestros listos en: {export_path}")
    except Exception as e:
        logging.error(f"FALLO DE EXPORTACIÓN: {e}")
        raise

if __name__ == '__main__':
    logging.info("=== INICIO DE ORQUESTACIÓN MAESTRA (Full-Stack) ===")
    try:
        data_master = get_integrated_data()
        export_for_dashboard(data_master)
        logging.info("=== ORQUESTACIÓN FINALIZADA CON ÉXITO ===")
    except Exception as e:
        logging.critical(f"FALLO CRÍTICO EN SOLUCIÓN MAESTRA: {e}")
        print(f"Error: {e}")
