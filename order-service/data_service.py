from models import Order, OrderItem, OrderStatus

orders_db = [
    Order(
        id=1,
        customer_name="Kamal Perera",
        customer_phone="077-1234567",
        delivery_address="12 Temple Rd, Colombo 3",
        restaurant_id=1,
        items=[
            OrderItem(menu_item_id=1, name="Margherita Pizza", quantity=2, unit_price=1200.00, subtotal=2400.00),
            OrderItem(menu_item_id=3, name="Pasta Carbonara", quantity=1, unit_price=950.00, subtotal=950.00),
        ],
        total_amount=3350.00,
        status=OrderStatus.PREPARING,
        special_instructions="Extra cheese please"
    ),
    Order(
        id=2,
        customer_name="Nimal Silva",
        customer_phone="076-9876543",
        delivery_address="45 Galle Rd, Colombo 6",
        restaurant_id=2,
        items=[
            OrderItem(menu_item_id=4, name="Rice & Curry", quantity=3, unit_price=550.00, subtotal=1650.00),
            OrderItem(menu_item_id=5, name="Kottu Roti", quantity=2, unit_price=650.00, subtotal=1300.00),
        ],
        total_amount=2950.00,
        status=OrderStatus.OUT_FOR_DELIVERY
    ),
    Order(
        id=3,
        customer_name="Sunethra Fernando",
        customer_phone="071-5432109",
        delivery_address="88 Duplication Rd, Colombo 3",
        restaurant_id=3,
        items=[
            OrderItem(menu_item_id=7, name="Classic Burger", quantity=2, unit_price=800.00, subtotal=1600.00),
            OrderItem(menu_item_id=9, name="Loaded Fries", quantity=2, unit_price=500.00, subtotal=1000.00),
        ],
        total_amount=2600.00,
        status=OrderStatus.DELIVERED
    ),
]

def get_all():
    return orders_db

def get_by_id(order_id: int):
    return next((o for o in orders_db if o.id == order_id), None)

def get_by_restaurant(restaurant_id: int):
    return [o for o in orders_db if o.restaurant_id == restaurant_id]

def create(order_data):
    new_id = max(o.id for o in orders_db) + 1
    items = [
        OrderItem(
            menu_item_id=item.menu_item_id,
            name=item.name,
            quantity=item.quantity,
            unit_price=item.unit_price,
            subtotal=item.quantity * item.unit_price
        ) for item in order_data.items
    ]
    total = sum(i.subtotal for i in items)
    new_order = Order(
        id=new_id,
        customer_name=order_data.customer_name,
        customer_phone=order_data.customer_phone,
        delivery_address=order_data.delivery_address,
        restaurant_id=order_data.restaurant_id,
        items=items,
        total_amount=total,
        status=OrderStatus.PENDING,
        special_instructions=order_data.special_instructions
    )
    orders_db.append(new_order)
    return new_order

def update_status(order_id: int, new_status: OrderStatus):
    order = get_by_id(order_id)
    if not order:
        return None
    idx = next(i for i, o in enumerate(orders_db) if o.id == order_id)
    updated = order.dict()
    updated["status"] = new_status
    orders_db[idx] = Order(**updated)
    return orders_db[idx]

def delete(order_id: int):
    global orders_db
    order = get_by_id(order_id)
    if not order:
        return False
    orders_db = [o for o in orders_db if o.id != order_id]
    return True
