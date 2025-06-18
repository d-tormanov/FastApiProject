from sqlalchemy import Column, Integer, String
from models.base import Base
from sqlalchemy.orm import relationship


class DifficultyLevel(Base):
    __tablename__ = 'difficulty_levels'

    id = Column(Integer, primary_key=True)
    winter = Column(String(10))
    summer = Column(String(10))
    autumn = Column(String(10))
    spring = Column(String(10))

    pereval = relationship("Pereval", back_populates="level")
