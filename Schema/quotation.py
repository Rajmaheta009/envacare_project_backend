# schema/quotation.py
from pydantic import BaseModel

class QuotationCreate(BaseModel):
    order_id: int
    pdf_url: str

class QuotationResponse(BaseModel):
    id: int
    order_id: int
    pdf_url: str

    class Config:
        orm_mode = True
