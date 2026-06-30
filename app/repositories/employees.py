from sqlalchemy.orm import Session
from app.models import EmployeeModel


def get_all(db: Session):
    return db.query(EmployeeModel).all()


def get_one_by_id(db: Session, id: int):
    return (db.query(EmployeeModel)
            .filter(EmployeeModel.id == id)
            .first())


def create(db: Session, data: EmployeeModel):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update(db: Session, data: EmployeeModel):
    db.commit()
    db.refresh(data)
    return data


def delete(db: Session, data: EmployeeModel):
    db.delete(data)
    db.commit()
