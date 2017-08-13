FROM python:3.4-alpine

LABEL maintainer "project-aclu@codeforhawaii.org"

ADD ./api /src/

RUN cd /src; pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV MONGO_HOST db

CMD ["python", "/src/app.py"]
