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

ADD tags/5.1.012 /swmm
# RUN ["chmod", "+x", "/swmm/engine/configure"]

# RUN cd /swmm/engine \
#   && ./configure \
#   && make \
#   && make install

