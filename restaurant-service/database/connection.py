import os
from copy import deepcopy
from types import SimpleNamespace

from bson import ObjectId
from pymongo import MongoClient

DEFAULT_MONGO_URI = "mongodb+srv://Rashmika:200212@food-delivery-system.z55zyic.mongodb.net/food-delivery-system?appName=food-delivery-system"
MONGO_URI = os.getenv("MONGO_URI", DEFAULT_MONGO_URI)


class InMemoryRestaurantCollection:
    def __init__(self):
        self._items = {}

    def insert_one(self, data):
        document = deepcopy(data)
        object_id = ObjectId()
        document["_id"] = object_id
        self._items[str(object_id)] = document
        return SimpleNamespace(inserted_id=object_id)

    def find(self):
        return [deepcopy(item) for item in self._items.values()]

    def find_one(self, query):
        object_id = query.get("_id")
        if object_id is None:
            return None
        document = self._items.get(str(object_id))
        return deepcopy(document) if document else None

    def update_one(self, query, update):
        object_id = query.get("_id")
        existing = self._items.get(str(object_id))
        if not existing:
            return SimpleNamespace(matched_count=0)

        updates = update.get("$set", {})
        existing.update(deepcopy(updates))
        return SimpleNamespace(matched_count=1)

    def delete_one(self, query):
        object_id = query.get("_id")
        removed = self._items.pop(str(object_id), None)
        return SimpleNamespace(deleted_count=1 if removed else 0)


client = None
db = None

try:
    client = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=5000,
    )
    client.admin.command("ping")
    db = client["food-delivery-system"]
    restaurant_collection = db["restaurants"]
except Exception:
    restaurant_collection = InMemoryRestaurantCollection()
