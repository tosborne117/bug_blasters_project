from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, DateTime, Date
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Promotions(Base):
    __tablename__ = "promotions"

    promotion_key = Column("promotion_key", Integer, primary_key=True, index=True)
    promotion_name = Column("promotion_name", String(100), index=True, nullable=False)
    start_date = Column("start_date", Date, index=True, nullable=False)
    end_date = Column("end_date", Date, index="True", nullable=False)
    percentage = Column("percentage", Integer, index="True", nullable="False")

    order = relationship("Order", back_populates="promotion")