FROM python:3.8-slim

RUN pip install --no-cache-dir poetry~=1.1.6 \
 && poetry config virtualenvs.create false

WORKDIR /app
COPY . .

RUN poetry install

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]
