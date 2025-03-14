from sqlalchemy.orm import Session
from datetime import datetime
from app.models import Roll
from app.schemas import RollCreate


def create_roll(db: Session,
                roll: RollCreate):

    db_roll = Roll(length=roll.length, weight=roll.weight)
    db.add(db_roll)
    db.commit()
    db.refresh(db_roll)
    return db_roll


def get_rool(db: Session, roll_id: int):
    """Получение одного рулона по id"""
    return db.query(Roll).filter(Roll.id == roll_id).first()


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
    """Получение списка рулонов с фильтрацией"""
    query = db.query(Roll)

    if filters.get("id_range"):
        if filters["id_range"] and len(filters["id_range"]) == 2:
            query = query.filter(Roll.id.between(filters[
                "id_range"][0], filters["id_range"][1]))

    if filters.get("length_range"):
        if filters["length_range"] and len(filters["length_range"]) == 2:
            query = query.filter(Roll.length.between(filters[
                "length_range"][0], filters["length_range"][1]))

    if filters.get("weight_range"):
        if filters["weight_range"] and len(filters["weight_range"]) == 2:
            query = query.filter(Roll.weight.between(filters[
                "weight_range"][0], filters["weight_range"][1]))

    if filters.get("start_date") and filters.get("end_date"):
        query = query.filter(Roll.date_added.between(filters[
            "start_date"], filters["end_date"]))

    return query.offset(skip).limit(limit).all()


def get_statistics(db: Session,
                   start_date: datetime,
                   end_date: datetime):
    """Получение статистики по добавленным рулонам"""
    result = {
        "added_rolls": db.query(Roll).filter(
            Roll.date_added.between(start_date, end_date)
            ).count(),
    }
    return result
