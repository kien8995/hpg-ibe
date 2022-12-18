FROM python:3.9.15

RUN mkdir /app

WORKDIR /app

COPY ./src /app
COPY ./requirements.txt /app

ENV PYTHONPATH /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc git libssl-dev g++ make && \
    cd /tmp && git clone https://github.com/edenhill/librdkafka.git && \
    cd librdkafka && git checkout tags/v1.9.2 && \
    ./configure && make && make install && ldconfig && \
    cd ../ && rm -rf librdkafka

RUN pip install -r requirements.txt

CMD [ "python", "modules/cosco/kafka_consumer.py" ]