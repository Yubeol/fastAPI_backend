from sqlalchemy.orm import Session
from app.models import UsersModel


def get_all(db: Session):
    return db.query(UsersModel).all()


def get_one_by_id(db: Session, id: int):
    return db.query(UsersModel).filter(UsersModel.id == id).first()


def get_by_name(db: Session, name: str):
    return db.query(UsersModel).filter(UsersModel.username == name).first()

def create(db: Session, data: UsersModel):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update(db: Session, data: UsersModel):
    db.commit()
    db.refresh(data)
    return data


def delete(db: Session, data: UsersModel):
    db.delete(data)
    db.commit()