from datetime import date
from io import StringIO
from typing import Optional
from pydantic import BaseModel, model_validator

class PromotionsBase(BaseModel):
    promotion_name: str
    start_date: date
    end_date: date
    percentage: int

#nothing in promotions create because this table doesn't have any foreign keys
class PromotionsCreate(PromotionsBase):
    pass

class PromotionsUpdate(BaseModel):
    promotion_name: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    percentage: Optional[int] = None

class Promotions(PromotionsBase):
    promotion_key: int

    class ConfigDict:
        from_attributes = True

#validates that start_date is before end_date
@model_validator(mode="after")
def check_dates(cls, values): #gets all fields from promotions class
    start_date = values.get("start_date") #selects start_date field
    end_date = values.get("end_date") #selects end_date field
    if start_date and end_date and start_date > end_date: #if both dates are provided, and start date is after end_date, we raise an error
        raise ValueError("Start date can't be after the end date.")
    return values
