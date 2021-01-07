# Buildimage
FROM python:3.9-alpine as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"


ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM python-base as builder-base
RUN apk --no-cache add build-base curl postgresql-dev

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev

# Baseimage
FROM python-base as production

COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY . /app/
WORKDIR /app

RUN apk --no-cache add py3-psycopg2 curl

RUN rm -f poetry.lock pyproject.toml Dockerfile docker-compose.yml
RUN chmod +x /app/docker/*.sh

CMD ["/app/docker/entrypoint.sh"]

HEALTHCHECK --interval=2m --timeout=3s \
  CMD curl -f http://127.0.0.1:8000/api/admin/ || exit 1