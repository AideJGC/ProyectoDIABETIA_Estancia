FROM ubuntu:20.04
USER root
ENV TIMEZONE America/Mexico_City
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV DEB_BUILD_DEPS="python3-dev python3-pip python3-setuptools"
ENV DEB_PACKAGES="sudo nano less git wget curl ca-certificates"

RUN apt-get update && export $DEBIAN_FRONTEND && \
    echo $TIMEZONE > /etc/timezone && apt-get install -y tzdata

RUN apt-get update && apt-get install -y $DEB_PACKAGES $DEB_BUILD_DEPS && pip3 install --upgrade pip

# Install python 3.7
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3.7 -y
 
# Make python 3.7 the default
RUN echo "alias python=python3.7" >> ~/.bashrc
RUN export PATH=${PATH}:/usr/bin/python3.7
RUN /bin/bash -c "source ~/.bashrc"
 
RUN curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - && apt-get install -y nodejs

WORKDIR /

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN git clone https://github.com/AideJGC/ProyectoDIABETIA_Estancia

WORKDIR ProyectoDIABETIA_Estancia/src/diabetia_hta
ENTRYPOINT ["python", "diabetia_hta.py"]
