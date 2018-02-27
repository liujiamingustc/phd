FROM ubuntu:16.04
#FROM ubuntu:14.04

MAINTAINER Quan Pan <quanpan302@hotmail.com>

# ===========
#  essential
# ===========
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
  pkg-config \
  libssl-dev \
  libffi-dev \
  wget \
  vim \
  cmake \
  git

# python3
RUN apt-get install -y \
  python3-pip \
  python3-dev


# ===========
# version old
# ===========
RUN gfortran --version \
    && gcc --version \
    && g++ --version \
    && python3 -v \
    && cmake --version \
    && git --version


# ==============
# version update
# ==============
# g++ >= 6.0
# https://gist.github.com/application2000/73fd6f4bf1be6600a2cf9f56315a2d91
RUN apt-get update && apt-get install -y \
  build-essential \
  software-properties-common

RUN add-apt-repository -y \
  ppa:ubuntu-toolchain-r/test

RUN apt-get update && apt-get install -y \
  gcc-snapshot

RUN apt-get update && apt-get install -y \
  gcc-6 \
  g++-6

RUN update-alternatives \
  --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 \
  --slave /usr/bin/g++ g++ /usr/bin/g++-6

# gfortran
RUN apt-get update && apt-get install -y \
  gfortran

# gtest
RUN git clone -q https://github.com/google/googletest.git /googletest \
  && mkdir -p /googletest/build \
  && cd /googletest/build \
  && cmake .. && make && make install \
  && cd / && rm -rf /googletest

# Swig
# RUN cd / \
#   && git clone https://github.com/swig/swig.git \
#   && cd swig \
#   && ./autogen.sh \
#   && ./configure \
#   && make
RUN apt-get update && apt-get install -y \
  swig


# ===========
# version new
# ===========
RUN gfortran --version \
    && gcc --version \
    && g++ --version \
    && python3 -v \
    && cmake --version \
    && git --version

# python3 pip3
RUN pip3 install \
  numpy \
  mock
# RUN pip3 install \
#   mpi4py

# python3 test
RUN which python
RUN which python3
RUN python3 -c "import numpy; print(numpy.__version__)"


# ============
# project code
# ============
RUN df -h

# ADD project/tags/version /project

# RUN cd /project \
#   && python setup.py install
# RUN cd /project \
#   && python3 setup.py install

# WORKDIR /project
