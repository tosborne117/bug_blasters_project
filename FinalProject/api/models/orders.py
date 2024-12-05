from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    customer_name = Column(String(100), nullable=False)
    order_date = Column(DATETIME, nullable=False, server_default=func.now())
    description = Column(String(300))
    payment_type = Column(String(200), nullable=False)
    promotion_key = Column(Integer, ForeignKey("promotions.promotion_key"), nullable=True)
    order_status = Column(String(100), nullable=False)

    order_details = relationship("OrderDetail", back_populates="order")
    customers = relationship("Customers", back_populates="orders")
    promotion = relationship("Promotions", back_populates="order")
    review = relationship("Review", back_populates="order")

