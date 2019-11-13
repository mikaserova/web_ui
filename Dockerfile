FROM python:3

COPY . /v1
WORKDIR /v1

USER root
RUN python3 -m venv env
RUN . env/bin/activate 

RUN wget -O - http://packages.couchbase.com/ubuntu/couchbase.key | apt-key add -
# Adding Ubuntu 18.04 repo to apt/sources.list of 18.10 or 19.04
RUN echo "deb http://packages.couchbase.com/ubuntu bionic bionic/main" | tee /etc/apt/sources.list.d/couchbase.list
RUN apt-get update

RUN  apt-get install -y libcouchbase2-libevent libcouchbase-dev build-essential
RUN   pip3 install -r requirements.txt


EXPOSE 5000:5000 
CMD python ./run.py