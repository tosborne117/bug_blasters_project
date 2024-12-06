from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: int
    text: str

class ReviewCreate(ReviewBase):
    cust_id: int
    order_id: int

class ReviewUpdate(BaseModel): #todo: add logic to handle 'None' when not wanting to update value
    text: Optional[str] = None
    rating: Optional[int] = None
    cust_id: Optional[int] = None
    order_id: Optional[int] = None

class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True


