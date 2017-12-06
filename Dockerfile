FROM ubuntu:16.04

RUN apt-get update

RUN apt-get -y install python
RUN apt-get -y install python-pip
#RUN pip install --upgrade pip
RUN pip install pyOpenSSL --upgrade

RUN pip install requests

ADD scripts/run_salt_sumo_events.sh /run_salt_sumo_events.sh
RUN chmod a+x /run_salt_sumo_events.sh

COPY /src /salt_sumo_events_py

