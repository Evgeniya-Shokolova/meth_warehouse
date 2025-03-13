import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from . import models, schemas

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./test.db')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_rolls(db: Session, skip: int = 0, limit: int = 10):
    """Получение списка рулонов"""
    return db.query(models.Roll).offset(skip).limit(limit).all()


def get_rool(db: Session, roll_id: int):
    """Получение одного рулона по id"""
    return db.query(models.Roll).filter(models.Roll.id == roll_id).first()


def create_roll(db: Session, roll: schemas.RollCreate):
    """Создаём новый рулон в БД"""
    db_roll = models.Roll(length=roll.length, weight=roll.weight)
    db.add(db_roll)
    db.commit()
    db.refresh(db_roll)
    return db_roll


def delete_roll(db: Session, roll_id: int):
    """Удаление рулона"""
    db_roll = db.query(models.Roll).filter(models.Roll.id == roll_id).first()
    if db_roll:
        db.delete(db_roll)
        db.commit()
        return db_roll
