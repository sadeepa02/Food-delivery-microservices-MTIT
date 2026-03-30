from models import MenuItem

menu_db = [
    MenuItem(id=1, restaurant_id=1, name="Margherita Pizza", description="Classic tomato and mozzarella", price=1200.00, category="Pizza", is_available=True),
    MenuItem(id=2, restaurant_id=1, name="Pepperoni Pizza", description="Loaded with pepperoni slices", price=1500.00, category="Pizza", is_available=True),
    MenuItem(id=3, restaurant_id=1, name="Pasta Carbonara", description="Creamy pasta with bacon", price=950.00, category="Pasta", is_available=True),
    MenuItem(id=4, restaurant_id=2, name="Rice & Curry", description="Traditional Sri Lankan rice and curry", price=550.00, category="Main Course", is_available=True),
    MenuItem(id=5, restaurant_id=2, name="Kottu Roti", description="Shredded roti with vegetables and egg", price=650.00, category="Main Course", is_available=True),
    MenuItem(id=6, restaurant_id=2, name="Fish Ambul Thiyal", description="Sour fish curry with spices", price=750.00, category="Main Course", is_available=True),
    MenuItem(id=7, restaurant_id=3, name="Classic Burger", description="Beef patty with lettuce and tomato", price=800.00, category="Burgers", is_available=True),
    MenuItem(id=8, restaurant_id=3, name="BBQ Burger", description="Smoky BBQ sauce with caramelized onions", price=950.00, category="Burgers", is_available=True),
    MenuItem(id=9, restaurant_id=3, name="Loaded Fries", description="Fries with cheese sauce and bacon bits", price=500.00, category="Sides", is_available=True),
    MenuItem(id=10, restaurant_id=5, name="Fried Rice", description="Wok-tossed rice with vegetables", price=600.00, category="Rice", is_available=True),
    MenuItem(id=11, restaurant_id=5, name="Kung Pao Chicken", description="Spicy stir-fried chicken with peanuts", price=900.00, category="Main Course", is_available=True),
    MenuItem(id=12, restaurant_id=5, name="Spring Rolls", description="Crispy vegetable spring rolls", price=350.00, category="Starters", is_available=True),
]

def get_all():
    return menu_db

def get_by_id(item_id: int):
    return next((m for m in menu_db if m.id == item_id), None)

def get_by_restaurant(restaurant_id: int):
    return [m for m in menu_db if m.restaurant_id == restaurant_id]

def create(item_data):
    new_id = max(m.id for m in menu_db) + 1
    new_item = MenuItem(id=new_id, **item_data.dict())
    menu_db.append(new_item)
    return new_item

def update(item_id: int, update_data):
    item = get_by_id(item_id)
    if not item:
        return None
    updated = item.dict()
    for key, value in update_data.dict(exclude_unset=True).items():
        updated[key] = value
    idx = next(i for i, m in enumerate(menu_db) if m.id == item_id)
    menu_db[idx] = MenuItem(**updated)
    return menu_db[idx]

def delete(item_id: int):
    global menu_db
    item = get_by_id(item_id)
    if not item:
        return False
    menu_db = [m for m in menu_db if m.id != item_id]
    return True
