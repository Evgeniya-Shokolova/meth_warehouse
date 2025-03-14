from datetime import datetime
from typing import Optional

from pydantic import BaseModel, condecimal


class RollBase(BaseModel):
    """Схема создания рулона"""
    length: condecimal(ge=0)
    weight: condecimal(ge=0)


class RollCreate(RollBase):
    pass


class Roll(RollBase):
    """Схема рулона, API"""
    id: int
    date_added: datetime
    date_removed: Optional[datetime]

    class Config:
        orm_mode = True
