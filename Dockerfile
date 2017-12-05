FROM ubuntu:16.04

RUN apt-get update

RUN apt-get -y install python
RUN apt -y install python-pip
RUN pip install pyOpenSSL --upgrade

RUN wget https://github.com/requests/requests/tarball/master/requests-requests-v2.18.4-109-g24092b1.tar.gz
RUN tar -xvzf requests-requests-v2.18.4-109-g24092b1.tar.gz
RUN cd requests-requests-v2.18.4-109-g24092b1 && pip install .

ADD scripts/run_salt_sumo_events.sh /run_salt_sumo_events.sh
RUN chmod a+x /run_salt_sumo_events.sh

COPY /src /salt_sumo_events_py

ENTRYPOINT ["/run_salt_sumo_events.sh"]