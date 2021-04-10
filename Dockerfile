FROM python:3.7-alpine
LABEL maintainer=Nenad

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app
COPY ./.flake8 /app

RUN addgroup -S appgroup && adduser -S user -G appgroup -D
USER user
