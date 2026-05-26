from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base




class Container(Base):
    __tablename__ = "containers"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


    items = relationship("Item", back_populates="container")



class Item(Base):
    __tablename__ = "items"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    container_id = Column(Integer, ForeignKey("containers.id"))


    container = relationship("Container", back_populates="items")