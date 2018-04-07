FROM python:3.5

ENV DEBIAN_FRONTEND noninteractive

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update \
  && apt-get clean \
  && pip3 install -r /tmp/requirements.txt

ENV FLASK_DEBUG=1

RUN mkdir -p /app ; \
   mkdir -p /app/logs;

ADD src/ /app/
WORKDIR /app

COPY config.yml .

CMD python3 -u main.py
