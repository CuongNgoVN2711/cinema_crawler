FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /web
WORKDIR /web/src
ADD . /web
RUN pip install -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate