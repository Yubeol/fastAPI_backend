from sqlalchemy.orm import Session
from app.models import UsersModel

def get_all(db: Session):
    return db.query(UsersModel).all()

def get_by_id(db: Session, user_id: int):
    return db.query(UsersModel).filter(UsersModel.id == user_id).first()

def get_by_name(db: Session, name: str):
    return db.query(UsersModel).filter(UsersModel.username == name).first()

def create(db: Session, user: UsersModel):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update(db: Session, user: UsersModel):
    db.commit()
    db.refresh(user)
    return user

def delete(db: Session, user: UsersModel):
    db.delete(user)
    db.commit()