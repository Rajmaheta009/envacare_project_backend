from sqlalchemy import Column, Integer, String,Boolean
from database import Base

class Quotation(Base):
    __tablename__ = 'quotations'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, index=True)
    pdf_url = Column(String(500))
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
