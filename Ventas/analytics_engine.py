import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import os

def extraer_datos():
    """Conexión a base de datos y extracción de histórico con media móvil."""
    conn = sqlite3.connect("ecommerce_ventas.db")
    query = """
    SELECT 
        fecha, 
        total_ventas,
        AVG(total_ventas) OVER (ORDER BY fecha ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as media_movil_7d
    FROM ventas_historicas
    """
    df = pd.read_sql(query, conn, parse_dates=['fecha'])
    conn.close()
    return df

def ejecutar_forecast(df):
    """Procesamiento de serie temporal y aplicación de modelo Holt-Winters."""
    df = df.set_index('fecha').resample('D').sum()
    
    # Modelo de Suavizado Exponencial para datos con tendencia y estacionalidad
    modelo = ExponentialSmoothing(
        df['total_ventas'], 
        trend='add', 
        seasonal='add', 
        seasonal_periods=7
    ).fit()
    
    return modelo.forecast(180)

if __name__ == "__main__":
    print("Iniciando Motor de Inteligencia de Ventas...")
    
    # Crear directorio de resultados si no existe
    if not os.path.exists("Resultados"):
        os.makedirs("Resultados")
    
    # Extracción y Modelado
    datos = extraer_datos()
    prediccion = ejecutar_forecast(datos)
    
    # Estructuración y exportación de resultados
    df_forecast = prediccion.reset_index()
    df_forecast.columns = ['Fecha', 'Venta_Proyectada']
    
    ruta_excel = "Resultados/Proyecciones_Ventas_2026.xlsx"
    df_forecast.to_excel(ruta_excel, index=False)
    
    # Generación de visualización técnica
    plt.figure(figsize=(12, 6))
    plt.plot(datos['fecha'], datos['total_ventas'], label='Histórico', color='blue', alpha=0.5)
    plt.plot(prediccion.index, prediccion.values, label='Predicción IA (6 meses)', color='red', linewidth=2)
    plt.title('Análisis de Ventas: Histórico vs Proyección')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('Resultados/tendencia_ventas.png')
    
    print(f"Proceso finalizado. Archivo generado en: {ruta_excel}")