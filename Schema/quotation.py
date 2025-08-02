# --- schema/quotation.py ---
from pydantic import BaseModel
from typing import Optional, List

class ParameterInfo(BaseModel):
    parameter_id: int
    name: str
    cost: int
    quantity: int

class QuotationCreate(BaseModel):
    customer_id: int
    order_id: int
    parameter_info: List[ParameterInfo]

class QuotationResponse(BaseModel):
    id: int
    order_id: int
    pdf_url: Optional[str] = None