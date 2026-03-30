from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    PREPARING = "PREPARING"
    READY = "READY"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"

class OrderItem(BaseModel):
    menu_item_id: int
    name: str
    quantity: int
    unit_price: float
    subtotal: float

class Order(BaseModel):
    id: int
    customer_name: str
    customer_phone: str
    delivery_address: str
    restaurant_id: int
    items: List[OrderItem]
    total_amount: float
    status: OrderStatus = OrderStatus.PENDING
    special_instructions: Optional[str] = None

class OrderItemRequest(BaseModel):
    menu_item_id: int
    name: str
    quantity: int
    unit_price: float

class OrderCreate(BaseModel):
    customer_name: str
    customer_phone: str
    delivery_address: str
    restaurant_id: int
    items: List[OrderItemRequest]
    special_instructions: Optional[str] = None

class OrderStatusUpdate(BaseModel):
    status: OrderStatus
