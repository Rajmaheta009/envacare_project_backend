from sqlalchemy import Column, Integer, Double, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OrderParameter(Base):
    __tablename__ = 'order_parameters'

    id = Column(Integer, primary_key=True, index=True)
    quotation_id = Column(Integer, nullable=False)
    parameter_id = Column(Integer, nullable=False)
    cost = Column(Double, nullable=False)
    result = Column(String(255), nullable=True)
    is_delete = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
