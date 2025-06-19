FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl ca-certificates bash && \
    curl -LsSf https://astral.sh/uv/install.sh | bash && \
    mv /root/.cargo/bin/uv /usr/local/bin/uv && \
    chmod +x /usr/local/bin/uv && \
    rm -rf /root/.cargo

WORKDIR /app

COPY pyproject.toml ./

RUN uv pip compile pyproject.toml -o requirements.txt \
 && uv pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uv", "pip", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
