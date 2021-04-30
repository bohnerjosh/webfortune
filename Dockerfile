FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y fortune fortunes
RUN apt-get install -y cowsay
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip

env path=$path:/usr/games
env lc_all=c.utf-8
env lang=c.utf-8

FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY appserver.py appserver.py
ENV FLASK_APP=appserver.py

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
