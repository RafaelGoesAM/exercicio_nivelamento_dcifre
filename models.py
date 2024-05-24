from sqlalchemy import Column, Float, Integer, String

from .database import Base

class Product(Base): 
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Float)