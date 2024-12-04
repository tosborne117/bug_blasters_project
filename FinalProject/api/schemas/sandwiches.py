from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class SandwichBase(BaseModel):
    sandwich_name: str
    price: float
    category: str
    calories: int
    availability_status: str


class SandwichCreate(SandwichBase):
    pass


class SandwichUpdate(BaseModel):
    sandwich_name: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    calories: Optional[int] = None
    availability_status: Optional[str] = None


class Sandwich(SandwichBase):
    id: int

    class ConfigDict:
        from_attributes = True