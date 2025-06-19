FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app

COPY pyproject.toml /app/

RUN /root/.cargo/bin/uv pip install -r <( /root/.cargo/bin/uv pip compile pyproject.toml )

COPY . /app

EXPOSE 8000

CMD ["/root/.cargo/bin/uv", "pip", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
