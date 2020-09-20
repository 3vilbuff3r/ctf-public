FROM ubuntu:16.04

LABEL Description="M365 CTF challenge docker image: Mr. Robot"
LABEL Author="3vilbuff3r"

RUN apt-get update
RUN apt-get install apache2 php libapache2-mod-php net-tools vim wget curl -y
RUN apt clean
RUN rm /var/www/html/index.html

ADD index.php /var/www/html/index.php

RUN chown www-data:www-data /var/www/html -R
EXPOSE 80
CMD apachectl -D FOREGROUND