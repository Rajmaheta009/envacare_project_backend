# --- model/quotation.py ---
from sqlalchemy import Column, Integer, String, Boolean, text
from database import Base
from requests import Session

class Quotation(Base):
    __tablename__ = 'quotations'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, index=True)
    pdf_url = Column(String(500))
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)

def get_next_id(db: Session):
    result = db.execute(text("SELECT nextval(pg_get_serial_sequence('quotations', 'id'))"))
    return result.scalar()
