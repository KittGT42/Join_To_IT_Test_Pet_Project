FROM python:3.12-slim

WORKDIR /app

COPY event_manager .

RUN pip install poetry
RUN poetry install

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
