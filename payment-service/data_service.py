from models import Payment, PaymentMethod, PaymentStatus
import uuid

payments_db = [
    Payment(
        id=1, order_id=1,
        customer_name="Kamal Perera",
        amount=3350.00,
        payment_method=PaymentMethod.CARD,
        status=PaymentStatus.COMPLETED,
        transaction_id="TXN-001-KP2024",
        notes="Visa card ending 4242"
    ),
    Payment(
        id=2, order_id=2,
        customer_name="Nimal Silva",
        amount=2950.00,
        payment_method=PaymentMethod.CASH,
        status=PaymentStatus.PENDING,
        notes="Cash on delivery"
    ),
    Payment(
        id=3, order_id=3,
        customer_name="Sunethra Fernando",
        amount=2600.00,
        payment_method=PaymentMethod.ONLINE,
        status=PaymentStatus.COMPLETED,
        transaction_id="TXN-003-SF2024",
        notes="PayHere online payment"
    ),
]

def get_all():
    return payments_db

def get_by_id(payment_id: int):
    return next((p for p in payments_db if p.id == payment_id), None)

def get_by_order(order_id: int):
    return next((p for p in payments_db if p.order_id == order_id), None)

def create(payment_data):
    new_id = max(p.id for p in payments_db) + 1
    new_payment = Payment(id=new_id, **payment_data.dict())
    payments_db.append(new_payment)
    return new_payment

def update_status(payment_id: int, new_status: PaymentStatus, transaction_id: str = None):
    payment = get_by_id(payment_id)
    if not payment:
        return None
    idx = next(i for i, p in enumerate(payments_db) if p.id == payment_id)
    updated = payment.dict()
    updated["status"] = new_status
    if transaction_id:
        updated["transaction_id"] = transaction_id
    elif new_status == PaymentStatus.COMPLETED and not updated.get("transaction_id"):
        updated["transaction_id"] = f"TXN-{str(uuid.uuid4())[:8].upper()}"
    payments_db[idx] = Payment(**updated)
    return payments_db[idx]

def delete(payment_id: int):
    global payments_db
    payment = get_by_id(payment_id)
    if not payment:
        return False
    payments_db = [p for p in payments_db if p.id != payment_id]
    return True
