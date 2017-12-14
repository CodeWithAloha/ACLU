FROM python:3.4-alpine

LABEL maintainer "project-aclu@codeforhawaii.org"

RUN apk add --update git 

# gunicorn gevent dependencies 
RUN apk add --update gcc musl-dev

ADD ./api/requirements.txt /src/requirements.txt

RUN cd /src; pip install --no-cache-dir -r requirements.txt --upgrade

ADD ./api/ /src

EXPOSE 50050

WORKDIR /src

CMD ["gunicorn", "-k", "gevent", "--bind", "0.0.0.0:50050", "app:app", "--reload", "--capture-output", "--enable-stdio-inheritance", "--access-logfile", "-", "--error-logfile", "-"]
