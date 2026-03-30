from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import data_service
from models import OrderCreate, OrderStatusUpdate

app = FastAPI(
    title="Order Service",
    description="Handles customer orders in the Food Delivery System",
    version="1.0.0"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/", tags=["Health"])
def root():
    return {"service": "Order Service", "status": "running", "port": 8003}

@app.get("/orders", tags=["Orders"])
def get_all_orders():
    """Retrieve all orders"""
    return data_service.get_all()

@app.get("/orders/{order_id}", tags=["Orders"])
def get_order(order_id: int):
    """Retrieve an order by ID"""
    order = data_service.get_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return order

@app.get("/orders/restaurant/{restaurant_id}", tags=["Orders"])
def get_orders_by_restaurant(restaurant_id: int):
    """Get all orders for a specific restaurant"""
    orders = data_service.get_by_restaurant(restaurant_id)
    return orders

@app.post("/orders", status_code=201, tags=["Orders"])
def create_order(order: OrderCreate):
    """Place a new food order"""
    return data_service.create(order)

@app.patch("/orders/{order_id}/status", tags=["Orders"])
def update_order_status(order_id: int, status_update: OrderStatusUpdate):
    """Update the status of an order"""
    result = data_service.update_status(order_id, status_update.status)
    if not result:
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return result

@app.delete("/orders/{order_id}", tags=["Orders"])
def cancel_order(order_id: int):
    """Cancel/delete an order"""
    if not data_service.delete(order_id):
        raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
    return {"message": f"Order {order_id} cancelled successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8003, reload=True)
