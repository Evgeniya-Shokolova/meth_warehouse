from datetime import datetime
from app.database import Base, engine
from sqlalchemy import Column, DateTime, Float, Integer


class Roll(Base):
    """Модель рулона металла"""
    __tablename__ = "rolls"

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    date_added = Column(DateTime, default=datetime.utcnow)
    date_removed = Column(DateTime, nullable=True)


Base.metadata.create_all(bind=engine)
