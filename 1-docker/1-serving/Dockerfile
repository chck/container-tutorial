FROM python:3.8-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake \
    build-essential \
    git \
 && apt-get autoremove -y && apt-get clean && rm -rf /usr/local/src/*

run pip install --no-cache-dir poetry~=1.1.6 \
 && poetry config virtualenvs.create false

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]
