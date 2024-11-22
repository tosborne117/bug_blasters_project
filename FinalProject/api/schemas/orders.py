from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str]
    tracking_num: int
    order_date: Optional[datetime] = None


class OrderCreate(OrderBase):
    user_id: int
    payment_id: int

class OrderRead(OrderBase):
    order_id: int
    user_id: int
    payment_id: int
    customer_name: str
    tracking_num: int
    description: str
    order_date: datetime
    order_details: List[dict]

    class Config:
        orm_mode = True


class OrderUpdate(BaseModel):
    customer_name: Optional[str]
    description: Optional[str]
    tracking_num: Optional[int]
    order_date: Optional[datetime]
    user_id: Optional[int]
    payment_id: Optional[int]



class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
