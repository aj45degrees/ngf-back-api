FROM python:3.9-alpine3.14
LABEL maintainer="45deg"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# for security use a non-root user
RUN adduser -D user
USER user

