from models import Delivery, DeliveryStatus

deliveries_db = [
    Delivery(
        id=1, order_id=1,
        driver_name="Ashan Perera",
        driver_phone="078-1112222",
        vehicle_type="Motorcycle",
        pickup_address="123 Main St, Colombo (Pizza Palace)",
        delivery_address="12 Temple Rd, Colombo 3",
        status=DeliveryStatus.EN_ROUTE,
        estimated_time_minutes=25,
        notes="Call on arrival"
    ),
    Delivery(
        id=2, order_id=2,
        driver_name="Ruwan Kumara",
        driver_phone="077-3334444",
        vehicle_type="Bicycle",
        pickup_address="456 Galle Rd, Colombo (Spice Garden)",
        delivery_address="45 Galle Rd, Colombo 6",
        status=DeliveryStatus.PICKED_UP,
        estimated_time_minutes=15
    ),
    Delivery(
        id=3, order_id=3,
        driver_name="Tharanga Wijesinghe",
        driver_phone="071-5556666",
        vehicle_type="Motorcycle",
        pickup_address="789 Union Pl, Colombo (Burger Barn)",
        delivery_address="88 Duplication Rd, Colombo 3",
        status=DeliveryStatus.DELIVERED,
        estimated_time_minutes=30
    ),
]

def get_all():
    return deliveries_db

def get_by_id(delivery_id: int):
    return next((d for d in deliveries_db if d.id == delivery_id), None)

def get_by_order(order_id: int):
    return next((d for d in deliveries_db if d.order_id == order_id), None)

def create(delivery_data):
    new_id = max(d.id for d in deliveries_db) + 1
    new_delivery = Delivery(id=new_id, **delivery_data.dict())
    deliveries_db.append(new_delivery)
    return new_delivery

def update_status(delivery_id: int, new_status: DeliveryStatus):
    delivery = get_by_id(delivery_id)
    if not delivery:
        return None
    idx = next(i for i, d in enumerate(deliveries_db) if d.id == delivery_id)
    updated = delivery.dict()
    updated["status"] = new_status
    deliveries_db[idx] = Delivery(**updated)
    return deliveries_db[idx]

def delete(delivery_id: int):
    global deliveries_db
    delivery = get_by_id(delivery_id)
    if not delivery:
        return False
    deliveries_db = [d for d in deliveries_db if d.id != delivery_id]
    return True
