from datetime import datetime

from sqlalchemy.orm import Session

from app.models import Roll
from app.schemas import RollCreate


def create_roll(db: Session,
                roll: RollCreate):
    """Создаём новый рулон в БД"""
    db_roll = Roll(length=roll.length, weight=roll.weight)
    db.add(db_roll)
    db.commit()
    db.refresh(db_roll)
    return db_roll


def delete_roll(db: Session,
                roll_id: int):
    """Удаление рулона"""
    roll = db.query(Roll).filter(Roll.id == roll_id).first()
    if roll:
        roll.date_removed = datetime.utcnow()
        db.commit()
        db.refresh(roll)
    return roll


def get_rolls(db: Session,
              skip: int = 0,
              limit: int = 100,
              filters: dict = None):
    """Получение списка рулонов"""
    query = db.query(Roll)
    if filters:
        if "id_range" in filters:
            query = query.filter(Roll.id.between(filters["id_range"][0],
                                                 filters["id_range"][1]))
        if "length_range" in filters:
            query = query.filter(Roll.length.between(
                filters["length_range"][0], filters["length_range"][1]))
    return query.offset(skip).limit(limit).all()


def get_statistics(db: Session,
                   start_date: datetime,
                   end_date: datetime):
    result = {
        "added_rolls": db.query(Roll).filter(
            Roll.date_added.between(start_date, end_date)
            ).count(),
    }
    return result
