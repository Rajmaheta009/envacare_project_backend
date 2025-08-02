from typing import Optional
from pydantic import BaseModel

class ParameterCreate(BaseModel):
    parent_id: int
    name: str
    price: float
    min_range: float
    max_range: float
    is_3025_method: Optional[str] = ""  # ✅ allows null or empty string
    apha_24th_edition_method: Optional[str] = ""  # ✅ allows null or empty string
    unit: str



class ParameterUpdate(BaseModel):
    name: str
    price: float = 00.00
    min_range : float = 00.00
    max_range : float= 00.00
    is_3025_method : str
    apha_24th_edition_method : str
    unit: str