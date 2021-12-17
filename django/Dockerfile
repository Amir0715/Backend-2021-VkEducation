FROM python:3.9
LABEL maintainer="kamolov.amir2000@yandex.ru"

RUN apt-get update
RUN apt-get install -y build-essential gcc libc6-dev wget
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev musl-dev unzip libaio-dev postgresql-client

RUN pip install poetry

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/
COPY ./pyproject.toml ./
COPY ./poetry.lock ./
RUN poetry install

RUN rm -rf ./.env.prod
COPY ./.env.prod ./
COPY ./metroim ./metroim

RUN poetry run python ./metroim/manage.py collectstatic --noinput

WORKDIR /app/metroim/

EXPOSE 8000

CMD [ "poetry", "run", "gunicorn", "--reload", "--bind", "0.0.0.0:8000", "application.wsgi:application" ]