FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code

WORKDIR /code

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install ipython

COPY requirements.txt /code/

RUN python -m pip install -r requirements.txt

COPY . /code/
