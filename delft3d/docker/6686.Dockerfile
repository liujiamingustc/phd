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
  ruby \
  build-essential \
  wget \
  pkg-config \
  gedit

#zlib
ENV v=1.2.8
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/zlib-${v}.tar.gz \
    && tar -xf zlib-${v}.tar.gz \
    && cd zlib-${v} \
    && ./configure --prefix=/usr/local \
    && make install

#hdf5
ENV v=1.8.13
ENV HDF5_DIR="/root/Downloads/libraries/hdf5-${v}"
RUN wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4/hdf5-${v}.tar.gz \
    && tar -xf hdf5-${v}.tar.gz \
    && cd hdf5-${v} \
    && ./configure --enable-shared --enable-hl --prefix=$HDF5_DIR \
    && make -j 2 \
    && make install

