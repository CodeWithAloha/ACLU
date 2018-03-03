FROM python:3.4-alpine

LABEL maintainer "project-aclu@codeforhawaii.org"

ARG MONGO_HOST="localhost"
ARG MONGO_PORT="27017"
ARG MONGO_USERNAME=""
ARG MONGO_PASSWORD=""
ARG MONGO_DBNAME="aclu"

RUN apk add --update git 

# gunicorn gevent dependencies
RUN apk add --update gcc musl-dev

ADD ./api/requirements.txt /src/requirements.txt

RUN cd /src; pip install --no-cache-dir -r requirements.txt --upgrade

ADD ./api/ /src

EXPOSE 50050

WORKDIR /src

ENV MONGO_HOST $MONGO_HOST
ENV MONGO_PORT $MONGO_PORT
ENV MONGO_USERNAME $MONGO_USERNAME
ENV MONGO_PASSWORD $MONGO_PASSWORD
ENV MONGO_DBNAME $MONGO_DBNAME

CMD ["gunicorn", "-k", "gevent", "--bind", "0.0.0.0:50050", "app:app", "--reload", "--capture-output", "--enable-stdio-inheritance", "--access-logfile", "-", "--error-logfile", "-"]
