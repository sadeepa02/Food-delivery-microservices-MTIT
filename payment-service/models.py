from pydantic import BaseModel
from typing import Optional
from enum import Enum

class PaymentMethod(str, Enum):
    CASH = "CASH"
    CARD = "CARD"
    ONLINE = "ONLINE"
    WALLET = "WALLET"

class PaymentStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"

class Payment(BaseModel):
    id: int
    order_id: int
    customer_name: str
    amount: float
    payment_method: PaymentMethod
    status: PaymentStatus = PaymentStatus.PENDING
    transaction_id: Optional[str] = None
    notes: Optional[str] = None

class PaymentCreate(BaseModel):
    order_id: int
    customer_name: str
    amount: float
    payment_method: PaymentMethod
    notes: Optional[str] = None

class PaymentStatusUpdate(BaseModel):
    status: PaymentStatus
    transaction_id: Optional[str] = None
