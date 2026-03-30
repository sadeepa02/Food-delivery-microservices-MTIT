from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import data_service
from models import MenuItemCreate, MenuItemUpdate

app = FastAPI(
    title="Menu Service",
    description="Manages menu items for restaurants in the Food Delivery System",
    version="1.0.0"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/", tags=["Health"])
def root():
    return {"service": "Menu Service", "status": "running", "port": 8002}

@app.get("/menu", tags=["Menu"])
def get_all_items():
    """Retrieve all menu items"""
    return data_service.get_all()

@app.get("/menu/{item_id}", tags=["Menu"])
def get_menu_item(item_id: int):
    """Retrieve a menu item by ID"""
    item = data_service.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail=f"Menu item {item_id} not found")
    return item

@app.get("/menu/restaurant/{restaurant_id}", tags=["Menu"])
def get_menu_by_restaurant(restaurant_id: int):
    """Retrieve all menu items for a specific restaurant"""
    items = data_service.get_by_restaurant(restaurant_id)
    if not items:
        raise HTTPException(status_code=404, detail=f"No menu items found for restaurant {restaurant_id}")
    return items

@app.post("/menu", status_code=201, tags=["Menu"])
def create_menu_item(item: MenuItemCreate):
    """Add a new menu item"""
    return data_service.create(item)

@app.put("/menu/{item_id}", tags=["Menu"])
def update_menu_item(item_id: int, update: MenuItemUpdate):
    """Update a menu item"""
    result = data_service.update(item_id, update)
    if not result:
        raise HTTPException(status_code=404, detail=f"Menu item {item_id} not found")
    return result

@app.delete("/menu/{item_id}", tags=["Menu"])
def delete_menu_item(item_id: int):
    """Remove a menu item"""
    if not data_service.delete(item_id):
        raise HTTPException(status_code=404, detail=f"Menu item {item_id} not found")
    return {"message": f"Menu item {item_id} deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
