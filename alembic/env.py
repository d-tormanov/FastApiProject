import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncConnection
from alembic import context

from db.db import Base
from core.config import app_settings


fileConfig(context.config.config_file_name)

target_metadata = Base.metadata

url = app_settings.postgres_url


def run_migrations_offline():
    """Запуск миграций в offline-режиме."""
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Асинхронное подключение к БД и запуск миграций."""
    connectable = create_async_engine(url, pool_pre_ping=True)

    async with connectable.connect() as connection:
        await connection.run_sync(
            lambda sync_conn: context.configure(
                connection=sync_conn,
                target_metadata=target_metadata,
            )
        )
        await connection.run_sync(context.run_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
