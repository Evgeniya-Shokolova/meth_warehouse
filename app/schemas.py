from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RollBase(BaseModel):
    """Схема создания рулона"""
    length: float
    weight: float


class RollCreate(RollBase):
    pass


class Roll(RollBase):
    """Схема рулона, API"""
    id: int
    date_added: datetime
    date_removed: Optional[datetime]

    class Config:
        orm_mode = True
