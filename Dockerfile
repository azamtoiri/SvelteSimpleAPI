FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apt-get update \
    && apt-get install -y --no-install-recommends make curl \
    && apt-get clean

RUN pip install --no-cache-dir poetry==1.7.1

COPY pyproject.toml ./

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . .

ENTRYPOINT ["make", "run_migrations_server"]
EXPOSE 8080