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

ADD epanet/tags/v2.0.12 /epanet
RUN ["chmod", "+x", "/epanet/configure"]

RUN cd /epanet \
  && ./configure \
  && make \
  && make install

