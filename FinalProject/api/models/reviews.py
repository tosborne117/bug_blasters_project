from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cust_id = Column(Integer, ForeignKey("customers.customer_id", ondelete="CASCADE"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.order_id", ondelete="CASCADE"), nullable=False)
    rating = Column(Integer, nullable=False)
    text = Column(String(100))
    date = Column(DATETIME, nullable=False, server_default=func.now())

    customer = relationship("Customer", back_populates="reviews")
    order = relationship("Order", back_populates="reviews")