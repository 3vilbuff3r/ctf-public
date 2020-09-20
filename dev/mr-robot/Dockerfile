FROM ubuntu:16.04

LABEL Description="M365 CTF challenge docker image: Mr. Robot"
LABEL Author="3vilbuff3r"

RUN apt-get update
RUN apt-get install apache2 -y
RUN apt clean
RUN mkdir /var/www/html/206cac20-e908-4e95-94e2-f439be754838

ADD index.html /var/www/html/index.html
ADD robot.jpeg /var/www/html/robot.jpeg
ADD robots.txt /var/www/html/robots.txt
ADD flag.txt /var/www/html/206cac20-e908-4e95-94e2-f439be754838/flag.txt

EXPOSE 80
CMD apachectl -D FOREGROUND