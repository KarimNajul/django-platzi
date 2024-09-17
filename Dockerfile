FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

RUN apt-get update && apt-get install -y postgresql-client

COPY requirements.txt /code/

RUN python -m pip install -r requirements.txt

COPY . /code/
