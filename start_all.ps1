# Food Delivery System - PowerShell Startup Script
# Run with: .\start_all.ps1

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Food Delivery System - Starting Services" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

$root = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "[1/6] Starting Restaurant Service on port 8001..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\restaurant-service'; python main.py" -WindowStyle Normal

Start-Sleep -Seconds 2

Write-Host "[2/6] Starting Menu Service on port 8002..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\menu-service'; python main.py" -WindowStyle Normal

Start-Sleep -Seconds 2

Write-Host "[3/6] Starting Order Service on port 8003..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\order-service'; python main.py" -WindowStyle Normal

Start-Sleep -Seconds 2

Write-Host "[4/6] Starting Delivery Service on port 8004..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\delivery-service'; python main.py" -WindowStyle Normal

Start-Sleep -Seconds 2

Write-Host "[5/6] Starting Payment Service on port 8005..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\payment-service'; python main.py" -WindowStyle Normal

Start-Sleep -Seconds 2

Write-Host "[6/6] Starting API Gateway on port 8000..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$root\gateway'; python main.py" -WindowStyle Normal

Start-Sleep -Seconds 3

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "  All services started!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "  API Gateway:          http://localhost:8000" -ForegroundColor White
Write-Host "  Gateway Swagger:      http://localhost:8000/docs" -ForegroundColor White
Write-Host "  Restaurant Service:   http://localhost:8001/docs" -ForegroundColor White
Write-Host "  Menu Service:         http://localhost:8002/docs" -ForegroundColor White
Write-Host "  Order Service:        http://localhost:8003/docs" -ForegroundColor White
Write-Host "  Delivery Service:     http://localhost:8004/docs" -ForegroundColor White
Write-Host "  Payment Service:      http://localhost:8005/docs" -ForegroundColor White
Write-Host ""
Write-Host "  Close the individual terminal windows to stop services." -ForegroundColor Gray
