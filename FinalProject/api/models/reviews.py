from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Constraint
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cust_id = Column(Integer, ForeignKey("customers.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    rating = Column(Integer, nullable=False)
    text = Column(String(100))
    date = Column(DATETIME)

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating')
    )