FROM ubuntu:16.04

LABEL Description="M365 CTF challenge docker image: Mr. Robot"
LABEL Author="3vilbuff3r"

RUN apt-get update
RUN apt-get install unzip socat wget net-tools apt-transport-https gcc g++ -y
RUN wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get update && apt-get install -y dotnet-sdk-3.1
RUN apt clean
RUN useradd user
RUN mkdir -p /home/user/project

ADD project.zip /home/user/project.zip
RUN unzip /home/user/project.zip -d /home/user/project/

WORKDIR /home/user/project/project/
RUN dotnet build

EXPOSE 20000
CMD su -c "socat -T30 TCP-LISTEN:20000,reuseaddr,fork EXEC:/home/user/project/project/bin/Debug/netcoreapp3.1/project" - user