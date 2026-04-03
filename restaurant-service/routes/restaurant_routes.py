from fastapi import APIRouter, HTTPException
from bson import ObjectId
from pymongo.errors import PyMongoError
from database.connection import restaurant_collection
from schemas.restaurant_schema import Restaurant

router = APIRouter()

def parse_object_id(id: str) -> ObjectId:
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid restaurant id")
    return ObjectId(id)

# Create Restaurant
@router.post("/")
def create_restaurant(data: Restaurant):
    try:
        result = restaurant_collection.insert_one(data.dict())
        return {"id": str(result.inserted_id)}
    except PyMongoError:
        raise HTTPException(status_code=503, detail="Restaurant database is unavailable")

# Get All Restaurants
@router.get("/")
def get_restaurants():
    try:
        restaurants = []
        for r in restaurant_collection.find():
            r["id"] = str(r["_id"])
            del r["_id"]
            restaurants.append(r)
        return restaurants
    except PyMongoError:
        raise HTTPException(status_code=503, detail="Restaurant database is unavailable")

# Get One Restaurant
@router.get("/{id}")
def get_restaurant(id: str):
    object_id = parse_object_id(id)

    try:
        restaurant = restaurant_collection.find_one({"_id": object_id})
        if not restaurant:
            raise HTTPException(status_code=404, detail="Restaurant not found")

        restaurant["id"] = str(restaurant["_id"])
        del restaurant["_id"]
        return restaurant
    except PyMongoError:
        raise HTTPException(status_code=503, detail="Restaurant database is unavailable")

# Edit Restaurant Details
@router.put("/{id}")
def edit_restaurant(id: str, data: Restaurant):
    object_id = parse_object_id(id)
    try:
        result = restaurant_collection.update_one(
            {"_id": object_id},
            {"$set": data.dict()}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Restaurant not found")

        return {"message": "Restaurant details updated successfully"}
    except PyMongoError:
        raise HTTPException(status_code=503, detail="Restaurant database is unavailable")

# Delete Restaurant
@router.delete("/{id}")
def delete_restaurant(id: str):
    object_id = parse_object_id(id)
    try:
        result = restaurant_collection.delete_one({"_id": object_id})

        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Restaurant not found")

        return {"message": "Restaurant deleted successfully"}
    except PyMongoError:
        raise HTTPException(status_code=503, detail="Restaurant database is unavailable")
