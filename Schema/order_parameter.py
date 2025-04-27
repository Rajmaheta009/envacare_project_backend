from pydantic import BaseModel
from typing import Optional

class OrderParameterBase(BaseModel):
    quotation_id: int
    parameter_id: int
    cost: float
    result: Optional[str] = None
    is_delete: Optional[bool] = False
    is_active: Optional[bool] = True

class OrderParameterCreate(OrderParameterBase):
    pass

class OrderParameterUpdate(BaseModel):
    cost: Optional[float] = None
    result: Optional[str] = None
    is_delete: Optional[bool] = None
    is_active: Optional[bool] = None

class OrderParameterOut(OrderParameterBase):
    id: int

    class Config:
        orm_mode = True
