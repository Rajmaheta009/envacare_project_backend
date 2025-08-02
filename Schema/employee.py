from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class EmployeeBase(BaseModel):
    first_name: str  # Mapping to 'First Name'
    middle_name: Optional[str] = None  # Mapping to 'Middle Name'
    last_name: str  # Mapping to 'Last Name'
    email: EmailStr  # Mapping to 'Email Address'
    phone_number: str  # Mapping to 'Phone No.'
    dept_id: int  # Mapping to 'Department'
    position: Optional[str] = None  # Mapping to 'Position'
    date_of_hire: datetime  # Mapping to 'Date of Hire'
    date_of_birth: datetime  # Mapping to 'Date of Birth'
    gender: Optional[str] = None  # Mapping to 'Gender'
    address: Optional[str] = None  # Mapping to 'Address'
    is_deleted: Optional[bool] = False
    is_active: Optional[bool] = True

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    dept_id: Optional[int]
    position: Optional[str]
    date_of_hire: Optional[datetime]
    date_of_birth: Optional[datetime]
    gender: Optional[str]
    address: Optional[str]
    is_deleted: Optional[bool]
    is_active: Optional[bool]

class EmployeeOut(EmployeeBase):
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        orm_mode = True
