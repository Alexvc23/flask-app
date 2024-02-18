FROM python:3.13.0a4-alpine3.18

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY ./App.py /app/