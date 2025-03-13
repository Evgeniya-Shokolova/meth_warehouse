from sqlalchemy import Column, DateTime, Float, Intrger
from sqlalchemy.sql import func

from database import Base


class Roll(Base):
    """Модель рулона металла"""
    __tablename__ = 'rolls'

    id = Column(Intrger, primary_key=True, index=True)
    length = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    data_add = Column(DateTime(timezone=True), default=func.now())
    data_del = Column(DateTime(timezone=True), nullable=True)
