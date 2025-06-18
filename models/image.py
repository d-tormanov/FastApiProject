from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, ForeignKey


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    pereval_id = Column(Integer, ForeignKey('perevals.id'), nullable=False)
    image_url = Column(Text, nullable=False)
    title = Column(String(255), nullable=True)

    pereval = relationship("Pereval", back_populates="images")
