from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.sql import func
from database import Base

class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, nullable=True)
    particulars = Column(String(255))
    quantity = Column(Float)
    location = Column(String(255))
    condition = Column(String(255))
    sample_type = Column(String(100))
    collect_date = Column(Date)
    receipt_date = Column(Date)
    collected_by = Column(String(255))
    is_delete = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
