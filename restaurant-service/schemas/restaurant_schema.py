from pydantic import BaseModel
from pydantic import Field
from typing import List

class MenuItem(BaseModel):
    name: str
    price: float

class Restaurant(BaseModel):
    name: str
    location: str
    menu: List[MenuItem] = Field(default_factory=list)
