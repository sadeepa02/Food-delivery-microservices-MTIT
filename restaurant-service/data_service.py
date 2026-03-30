from models import Restaurant

restaurants_db = [
    Restaurant(id=1, name="Pizza Palace", address="123 Main St, Colombo", cuisine_type="Italian", phone="011-2345678", rating=4.5, is_open=True),
    Restaurant(id=2, name="Spice Garden", address="456 Galle Rd, Colombo", cuisine_type="Sri Lankan", phone="011-3456789", rating=4.8, is_open=True),
    Restaurant(id=3, name="Burger Barn", address="789 Union Pl, Colombo", cuisine_type="American", phone="011-4567890", rating=4.2, is_open=True),
    Restaurant(id=4, name="Sushi World", address="321 Marine Dr, Colombo", cuisine_type="Japanese", phone="011-5678901", rating=4.6, is_open=False),
    Restaurant(id=5, name="The Rice Bowl", address="654 Duplication Rd, Colombo", cuisine_type="Chinese", phone="011-6789012", rating=4.3, is_open=True),
]

def get_all():
    return restaurants_db

def get_by_id(restaurant_id: int):
    return next((r for r in restaurants_db if r.id == restaurant_id), None)

def create(restaurant_data):
    new_id = max(r.id for r in restaurants_db) + 1
    new_restaurant = Restaurant(id=new_id, **restaurant_data.dict())
    restaurants_db.append(new_restaurant)
    return new_restaurant

def update(restaurant_id: int, update_data):
    restaurant = get_by_id(restaurant_id)
    if not restaurant:
        return None
    updated = restaurant.dict()
    for key, value in update_data.dict(exclude_unset=True).items():
        updated[key] = value
    idx = next(i for i, r in enumerate(restaurants_db) if r.id == restaurant_id)
    restaurants_db[idx] = Restaurant(**updated)
    return restaurants_db[idx]

def delete(restaurant_id: int):
    global restaurants_db
    restaurant = get_by_id(restaurant_id)
    if not restaurant:
        return False
    restaurants_db = [r for r in restaurants_db if r.id != restaurant_id]
    return True
