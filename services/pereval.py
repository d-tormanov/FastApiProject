from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from models import User, Coordinates, DifficultyLevel, Image, Pereval
from models.pereval import StatusEnum
from schemas.pereval import PerevalCreate


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
