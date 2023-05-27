ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

LABEL org.opencontainers.image.source=https://github.com/victoraugusto6/api-loan-django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

# mock secrets to deploy
CMD ["cp", "contrib/env-sample", ".env"]

WORKDIR /code

ENV DEBUG "False"

RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root --no-interaction
COPY . /code

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "onidata.wsgi"]
