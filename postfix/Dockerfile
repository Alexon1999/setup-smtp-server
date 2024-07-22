FROM ubuntu:latest

RUN apt-get update && apt-get install -y postfix postfix-pgsql

COPY configs/main.cf /etc/postfix/main.cf
# COPY configs/master.cf /etc/postfix/master.cf
COPY configs/postfix-lookup /etc/postfix/postfix-lookup

EXPOSE 25 587

CMD ["postfix", "start-fg"]
