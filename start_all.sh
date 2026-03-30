#!/bin/bash

echo "============================================"
echo "  Food Delivery System - Starting Services"
echo "============================================"
echo ""

# Kill any existing processes on our ports
for port in 8000 8001 8002 8003 8004 8005; do
  lsof -ti:$port | xargs kill -9 2>/dev/null || true
done

echo "[1/6] Starting Restaurant Service on port 8001..."
cd restaurant-service && python main.py &
cd ..
sleep 1

echo "[2/6] Starting Menu Service on port 8002..."
cd menu-service && python main.py &
cd ..
sleep 1

echo "[3/6] Starting Order Service on port 8003..."
cd order-service && python main.py &
cd ..
sleep 1

echo "[4/6] Starting Delivery Service on port 8004..."
cd delivery-service && python main.py &
cd ..
sleep 1

echo "[5/6] Starting Payment Service on port 8005..."
cd payment-service && python main.py &
cd ..
sleep 1

echo "[6/6] Starting API Gateway on port 8000..."
cd gateway && python main.py &
cd ..
sleep 2

echo ""
echo "============================================"
echo "  All services started!"
echo "============================================"
echo ""
echo "  API Gateway:          http://localhost:8000"
echo "  Gateway Swagger:      http://localhost:8000/docs"
echo "  Restaurant Service:   http://localhost:8001/docs"
echo "  Menu Service:         http://localhost:8002/docs"
echo "  Order Service:        http://localhost:8003/docs"
echo "  Delivery Service:     http://localhost:8004/docs"
echo "  Payment Service:      http://localhost:8005/docs"
echo ""
echo "Press Ctrl+C to stop all services."
wait
