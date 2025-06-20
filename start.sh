#!/bin/bash

mkdir -p alembic/versions

echo "Генерация миграций Alembiс..."
alembic revision --autogenerate -m "autogen" || echo "📭 Нет изменений для миграции"

echo "Применение миграций Alembic..."
alembic upgrade head

echo "Запуск FastAPI через Uvicorn..."
exec uvicorn main:app --host 0.0.0.0 --port 8000
