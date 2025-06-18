from sqlalchemy import Column, Integer, Float
from models.base import Base
from sqlalchemy.orm import relationship


class Coordinates(Base):
    __tablename__ = 'coords'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    height = Column(Integer, nullable=False)

    pereval = relationship("Pereval", back_populates="coords")
