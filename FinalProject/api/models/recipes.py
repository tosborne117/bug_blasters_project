from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
from ..models.sandwiches import Sandwich


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    amount = Column(Integer, nullable=False, server_default='0.0')

    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")