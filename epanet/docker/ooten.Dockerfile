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
# NOTE: we need to replace the '~' with the actual path as it causes
# errors in the delft3d build script
RUN df -h

ADD tags/ooten /epanet
RUN ["chmod", "+x", "/epanet/configure"]

RUN cd /epanet \
  && ./configure \
  && make \
  && make install

