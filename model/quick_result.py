from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base

class QuickResult(Base):
    __tablename__ = "quick_result"

    id = Column(Integer, primary_key=True, index=True)
    parameter_name = Column(String)
    unit = Column(String)
    protocol_use_for_analysis = Column(String)
    result = Column(String)
    current_time_date = Column(DateTime, default=datetime.utcnow)  # Saves datetime in UTC
    is_delete = Column(Boolean, default=False)
