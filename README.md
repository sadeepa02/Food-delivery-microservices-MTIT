# 🍕 Food Delivery System — Microservices with API Gateway

A complete microservices backend built with **Python FastAPI**, following the API Gateway pattern.

## 📁 Project Structure

```
food-delivery/
├── restaurant-service/       ← Port 8001
│   ├── main.py
│   ├── models.py
│   ├── data_service.py
├── menu-service/             ← Port 8002
│   ├── main.py
│   ├── models.py
│   ├── data_service.py
├── order-service/            ← Port 8003
│   ├── main.py
│   ├── models.py
│   ├── data_service.py
├── delivery-service/         ← Port 8004
│   ├── main.py
│   ├── models.py
│   ├── data_service.py
├── payment-service/          ← Port 8005
│   ├── main.py
│   ├── models.py
│   ├── data_service.py
├── gateway/                  ← Port 8000 (single entry point)
│   ├── main.py
│   ├── proxy.py
│   └── routes.py
├── requirements.txt
├── start_all.bat             ← Windows startup script
├── start_all.sh              ← Linux/Mac startup script
└── README.md
```

## ⚙️ Setup & Installation

### 1. Create and activate virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start all services

**Windows:**
```bash
start_all.bat
```

**Linux / Mac:**
```bash
chmod +x start_all.sh
./start_all.sh
```

### 4. Or start individually

```bash
# Terminal 1
cd restaurant-service && python main.py

# Terminal 2
cd menu-service && python main.py

# Terminal 3
cd order-service && python main.py

# Terminal 4
cd delivery-service && python main.py

# Terminal 5
cd payment-service && python main.py

# Terminal 6 - Gateway (start last)
cd gateway && python main.py
```

## 🌐 Service URLs

| Service            | Direct URL                          | Via Gateway                              |
|--------------------|-------------------------------------|------------------------------------------|
| API Gateway        | http://localhost:8000/docs          | —                                        |
| Restaurant Service | http://localhost:8001/docs          | http://localhost:8000/api/v1/restaurants |
| Menu Service       | http://localhost:8002/docs          | http://localhost:8000/api/v1/menu        |
| Order Service      | http://localhost:8003/docs          | http://localhost:8000/api/v1/orders      |
| Delivery Service   | http://localhost:8004/docs          | http://localhost:8000/api/v1/deliveries  |
| Payment Service    | http://localhost:8005/docs          | http://localhost:8000/api/v1/payments    |

## 📡 API Endpoints

### 🍽️ Restaurant Service (Port 8001)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /restaurants | Get all restaurants |
| GET | /restaurants/{id} | Get restaurant by ID |
| POST | /restaurants | Add new restaurant |
| PUT | /restaurants/{id} | Update restaurant |
| DELETE | /restaurants/{id} | Delete restaurant |

### 📋 Menu Service (Port 8002)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /menu | Get all menu items |
| GET | /menu/{id} | Get item by ID |
| GET | /menu/restaurant/{id} | Get menu by restaurant |
| POST | /menu | Add menu item |
| PUT | /menu/{id} | Update menu item |
| DELETE | /menu/{id} | Delete menu item |

### 🛒 Order Service (Port 8003)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /orders | Get all orders |
| GET | /orders/{id} | Get order by ID |
| GET | /orders/restaurant/{id} | Orders by restaurant |
| POST | /orders | Place new order |
| PATCH | /orders/{id}/status | Update order status |
| DELETE | /orders/{id} | Cancel order |

### 🚴 Delivery Service (Port 8004)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /deliveries | Get all deliveries |
| GET | /deliveries/{id} | Get delivery by ID |
| GET | /deliveries/order/{id} | Track by order |
| POST | /deliveries | Assign delivery |
| PATCH | /deliveries/{id}/status | Update delivery status |
| DELETE | /deliveries/{id} | Remove delivery |

### 💳 Payment Service (Port 8005)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /payments | Get all payments |
| GET | /payments/{id} | Get payment by ID |
| GET | /payments/order/{id} | Payment by order |
| POST | /payments | Initiate payment |
| PATCH | /payments/{id}/status | Update payment status |
| DELETE | /payments/{id} | Delete payment |

## 🔑 Why API Gateway?

Without the gateway, clients must know and manage 5 different ports (8001–8005).
The API Gateway exposes a **single port (8000)** that:
- Routes all traffic to the correct microservice
- Hides internal service topology
- Enables centralized logging, auth, and rate limiting
- Simplifies client configuration

## 🧪 Testing with Postman

Import the base URL `http://localhost:8000/api/v1` and test all endpoints.
Swagger UI is available at `http://localhost:8000/docs`.
