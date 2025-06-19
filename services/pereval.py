from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from models import User, Coordinates, DifficultyLevel, Image, Pereval
from models.pereval import StatusEnum
from schemas.pereval import PerevalCreate
from sqlalchemy.orm import selectinload
from sqlalchemy import delete


class PerevalService:

    @staticmethod
    async def add_pereval(session: AsyncSession, data: PerevalCreate) -> dict:
        try:
            # 1. Пользователь
            stmt = select(User).where(User.email == data.user.email)
            result = await session.execute(stmt)
            user = result.scalars().first()

            if not user:
                user = User(**data.user.dict())
                session.add(user)
                await session.flush()

            # 2. Координаты
            coords = Coordinates(**data.coords.dict())
            session.add(coords)
            await session.flush()

            # 3. Уровень сложности
            level = DifficultyLevel(**data.level.dict())
            session.add(level)
            await session.flush()

            # 4. Перевал
            pereval = Pereval(
                beauty_title=data.beauty_title,
                title=data.title,
                other_titles=data.other_titles,
                connect=data.connect,
                add_time=data.add_time,
                status=StatusEnum.new,
                user_id=user.id,
                coords_id=coords.id,
                level_id=level.id
            )
            session.add(pereval)
            await session.flush()

            # 5. Фото
            for img in data.images:
                image = Image(
                    pereval_id=pereval.id,
                    image_url=img.image_url,
                    title=img.title
                )
                session.add(image)

            await session.commit()

            return {"status": 200, "message": "Успешное отправление", "id": pereval.id}

        except SQLAlchemyError as e:
            await session.rollback()
            return {
                "status": 500,
                "message": f"Ошибка при сохранении: {str(e)}",
                "id": None
            }


    @staticmethod
    async def get_pereval_by_id(session: AsyncSession, pereval_id: int):
        result = await session.execute(
            select(Pereval).where(Pereval.id == pereval_id)
            .options(
                selectinload(Pereval.user),
                selectinload(Pereval.coords),
                selectinload(Pereval.level),
                selectinload(Pereval.images)
            )
        )
        pereval = result.scalars().first()
        return pereval


    @staticmethod
    async def update_pereval(session: AsyncSession, pereval_id: int, data: PerevalCreate):
        result = await session.execute(
            select(Pereval)
            .options(
                selectinload(Pereval.coords),
                selectinload(Pereval.level),
                selectinload(Pereval.images)
            )
            .where(Pereval.id == pereval_id)
        )
        pereval = result.scalars().first()

        if not pereval:
            return {"state": 0, "message": "Запись не найдена"}

        if pereval.status != StatusEnum.new:
            return {"state": 0, "message": f"Редактирование запрещено: статус '{pereval.status}'"}

        pereval.beauty_title = data.beauty_title
        pereval.title = data.title
        pereval.other_titles = data.other_titles
        pereval.connect = data.connect
        pereval.add_time = data.add_time

        for field in ("latitude", "longitude", "height"):
            setattr(pereval.coords, field, getattr(data.coords, field))

        for season in ("winter", "summer", "autumn", "spring"):
            setattr(pereval.level, season, getattr(data.level, season))

        await session.execute(delete(Image).where(Image.pereval_id == pereval.id))
        for img in data.images:
            session.add(Image(pereval_id=pereval.id, image_url=img.image_url, title=img.title))

        await session.commit()
        return {"state": 1, "message": "Запись успешно обновлена"}


    @staticmethod
    async def get_perevals_by_email(session: AsyncSession, email: str):
        stmt = select(Pereval).join(User).where(User.email == email)
        result = await session.execute(
            stmt.options(
                selectinload(Pereval.user),
                selectinload(Pereval.coords),
                selectinload(Pereval.level),
                selectinload(Pereval.images)
            )
        )
        return result.scalars().all()
