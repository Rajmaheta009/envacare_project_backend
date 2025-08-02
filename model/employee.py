from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)  # Mapping to 'First Name'
    middle_name = Column(String(255))  # Mapping to 'Middle Name'
    last_name = Column(String(255), nullable=False)  # Mapping to 'Last Name'
    email = Column(String(255), unique=True, nullable=False)  # Mapping to 'Email Address'
    phone_number = Column(String(255), nullable=False)  # Mapping to 'Phone No.'
    dept_id = Column(Integer, ForeignKey("department.id"), nullable=False)  # Mapping to 'Department'
    position = Column(String(255))  # Mapping to 'Position'
    date_of_hire = Column(DateTime, nullable=False)  # Mapping to 'Date of Hire'
    date_of_birth = Column(DateTime, nullable=False)  # Mapping to 'Date of Birth'
    gender = Column(String(255))  # Mapping to 'Gender'
    address = Column(String(255))  # Mapping to 'Address'
    is_deleted = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
