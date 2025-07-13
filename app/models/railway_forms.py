from sqlalchemy import Column, Integer, String, DateTime, JSON, Text
from sqlalchemy.sql import func
from ..database import Base


class WheelSpecification(Base):
    __tablename__ = "wheel_specifications"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True, nullable=False)
    submitted_by = Column(String, nullable=False)
    submitted_date = Column(String, nullable=False)
    fields = Column(JSON, nullable=False)
    status = Column(String, default="Saved")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheets"
    
    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, unique=True, index=True, nullable=False)
    inspection_by = Column(String, nullable=False)
    inspection_date = Column(String, nullable=False)
    bogie_details = Column(JSON, nullable=False)
    bogie_checksheet = Column(JSON, nullable=False)
    bmbc_checksheet = Column(JSON, nullable=False)
    status = Column(String, default="Saved")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 