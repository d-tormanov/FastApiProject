FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl tar

RUN curl -L https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz \
    | tar -xz -C /usr/local/bin --strip-components=1 uv

WORKDIR /app

COPY pyproject.toml ./

RUN uv pip compile pyproject.toml -o requirements.txt && uv pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uv", "pip", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
