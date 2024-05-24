from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    value: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(SQLModel):
    name: str | None = None
    value: float | None = None

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True