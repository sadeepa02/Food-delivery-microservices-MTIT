from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(
    title="🍕 Food Delivery API Gateway",
    description="""
## Food Delivery System — API Gateway

This **API Gateway** is the single entry point for all Food Delivery microservices.
It routes requests to the appropriate backend service without exposing individual ports.

### Microservices Behind This Gateway

| Service | Internal Port | Responsibility |
|---|---|---|
| 🍽️ Restaurant Service | 8001 | Manage restaurant listings |
| 📋 Menu Service | 8002 | Manage food menus per restaurant |
| 🛒 Order Service | 8003 | Place and track customer orders |
| 🚴 Delivery Service | 8004 | Assign and track deliveries |
| 💳 Payment Service | 8005 | Handle order payments |

> All endpoints below are proxied through this gateway on **port 8000**.
    """,
    version="1.0.0",
    contact={
        "name": "Food Delivery Team",
        "email": "fooddelivery@sliit.lk"
    }
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(router, prefix="/api/v1")

@app.get("/", tags=["Gateway Health"])
def gateway_root():
    return {
        "gateway": "Food Delivery API Gateway",
        "status": "running",
        "version": "1.0.0",
        "port": 8000,
        "services": {
            "restaurant-service": "http://localhost:8001 → /api/v1/restaurants",
            "menu-service":        "http://localhost:8002 → /api/v1/menu",
            "order-service":       "http://localhost:8003 → /api/v1/orders",
            "delivery-service":    "http://localhost:8004 → /api/v1/deliveries",
            "payment-service":     "http://localhost:8005 → /api/v1/payments",
        },
        "docs": "http://localhost:8000/docs"
    }

@app.get("/health", tags=["Gateway Health"])
def health_check():
    return {"status": "healthy", "gateway": "Food Delivery API Gateway"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
