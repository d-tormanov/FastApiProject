from sqlalchemy import Column, Integer, String
from models.base import Base


class PerevalArea(Base):
    __tablename__ = 'pereval_areas'

    id = Column(Integer, primary_key=True)
    id_parent = Column(Integer, nullable=False)
    title = Column(String(255), nullable=False)
