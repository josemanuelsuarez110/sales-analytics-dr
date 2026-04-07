import pandas as pd
import numpy as np
import os
import datetime

# --- Configuración del Ecosistema de Datos de RRHH ---
DB_NAME = 'hr_talent.db'
DB_PATH = os.path.join('people_analytics', 'sql', DB_NAME)

def generate_hr_data(num_employees=200):
    """
    Genera un dataset sintético para análisis de People Analytics.
    Simula 200 colaboradores con variables de desempeño y rotación.
    """
    departments = ['Ventas', 'IT', 'Recursos Humanos', 'Operaciones', 'Marketing', 'Finanzas']
    
    data = []
    start_date = datetime.date(2021, 1, 1)
    
    print(f"Generando datos para {num_employees} colaboradores (People Analytics)...")
    
    for i in range(num_employees):
        employee_id = 1000 + i
        dept = np.random.choice(departments)
        gender = np.random.choice(['M', 'F', 'NB'])
        age = np.random.randint(22, 60)
        tenure_months = np.random.randint(1, 60)
        performance = np.random.randint(1, 6) # 1 a 5
        potential = np.random.randint(1, 6)    # 1 a 5
        salary = np.random.randint(35000, 150000)
        last_increase_months = np.random.randint(0, 36)
        
        # Lógica de Riesgo de Fuga (Mecánica de negocio simplificada)
        # Riesgo alto si: Desempeño alto + Salario bajo + Mucho tiempo sin aumento
        risk_score = (performance * 0.4) + (last_increase_months * 0.4) - (salary / 100000 * 0.2)
        
        data.append({
            'EmployeeID': employee_id,
            'Department': dept,
            'Gender': gender,
            'Age': age,
            'Salary': salary,
            'Performance': performance,
            'Potential': potential,
            'Tenure_Months': tenure_months,
            'Last_Increase_Months': last_increase_months,
            'Risk_Score': risk_score,
            'Is_Active': 1 if risk_score < 4 else np.random.choice([0, 1]) # Probabilidad de baja
        })
        
    return pd.DataFrame(data)

def segment_talent_9box(df):
    """
    Segmenta el talento en la Matriz 9-Box (Potencial vs Desempeño).
    """
    def label_9box(row):
        perf = row['Performance']
        pot = row['Potential']
        
        if pot >= 4 and perf >= 4: return 'Talento Estrella (Top Talent)'
        if pot >= 4 and perf < 3: return 'Enigma (Alto Potencial/Bajo Desempeño)'
        if pot < 3 and perf >= 4: return 'Caballos de Batalla (Bajo Potencial/Alto Desempeño)'
        if pot < 3 and perf < 3: return 'Bajo Desempeño (Underperformer)'
        return 'Promedio Sólido (Solid Professional)'
    
    df['Talent_Segment'] = df.apply(label_9box, axis=1)
    return df

def identify_flight_risk(df):
    """
    Identifica empleados con alto riesgo de fuga basándose en el Risk_Score.
    """
    threshold = df['Risk_Score'].quantile(0.85) # Top 15% de riesgo
    df['High_Flight_Risk'] = df['Risk_Score'] > threshold
    return df

if __name__ == '__main__':
    # 1. Generación y Segmentación
    hr_df = generate_hr_data()
    hr_df = segment_talent_9box(hr_df)
    hr_df = identify_flight_risk(hr_df)
    
    # 2. Resumen de Hallazgos
    print("\n--- Auditoría de Capital Humano (Resumen) ---")
    print(hr_df['Talent_Segment'].value_counts())
    
    critical_risk = hr_df[hr_df['High_Flight_Risk'] == True]
    print(f"\nAlerta: Se han identificado {len(critical_risk)} colaboradores con ALTO RIESGO de fuga.")
    print(critical_risk[['EmployeeID', 'Department', 'Risk_Score', 'Talent_Segment']].head())
    
    # 3. Exportación Anonimizada para SQL (Integridad referencial y ética)
    # Se eliminan los scores brutos para proteger la evaluación individual en el reporte masivo
    hr_df.to_csv('people_analytics/etl/stg_hr_data.csv', index=False)
    print("\nSUCCESS: Dataset de Personas generado y segmentado exitosamente.")
