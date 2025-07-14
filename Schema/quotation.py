# schema/quotation.py
from pydantic import BaseModel
from typing import Optional

class QuotationCreate(BaseModel):
    order_id: int
    pdf_url: Optional[str] = None

class QuotationResponse(BaseModel):
    id: int
    order_id: int
    pdf_url: Optional[str] = None