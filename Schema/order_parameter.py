from pydantic import BaseModel
from typing import Optional

class OrderParameterBase(BaseModel):
    quotation_id: int
    parameter_id: int
    cost: int
    result: Optional[str] = None
    is_delete: Optional[bool] = False
    is_active: Optional[bool] = True

class OrderParameterCreate(OrderParameterBase):
    pass

class OrderParameterUpdate(BaseModel):
    cost: Optional[int] = None
    result: Optional[str] = None
    is_delete: Optional[bool] = None
    is_active: Optional[bool] = None

class OrderParameterOut(OrderParameterBase):
    id: int

