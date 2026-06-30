from sqlalchemy.orm import Session
from app.models import TodosModel

def get_all(db: Session):
    return db.query(TodosModel).all()

def get_one_by_id(db: Session, id: int):
    return db.query(TodosModel).filter(TodosModel.id == id).first()

def create(db: Session, data: TodosModel):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data

def update(db: Session, data: TodosModel):
    db.commit()
    db.refresh(data)
    return data

def delete(db: Session, data: TodosModel):
    db.delete(data)
    db.commit()