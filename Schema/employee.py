from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone_number: str
    dept_id: int
    is_deleted: Optional[bool] = False
    is_active: Optional[bool] = True

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    phone_number: Optional[str]
    dept_id: Optional[int]
    is_deleted: Optional[bool]
    is_active: Optional[bool]

class EmployeeOut(EmployeeBase):
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
