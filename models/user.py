from sqlalchemy import Column, Integer, String
from models.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    fam = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    otc = Column(String(100), nullable=False)

    perevals = relationship("Pereval", back_populates="user")
