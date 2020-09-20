FROM ubuntu:16.04

LABEL Description="M365 CTF challenge docker image: Mr. Robot"
LABEL Author="3vilbuff3r"

RUN apt-get update
RUN apt-get install unzip socat wget net-tools python3 python3-numpy -y
RUN apt clean 
RUN useradd user
RUN mkdir -p /home/user/

ADD runme.py /home/user/runme.py
RUN chmod u+x /home/user/runme.py
RUN chown user:user /home/user -R

EXPOSE 20000
CMD su -c "socat -T30 TCP-LISTEN:20000,reuseaddr,fork EXEC:/home/user/runme.py" - user