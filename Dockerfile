FROM python:3.8-alpine

ENV LANG C.UTF-8


# install dev packages

RUN set -ex \
  && apk add --no-cache \
    postgresql-dev \
    build-base \
    libffi-dev

RUN set -ex \
  && pip install poetry


# install dev dependencies

ENV POETRY_VIRTUALENVS_IN_PROJECT 1

COPY pyproject.toml poetry.lock ./

RUN set -ex \
  && poetry install


ENV PYTHONDONTWRITEBYTECODE 1
