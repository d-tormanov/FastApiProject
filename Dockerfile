FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential curl

RUN pip install --upgrade pip setuptools wheel

WORKDIR /app

COPY pyproject.toml ./

RUN pip install .

COPY . .

RUN mkdir -p /app/alembic/versions

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 8000

CMD ["/start.sh"]
