FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root --no-cache

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "python", "main.py"]