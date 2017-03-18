FROM alpine:3.3

ADD . /spatter
WORKDIR /spatter
RUN apk --update add py-gunicorn python py-pip && \
    pip install -U Flask boto3 && \
    python setup.py install

EXPOSE 8000

ENTRYPOINT /usr/bin/gunicorn --bind 0.0.0.0:8000 spatter:app

