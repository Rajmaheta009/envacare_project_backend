from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class QuickResultBase(BaseModel):
    parameter_name: str
    unit: Optional[str] = None
    protocol_use_for_analysis: Optional[str] = None
    result: Optional[str] = None
    is_delete: Optional[bool] = False


class QuickResultCreate(QuickResultBase):
    pass


class QuickResultOut(QuickResultBase):
    id: int
    current_time_date: datetime

    class Config:
        orm_mode = True

    def formatted_datetime(self) -> str:
        return self.current_time_date.strftime("%H:%M %d:%m:%Y") if self.current_time_date else ""
