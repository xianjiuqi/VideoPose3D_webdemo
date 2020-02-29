FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
    python3.7 \
    python-pip
COPY . /web
WORKDIR /web
RUN pip install -r requirements.txt