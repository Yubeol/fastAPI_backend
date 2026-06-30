from sqlalchemy.orm import Session
from app.models import SalesModel


def get_all(db: Session):
    return db.query(SalesModel).all()


def get_one_by_id(db: Session, id: int):
    return db.query(SalesModel).filter(SalesModel.id == id).first()


def create(db: Session, data: SalesModel):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update(db: Session, data: SalesModel):
    db.commit()
    db.refresh(data)
    return data


def delete(db: Session, data: SalesModel):
    db.delete(data)
    db.commit()