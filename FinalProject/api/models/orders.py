from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"


    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    customer_name = Column(String(100), nullable=False)
    order_date = Column(DATETIME, nullable=False, server_default=func.now())
    description = Column(String(300))
    payment_id = Column(Integer, ForeignKey("payment.id"), nullable=False)
    tracking_num = Column(Integer, unique=True, nullable=False)
    order_details = relationship("OrderDetail", back_populates="order")