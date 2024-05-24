from sqlalchemy.orm import Session

from . import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, value=product.value)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_product_by_name(db: Session, product_name: str):
    return db.query(models.Product).filter(models.Product.name == product_name).first()

def get_products(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Product).offset(skip).limit(limit).all

def update_product(db: Session, db_product: models.Product, product: schemas.ProductUpdate):
    product_data = product.model_dump(exclude_unset=True)
    db_product.sqlmodel_update(product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, db_product: models.Product):
    db.delete(db_product)
    db.commit()
    return {"ok": True}