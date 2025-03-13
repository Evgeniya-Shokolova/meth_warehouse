from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import database
import models
import schemas
from database import SessionLocal, engine

router = APIRouter()

models.Base.metedata.create_all(bind=engine)


def get_db():
    """Подключение к БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/rolls/", response_model=schemas.Roll)
def create_roll(roll: schemas.RollCreate, db: Session = Depends(get_db)):
    """Создать новый рулон"""
    return database.create_roll(db=db, roll=roll)


@router.get("/rolls/", response_model=List[schemas.Roll])
def read_roll(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Получить список рулонов"""
    rolls = database.get_rolls(db, skip=skip, limit=limit)
    return rolls


@router.delete("/rolls/{roll_id}", response_model=schemas.Roll)
def delete_roll(roll_id: int, db: Session = Depends(get_db)):
    """Удаление рулона"""
    roll = database.get_rolls(db, roll_id=roll_id)
    if roll is None:
        raise HTTPException(status=404, detail='Рулон не найден')
    return roll
