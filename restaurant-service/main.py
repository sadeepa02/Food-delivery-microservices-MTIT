from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import data_service
from models import RestaurantCreate, RestaurantUpdate

app = FastAPI(
    title="Restaurant Service",
    description="Manages restaurant listings for the Food Delivery System",
    version="1.0.0"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/", tags=["Health"])
def root():
    return {"service": "Restaurant Service", "status": "running", "port": 8001}

@app.get("/restaurants", tags=["Restaurants"])
def get_all_restaurants():
    """Retrieve all restaurants"""
    return data_service.get_all()

@app.get("/restaurants/{restaurant_id}", tags=["Restaurants"])
def get_restaurant(restaurant_id: int):
    """Retrieve a restaurant by ID"""
    restaurant = data_service.get_by_id(restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail=f"Restaurant {restaurant_id} not found")
    return restaurant

@app.post("/restaurants", status_code=201, tags=["Restaurants"])
def create_restaurant(restaurant: RestaurantCreate):
    """Add a new restaurant"""
    return data_service.create(restaurant)

@app.put("/restaurants/{restaurant_id}", tags=["Restaurants"])
def update_restaurant(restaurant_id: int, update: RestaurantUpdate):
    """Update restaurant details"""
    result = data_service.update(restaurant_id, update)
    if not result:
        raise HTTPException(status_code=404, detail=f"Restaurant {restaurant_id} not found")
    return result

@app.delete("/restaurants/{restaurant_id}", tags=["Restaurants"])
def delete_restaurant(restaurant_id: int):
    """Remove a restaurant"""
    if not data_service.delete(restaurant_id):
        raise HTTPException(status_code=404, detail=f"Restaurant {restaurant_id} not found")
    return {"message": f"Restaurant {restaurant_id} deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
