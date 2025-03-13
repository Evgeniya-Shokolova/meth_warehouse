from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RollCreate(BaseModel):
    """Схема создания рулона"""
    length: float
    weight: float


class Roll(BaseModel):
    """Схема рулона, API"""
    id: int
    length: float
    weight: float
    data_add: datetime
    data_del: Optional[datetime]

    class Config:
        orm_mode = True
