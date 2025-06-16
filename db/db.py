from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from fastapi import Depends
from typing import Annotated
from core.config import app_settings


engine = create_async_engine(str(app_settings.postgres_dsn))

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session

db_dependency = Annotated[AsyncSession, Depends(get_async_session)]
