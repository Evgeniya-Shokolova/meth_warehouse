from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud import create_roll, delete_roll, get_rolls, get_statistics
from app.database import SessionLocal
from app.schemas import Roll, RollCreate

router = APIRouter(prefix="/rolls", tags=["rolls"])


def get_db():
    """Подключение к БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Roll)
def add_roll(roll: RollCreate, db: Session = Depends(get_db)):
    """Создать новый рулон"""
    return create_roll(db, roll)


@router.delete("rolls/{roll_id}", response_model=Roll)
def remove_roll(roll_id: int, db: Session = Depends(get_db)):
    """Удаление рулона"""
    roll = delete_roll(db, roll_id)
    if not roll:
        raise HTTPException(status_code=404, detail="Roll not found")
    return roll


@router.get("/",
            response_model=list[Roll])
def list_rolls(skip: int = 0, limit: int = 100,
               id_range: Optional[List[int]] = None,
               length_range: Optional[List[float]] = None,
               weight_range: Optional[List[float]] = None,
               start_date: Optional[datetime] = None,
               end_date: Optional[datetime] = None,
               db: Session = Depends(get_db)):
    """Получить список рулонов с фильтрацией"""
    filters = {"id_range": id_range,
               "length_range": length_range,
               "weight_range": weight_range, "start_date": start_date,
               "end_date": end_date}
    return get_rolls(db, skip=skip, limit=limit, filters=filters)


@router.get("/statistics")
def statistics(start_date: datetime,
               end_date: datetime,
               db: Session = Depends(get_db)):
    """Получение статистики по рулонам за указанный период"""
    statistics_data = get_statistics(db,
                                     start_date=start_date,
                                     end_date=end_date)

    statistics_data["removed_rolls"] = db.query(Roll).filter(
        Roll.date_removed.between(start_date, end_date)).count()

    rolls = db.query(Roll).filter(
        Roll.date_added.between(start_date, end_date)
    ).all()

    if rolls:
        lengths = [roll.length for roll in rolls]
        weights = [roll.weight for roll in rolls]
        statistics_data["average_length"] = sum(lengths) / len(lengths)
        statistics_data["average_weight"] = sum(weights) / len(weights)
        statistics_data["max_length"] = max(lengths)
        statistics_data["min_length"] = min(lengths)
        statistics_data["max_weight"] = max(weights)
        statistics_data["min_weight"] = min(weights)
        statistics_data["total_weight"] = sum(weights)

        intervals = [
            roll.date_removed - roll.date_added
            for roll in rolls if roll.date_removed]
        if intervals:
            statistics_data["max_interval"] = max(intervals).total_seconds()
            statistics_data["min_interval"] = min(intervals).total_seconds()

    return statistics_data
