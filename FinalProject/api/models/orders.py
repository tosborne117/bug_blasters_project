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
    tracking_num = Column(Integer, ForeignKey("orderstatus.tracking_num"), nullable=False)
    promotion_key = Column(Integer, ForeignKey("promotions.promotion_key"), nullable=False)

    order_details = relationship("OrderDetail", back_populates="order")
    orderstatus = relationship("OrderStatus", back_populates="order")
    customers = relationship("Customer", back_populates="order")
    promotion = relationship("Promotion", back_populates="order")

