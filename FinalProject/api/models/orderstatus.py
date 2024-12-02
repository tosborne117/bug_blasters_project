from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderStatus(Base):
    __tablename__ = "orderstatus"

    tracking_num = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id", ondelete="CASCADE", use_alter=True, name="fk_orderstatus_order"), nullable=True)
    order_status = Column(String(100), nullable=False)

    order = relationship("Order", back_populates="orderstatus")