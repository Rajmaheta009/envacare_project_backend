from sqlalchemy import Column, Integer, String,ForeignKey,Boolean
from database import Base


# Quotation Model
class Parameter(Base):
    __tablename__ = "parameters"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer)
    name = Column(String)
    price = Column(Integer)
    min_range = Column(Integer)
    max_range = Column(Integer)
    unit = Column(String)
    is_3025_method= Column(String)
    apha_24th_edition_method= Column(String)
    is_delete = Column(Boolean, default=False)

