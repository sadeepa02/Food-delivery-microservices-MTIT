@echo off
set "PYTHON=python"
if exist "venv\Scripts\python.exe" set "PYTHON=venv\Scripts\python.exe"

echo ============================================
echo   Food Delivery System - Starting Services
echo ============================================
echo.

echo [1/6] Starting Restaurant Service on port 8001...
start "Restaurant Service" cmd /k "cd restaurant-service && %PYTHON% main.py"
timeout /t 2 /nobreak >nul

echo [2/6] Starting Menu Service on port 8002...
start "Menu Service" cmd /k "cd menu-service && %PYTHON% main.py"
timeout /t 2 /nobreak >nul

echo [3/6] Starting Order Service on port 8003...
start "Order Service" cmd /k "cd order-service && %PYTHON% main.py"
timeout /t 2 /nobreak >nul

echo [4/6] Starting Delivery Service on port 8004...
start "Delivery Service" cmd /k "cd delivery-service && %PYTHON% main.py"
timeout /t 2 /nobreak >nul

echo [5/6] Starting Payment Service on port 8005...
start "Payment Service" cmd /k "cd payment-service && %PYTHON% main.py"
timeout /t 2 /nobreak >nul

echo [6/6] Starting API Gateway on port 8000...
start "API Gateway" cmd /k "cd gateway && %PYTHON% main.py"
timeout /t 3 /nobreak >nul

echo.
echo ============================================
echo   All services started successfully!
echo ============================================
echo.
echo   API Gateway:          http://localhost:8000
echo   Gateway Swagger:      http://localhost:8000/docs
echo   Restaurant Service:   http://localhost:8001/docs
echo   Menu Service:         http://localhost:8002/docs
echo   Order Service:        http://localhost:8003/docs
echo   Delivery Service:     http://localhost:8004/docs
echo   Payment Service:      http://localhost:8005/docs
echo.
pause
