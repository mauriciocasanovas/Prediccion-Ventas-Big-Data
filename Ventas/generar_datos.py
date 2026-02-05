import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generar_dataset(db_name="ecommerce_ventas.db"):
    """Simulación de datos históricos de ventas con tendencias y estacionalidad."""
    
    # Configuración de parámetros temporales
    fecha_inicio = datetime(2024, 1, 1)
    dias = 730
    fechas = [fecha_inicio + timedelta(days=i) for i in range(dias)]
    
    # Parámetros de simulación
    np.random.seed(42)
    ventas_base = 500
    crecimiento_diario = 0.8
    ruido = np.random.normal(0, 40, dias)
    
    # Construcción del set de datos
    data = {
        'fecha': fechas,
        'total_ventas': [
            int(ventas_base + (i * crecimiento_diario) + (120 if f.weekday() >= 5 else 0) + r)
            for i, (f, r) in enumerate(zip(fechas, ruido))
        ],
        'transacciones': np.random.randint(45, 110, dias),
        'categoria': np.random.choice(['Electrónica', 'Hogar', 'Moda', 'Deportes'], dias)
    }
    
    df = pd.DataFrame(data)
    
    # Persistencia en SQLite
    conn = sqlite3.connect(db_name)
    df.to_sql('ventas_historicas', conn, if_exists='replace', index=False)
    conn.close()
    
    print(f"Base de datos '{db_name}' generada exitosamente con {len(df)} registros.")

if __name__ == "__main__":
    generar_dataset()