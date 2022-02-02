from haproxy:latest
USER root
RUN apt update && apt install python3-pip -y
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt 

COPY . .

EXPOSE 5000

COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
RUN chmod +x ./docker-entrypoint.sh 
ENTRYPOINT [ "./docker-entrypoint.sh" ]