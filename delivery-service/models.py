from pydantic import BaseModel
from typing import Optional
from enum import Enum

class DeliveryStatus(str, Enum):
    ASSIGNED = "ASSIGNED"
    PICKED_UP = "PICKED_UP"
    EN_ROUTE = "EN_ROUTE"
    DELIVERED = "DELIVERED"
    FAILED = "FAILED"

class Delivery(BaseModel):
    id: int
    order_id: int
    driver_name: str
    driver_phone: str
    vehicle_type: str
    pickup_address: str
    delivery_address: str
    status: DeliveryStatus = DeliveryStatus.ASSIGNED
    estimated_time_minutes: int
    notes: Optional[str] = None

class DeliveryCreate(BaseModel):
    order_id: int
    driver_name: str
    driver_phone: str
    vehicle_type: str
    pickup_address: str
    delivery_address: str
    estimated_time_minutes: int
    notes: Optional[str] = None

class DeliveryStatusUpdate(BaseModel):
    status: DeliveryStatus
