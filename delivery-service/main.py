from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import data_service
from models import DeliveryCreate, DeliveryStatusUpdate

app = FastAPI(
    title="Delivery Service",
    description="Manages food delivery tracking in the Food Delivery System",
    version="1.0.0"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/", tags=["Health"])
def root():
    return {"service": "Delivery Service", "status": "running", "port": 8004}

@app.get("/deliveries", tags=["Deliveries"])
def get_all_deliveries():
    """Retrieve all deliveries"""
    return data_service.get_all()

@app.get("/deliveries/{delivery_id}", tags=["Deliveries"])
def get_delivery(delivery_id: int):
    """Retrieve a delivery by ID"""
    delivery = data_service.get_by_id(delivery_id)
    if not delivery:
        raise HTTPException(status_code=404, detail=f"Delivery {delivery_id} not found")
    return delivery

@app.get("/deliveries/order/{order_id}", tags=["Deliveries"])
def get_delivery_by_order(order_id: int):
    """Track delivery status for a specific order"""
    delivery = data_service.get_by_order(order_id)
    if not delivery:
        raise HTTPException(status_code=404, detail=f"No delivery found for order {order_id}")
    return delivery

@app.post("/deliveries", status_code=201, tags=["Deliveries"])
def create_delivery(delivery: DeliveryCreate):
    """Assign a new delivery"""
    return data_service.create(delivery)

@app.patch("/deliveries/{delivery_id}/status", tags=["Deliveries"])
def update_delivery_status(delivery_id: int, status_update: DeliveryStatusUpdate):
    """Update delivery status (for drivers)"""
    result = data_service.update_status(delivery_id, status_update.status)
    if not result:
        raise HTTPException(status_code=404, detail=f"Delivery {delivery_id} not found")
    return result

@app.delete("/deliveries/{delivery_id}", tags=["Deliveries"])
def delete_delivery(delivery_id: int):
    """Remove a delivery record"""
    if not data_service.delete(delivery_id):
        raise HTTPException(status_code=404, detail=f"Delivery {delivery_id} not found")
    return {"message": f"Delivery {delivery_id} removed successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
