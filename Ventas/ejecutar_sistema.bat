@echo off
title Sistema de Inteligencia de Ventas - Proyeccion 2026
echo ==========================================================
echo   Iniciando Proceso de Forecasting y Analisis de Datos
echo ==========================================================
echo.

echo [1/2] Generando base de datos historica...
python generar_datos.py
if %errorlevel% neq 0 (echo Error en la generacion de datos & pause & exit)
echo.

echo [2/2] Ejecutando motor de prediccion Holt-Winters...
python analytics_engine.py
if %errorlevel% neq 0 (echo Error en el motor de analitica & pause & exit)
echo.

echo ==========================================================
echo   PROCESO FINALIZADO EXITOSAMENTE
echo   Resultados disponibles en la carpeta /Resultados
echo ==========================================================
pause