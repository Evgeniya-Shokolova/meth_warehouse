from datetime import datetime

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


@router.delete("/{roll_id}", response_model=Roll)
def remove_roll(roll_id: int, db: Session = Depends(get_db)):
    """Удаление рулона"""
    roll = delete_roll(db, roll_id)
    if not roll:
        raise HTTPException(status_code=404, detail="Roll not found")
    return roll


@router.get("/",
            response_model=list[Roll])
def list_rolls(skip: int = 0,
               limit: int = 100,
               db: Session = Depends(get_db)):
    """Получить список рулонов"""
    filters = {}
    return get_rolls(db, skip=skip, limit=limit, filters=filters)


@router.get("/statistics")
def statistics(start_date: datetime,
               end_date: datetime,
               db: Session = Depends(get_db)):
    return get_statistics(db, start_date=start_date, end_date=end_date)
