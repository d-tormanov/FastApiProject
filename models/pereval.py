from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base


class StatusEnum(str, PyEnum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'


class Pereval(Base):
    __tablename__ = 'perevals'

    id = Column(Integer, primary_key=True)
    beauty_title = Column(String(255))
    title = Column(String(255), nullable=False)
    other_titles = Column(String(255))
    connect = Column(String(255))
    add_time = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(StatusEnum), default=StatusEnum.new)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    coords_id = Column(Integer, ForeignKey('coords.id'), nullable=False)
    level_id = Column(Integer, ForeignKey('difficulty_levels.id'), nullable=False)

    user = relationship("User", back_populates="perevals")
    coords = relationship("Coordinates", back_populates="pereval")
    level = relationship("DifficultyLevel", back_populates="pereval")
    images = relationship("Image", back_populates="pereval", cascade="all, delete-orphan")
