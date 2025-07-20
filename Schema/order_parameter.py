from pydantic import BaseModel
from typing import Optional

class OrderParameterBase(BaseModel):
    quotation_id: int
    parameter_id: int
    cost: int
    result: Optional[str] = None

class OrderParameterCreate(OrderParameterBase):
    pass

class OrderParameterOut(OrderParameterBase):
    id: int

class ResultUpdate(BaseModel):
    order_param_id: int
    result: str