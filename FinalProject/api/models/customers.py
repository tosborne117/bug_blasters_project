from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customers(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String(100), unique=False, nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    phone_number = Column(String(10), unique=True, nullable=True)
    address = Column(String(100), unique=True, nullable=True)









