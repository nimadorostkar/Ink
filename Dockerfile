FROM python:3.10-slim-buster

WORKDIR /ink

COPY /requirements/requirements.txt /ink/requirements/

RUN pip install --upgrade pip

RUN apt-get update && apt-get upgrade -y

RUN pip install -r requirements/requirements.txt

COPY . /ink


EXPOSE 8000 9000