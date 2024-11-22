from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderStatus(Base):
    __tablename__ = "orderstatus"

    tracking_num = Column("tracking_num", Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    order_status = Column(String, index=True, nullable=False)

    order = relationship("Order", back_populates="orderstatus")