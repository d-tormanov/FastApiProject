from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import async_session
from schemas.pereval import PerevalCreate
from services.pereval import PerevalService

router = APIRouter()

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@router.post("/submitData")
async def submit_data(
    data: PerevalCreate,
    session: AsyncSession = Depends(get_session)
):
    result = await PerevalService.add_pereval(session, data)
    return result
