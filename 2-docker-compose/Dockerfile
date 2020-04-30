FROM python:3.7-slim

RUN pip install --no-cache-dir poetry==1.0.* \
 && poetry config virtualenvs.create false

WORKDIR /app
COPY . .

RUN poetry install

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]
