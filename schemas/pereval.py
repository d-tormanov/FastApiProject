from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum


class StatusEnum(str, Enum):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'


class UserBase(BaseModel):
    email: EmailStr
    phone: str
    fam: str
    name: str
    otc: str


class CoordsBase(BaseModel):
    latitude: float
    longitude: float
    height: int


class LevelBase(BaseModel):
    winter: Optional[str]
    summer: Optional[str]
    autumn: Optional[str]
    spring: Optional[str]


class ImageBase(BaseModel):
    image_url: str
    title: Optional[str]


class PerevalBase(BaseModel):
    beauty_title: Optional[str]
    title: str
    other_titles: Optional[str]
    connect: Optional[str]
    add_time: Optional[datetime] = Field(default_factory=datetime.utcnow)
    status: Optional[StatusEnum] = StatusEnum.new

    user: UserBase
    coords: CoordsBase
    level: LevelBase
    images: List[ImageBase]


class PerevalCreate(PerevalBase):
    pass


class PerevalResponse(BaseModel):
    status: int
    message: str
    id: Optional[int] = None
