FROM python:3.12-slim

RUN apt-get update && apt-get install -y build-essential curl

RUN pip install --upgrade pip setuptools wheel

WORKDIR /app

COPY pyproject.toml ./

RUN pip install .

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
