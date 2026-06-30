from sqlalchemy.orm import Session
from app.models import ProductModel


def get_all(db: Session):
    return db.query(ProductModel).all()


def get_one_by_id(db: Session, id: int):
    return db.query(ProductModel).filter(ProductModel.id == id).first()


def create(db: Session, data: ProductModel):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def update(db: Session, data: ProductModel):
    db.commit()
    db.refresh(data)
    return data


def delete(db: Session, data: ProductModel):
    db.delete(data)
    db.commit()