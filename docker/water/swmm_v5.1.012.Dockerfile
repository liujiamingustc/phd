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

# SWMM
RUN df -h

ADD swmm/tags/v5.1.012 /swmm
RUN cp /swmm/engine/makefiles/Makefile /swmm/engine/src/Makefile
# RUN ["chmod", "+x", "/swmm/engine/configure"]

RUN ls /swmm/engine/src

RUN cd /swmm/engine/src \
  && make
  
RUN ls /swmm/engine/src

# RUN cd /swmm/engine/src \
#   && make install

