======================================================================================
SISTEMA INTEGRAL DE INTELIGENCIA DE VENTAS & FORECASTING PRO
======================================================================================

DESCRIPCION:
Este proyecto es una solucion integral de Ciencia de Datos aplicada al 
E-commerce. Utiliza Inteligencia Artificial para predecir la demanda futura 
(Forecasting) mediante algoritmos de series temporales, permitiendo una 
planificacion financiera y de stock basada en datos de alta precision.

ESTRUCTURA DEL PROYECTO:

1. ecommerce_ventas.db (Motor de Datos):
   Base de datos SQLite que centraliza la informacion historica de 
   transacciones, productos y comportamiento estacional de ventas.

2. generar_datos.py (Simulador de Entorno):
   Script encargado de crear el ecosistema de datos con historial de ventas, 
   tendencias de crecimiento y estacionalidad.

3. analytics_engine.py (Cerebro del Sistema):
   Script unificado que realiza el ciclo completo de datos:
   - Extraccion mediante consultas SQL Avanzadas (Window Functions).
   - Analisis de estacionalidad con Pandas.
   - Ejecucion del modelo de IA (Holt-Winters) para la prediccion a 6 meses.
   - Exportacion automatica de resultados a la carpeta /Resultados.

4. ejecutar_sistema.bat (Lanzador de Automatizacion):
   Archivo ejecutable que permite correr el flujo completo (generacion de datos 
   y motor de analitica) de forma secuencial con un solo clic.

5. Reporte_Prediccion.pbix (Dashboard):
   Tablero interactivo principal que consume las proyecciones generadas. 
   Incluye analisis de tendencia, indicadores de cumplimiento (Gauge/Velocimetro), 
   KPIs de performance y analisis de picos de venta mediante filtros Top N.

6. Carpeta Resultados:
   - Proyecciones_Ventas_2026.xlsx: Informe detallado con el forecast diario.
   - tendencia_ventas.png: Grafico de la comparativa historica vs proyeccion.

TECNOLOGIAS UTILIZADAS:
- Python 3.x (Lenguaje principal)
- SQL / SQLite3 (Gestion de base de datos relacional avanzada)
- Statsmodels (Modelo de IA Holt-Winters para Series Temporales)
- Pandas & Matplotlib (Ingenieria de datos y graficos)
- Power BI Desktop (Visualizacion avanzada)

VALOR AGREGADO:
- Identificacion de tendencias de mercado y picos de venta antes de que ocurran.
- Optimizacion de toma de decisiones mediante velocimetro de metas (KPIs).
- Pipeline completo: desde la generacion del dato hasta el Dashboard final.

======================================================================================