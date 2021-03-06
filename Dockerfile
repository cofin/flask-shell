FROM python:latest
MAINTAINER Cody Fincher <cody.fincher@gmail.com>

ENV INSTALL_PATH /src
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app.app:create_app()"
