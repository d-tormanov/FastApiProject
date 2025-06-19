from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import async_session
from schemas.pereval import PerevalCreate
from services.pereval import PerevalService
from fastapi.responses import JSONResponse
from fastapi import Query

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

@router.get("/submitData/{id}")
async def get_pereval(id: int, session: AsyncSession = Depends(get_session)):
    pereval = await PerevalService.get_pereval_by_id(session, id)
    if not pereval:
        return JSONResponse(status_code=404, content={"message": "Не найдено"})
    return pereval


@router.patch("/submitData/{id}")
async def update_pereval(id: int, data: PerevalCreate, session: AsyncSession = Depends(get_session)):
    return await PerevalService.update_pereval(session, id, data)


@router.get("/submitData/")
async def list_user_perevals(user__email: str = Query(...), session: AsyncSession = Depends(get_session)):
    perevals = await PerevalService.get_perevals_by_email(session, user__email)
    return perevals