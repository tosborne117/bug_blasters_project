from __future__ import annotations
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail


class OrderBase(BaseModel):
    customer_name: str
    description: str
    order_date: datetime
    payment_type: str
    order_status: str


class OrderCreate(OrderBase):
    customer_id: int
    promotion_key: int

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    payment_type: Optional[str] = None
    order_date: Optional[datetime] = None
    customer_id: Optional[int] = None
    promotion_key: Optional[int] = None
    order_status: Optional[str] = None



class Order(OrderBase):
    order_id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class Config:
        orm_mode = True

