FROM wizardsofindustry/quantum:latest

RUN mkdir /var/lib/hbts
RUN mkdir /var/spool/aorta
RUN pip3 install rfc3161ng==2.0.4
RUN pip3 install dsnparse==0.1.11

COPY . /app
COPY etc/ /etc/hbts/

WORKDIR /app
RUN python3 setup.py install

ENV QUANTUM_DEPLOYMENT_ENV development
ENV AORTA_SPOOL_DIR /var/spool/aorta
ENV HBTS_SECRET_KEY 197fb52f8305c461a677256c3cb588e64936dc814e8fcda98f5a0148be514da6
ENV HBTS_DEBUG 1
ENV HBTS_IOC_DEFAULTS /etc/hbts/ioc.conf
ENV HBTS_IOC_DIR /etc/hbts/ioc.conf.d/
ENV HBTS_RDBMS_DSN postgresql+psycopg2://hbts:hbts@rdbms:5432/hbts
ENV HBTS_HTTP_ADDR 0.0.0.0
ENV HBTS_HTTP_PORT 8443
ENV HBTS_TSA_REQUEST_URI https://freetsa.org/tsr
ENV HBTS_RUNTIME service

ENV SQ_TESTING_PHASE lint
RUN ./bin/run-tests

ENTRYPOINT ["./bin/docker-entrypoint"]
