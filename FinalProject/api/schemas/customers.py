from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: int
    address: str


class CustomerCreate(CustomerBase):
    name: str
    email: str
    phone_number: int
    address: str


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[int] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    id: int
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
