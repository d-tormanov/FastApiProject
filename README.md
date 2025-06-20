# Pereval REST API

FastAPI сервис для передачи данных о горных перевалах в Федерацию спортивного туризма России (ФСТР). Туристы отправляют информацию, модераторы проверяют, а пользователи могут отслеживать статус заявок и просматривать базу перевалов.

## Возможности

- Отправка данных о перевале с фотографиями
- Проверка статуса модерации
- Редактирование заявки (если статус `new`)
- Просмотр заявок пользователя по email
- Документация Swagger / ReDoc

## Установка и запуск

```bash
# Клонируйте репозиторий
git clone https://github.com/d-tormanov/FastApiProject
cd FastApiProject

# Установите зависимости
uv pip install -r <(uv pip compile)

# Скопируйте и настройте переменные окружения
cp .env.example .env

# Настройте и запустите PostgreSQL в docker-compose
docker compose up --build

# Генерация миграций Alembiс
alembic revision --autogenerate -m "autogen"

# Применение миграций Alembic
alembic upgrade head

# Запуск приложения
uvicorn main:app --reload

# API доступен по адресу
http://127.0.0.1:8000/

# Swagger UI по адресу
http://127.0.0.1:8000/docs

# Запуск тестов
pytest tests/
```

### .env пример

```env
DATABASE_URL=postgresql+asyncpg://user:password@host:port/dbname
```

## API эндпоинты

| Метод | Путь                                  | Описание                            |
| ----- | ------------------------------------- | ----------------------------------- |
| POST  | `/submitData`                         | Создание записи о перевале          |
| GET   | `/submitData/{id}`                    | Получение записи по ID              |
| PATCH | `/submitData/{id}`                    | Обновление записи со статусом `new` |
| GET   | `/submitData/?user_id__email={email}` | Получение всех заявок по email      |

## Пример POST запроса на добавление нового объекта

```json
{
  "beauty_title": "Вершина",
  "title": "Купол трёх озер",
  "other_titles": "Купол Актру",
  "connect": "хребет",
  "add_time": "2021-09-22 13:18:13",
  "user": {
    "email": "perg@example.com",
    "phone": "+13337772548",
    "fam": "Анисимов",
    "name": "Владимир",
    "otc": "Петрович"
  },
  "coords": {
    "latitude": "50.048400",
    "longitude": "87.796590",
    "height": 3556
  },
  "level": {
    "winter": "1Б",
    "summer": "1Б",
    "autumn": "1Б",
    "spring": "1Б"
  },
  "images": [
    {
      "image": "https://example.com/kupol.jpg",
      "title": "Купол"
    }
  ]
}
```

## Проект опубликован на хостинге Raillway(https://railway.com/)

- **API**: [pereval API](https://fastapiproject-production-b53d.up.railway.app/)
- **Swagger**: [документация Swagger](https://fastapiproject-production-b53d.up.railway.app/docs/)
- **ReDoc**: [документация ReDoc](https://fastapiproject-production-b53d.up.railway.app/redoc/)

---

> Проект разработан в рамках виртуальной стажировки SkillFactory для ФСТР.

