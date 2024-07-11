from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    order_number: str
    status: Optional[str] = "pending"

class OrderCreate(OrderBase):
    user_id: int
    subscription_id: int

class OrderUpdate(OrderBase):
    pass

class OrderInDBBase(OrderBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Order(OrderInDBBase):
    pass

class OrderInDB(OrderInDBBase):
    user_id: int
    subscription_id: int
