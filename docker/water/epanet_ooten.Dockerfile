FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
  autoconf \
  libtool \
  flex \
  g++ \
  gfortran \
  libstdc++6 \
  byacc \
  libexpat1-dev \
  uuid-dev \
  build-essential \
  wget \
  pkg-config \
  gedit

# Epanet
RUN df -h

ADD epanet/tags/ooten /epanet
# RUN ["chmod", "+x", "/epanet/configure"]

RUN apt-get install -y \
  cmake

RUN mkdir /epanet/build

RUN cd /epanet/build \
  && cmake ../

RUN cd /epanet/build \
  && make
  
# RUN cd /epanet/build/cmake \
#   && make install

