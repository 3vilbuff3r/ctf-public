FROM ubuntu:16.04

LABEL Description="M365 CTF challenge docker image: Mr. Robot"
LABEL Author="3vilbuff3r"

RUN apt-get update
RUN apt-get install unzip apache2 -y
RUN apt clean
RUN rm /var/www/html/index.html
ADD content.zip /tmp/content.zip

RUN unzip /tmp/content.zip -d /var/www/html/

EXPOSE 80
CMD apachectl -D FOREGROUND