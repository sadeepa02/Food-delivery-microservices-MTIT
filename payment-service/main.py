from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import data_service
from models import PaymentCreate, PaymentStatusUpdate

app = FastAPI(
    title="Payment Service",
    description="Handles payment processing for the Food Delivery System",
    version="1.0.0"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/", tags=["Health"])
def root():
    return {"service": "Payment Service", "status": "running", "port": 8005}

@app.get("/payments", tags=["Payments"])
def get_all_payments():
    """Retrieve all payments"""
    return data_service.get_all()

@app.get("/payments/{payment_id}", tags=["Payments"])
def get_payment(payment_id: int):
    """Retrieve a payment by ID"""
    payment = data_service.get_by_id(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail=f"Payment {payment_id} not found")
    return payment

@app.get("/payments/order/{order_id}", tags=["Payments"])
def get_payment_by_order(order_id: int):
    """Get payment details for a specific order"""
    payment = data_service.get_by_order(order_id)
    if not payment:
        raise HTTPException(status_code=404, detail=f"No payment found for order {order_id}")
    return payment

@app.post("/payments", status_code=201, tags=["Payments"])
def create_payment(payment: PaymentCreate):
    """Initiate a payment for an order"""
    return data_service.create(payment)

@app.patch("/payments/{payment_id}/status", tags=["Payments"])
def update_payment_status(payment_id: int, status_update: PaymentStatusUpdate):
    """Update payment status (confirm, fail, or refund)"""
    result = data_service.update_status(
        payment_id,
        status_update.status,
        status_update.transaction_id
    )
    if not result:
        raise HTTPException(status_code=404, detail=f"Payment {payment_id} not found")
    return result

@app.delete("/payments/{payment_id}", tags=["Payments"])
def delete_payment(payment_id: int):
    """Remove a payment record"""
    if not data_service.delete(payment_id):
        raise HTTPException(status_code=404, detail=f"Payment {payment_id} not found")
    return {"message": f"Payment {payment_id} deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8005, reload=True)
