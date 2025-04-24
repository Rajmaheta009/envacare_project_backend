from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class SampleBase(BaseModel):
    order_id: Optional[str] = None
    particulars: str
    quantity: float
    location: str
    condition: str
    sample_type: str
    collect_date: date
    receipt_date: date
    collected_by: str

class SampleCreate(SampleBase):
    pass

class SampleUpdate(SampleBase):
    pass

class SampleOut(SampleBase):
    id: int
    is_delete: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
