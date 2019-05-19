FROM python:2

LABEL Summary="ARA records Ansible Playbook runs and provides intuitive interfaces to browse them"
LABEL URL="https://github.com/openstack/ara"

RUN apt-get update && apt-get install netcat -y
RUN pip install --upgrade pip \
    && pip install pymysql psycopg2 \ 
    && pip install git+https://git.openstack.org/openstack/ara
ADD https://raw.githubusercontent.com/jakedevans/docker-compose-wait/1.0.0/wait.sh /wait.sh
RUN chmod +x /wait.sh
CMD /wait.sh && /usr/local/bin/ara-manage runserver -h 0.0.0.0 -p 8080
EXPOSE 8080
