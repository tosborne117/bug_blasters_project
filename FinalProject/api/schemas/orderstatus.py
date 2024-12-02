from typing import Optional
from pydantic import BaseModel
from .orders import Order

class  OrderStatusBase(BaseModel):
    order_status: str

class OrderStatusCreate(OrderStatusBase):
    order_id: int

class OrderStatusUpdate(BaseModel):
    order_id: Optional[int] = None
    order_status: Optional[str] = None

class OrderStatus(OrderStatusBase):
    tracking_num: int
    order_id: int

    class ConfigDict:
        orm_mode = True