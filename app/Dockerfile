FROM python:3.6
MAINTAINER Guilherme Lustri "lustrigui@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt