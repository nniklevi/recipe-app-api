FROM python:3.7-alpine
LABEL maintainer=Nenad

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN addgroup -S appgroup && adduser -S user -G appgroup -D
USER user


