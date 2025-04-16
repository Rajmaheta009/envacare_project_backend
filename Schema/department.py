from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DepartmentBase(BaseModel):
    name: str
    location: str
    head_name: str
    is_deleted: Optional[bool] = False
    is_active: Optional[bool] = True

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass

class DepartmentOut(DepartmentBase):
    id: int
    name:str
    location: str
    head_name: str
    create_at: datetime
    update_at: datetime

