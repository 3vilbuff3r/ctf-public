FROM ubuntu:16.04

LABEL Description="M365 CTF challenge docker image: Mr. Robot"
LABEL Author="3vilbuff3r"
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install apache2 php libapache2-mod-php net-tools vim wget curl mysql-server php-mysql -y
RUN apt-get install unzip
RUN apt clean

RUN rm /var/www/html/index.html
ADD content.zip /tmp/content.zip
RUN unzip /tmp/content.zip -d /var/www/html

ADD db.sql /tmp/db.sql
RUN service mysql start; mysql < /tmp/db.sql; mysqladmin --user=root password "root" 

RUN chown www-data:www-data /var/www/html -R
EXPOSE 80
CMD service mysql start; apachectl -D FOREGROUND