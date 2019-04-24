# DockertFile for the Massive-PotreeConverter

# FROM i386/ubuntu:16.04
FROM i386/ubuntu:xenial
MAINTAINER Gijs van den Oord <g.vandenoord@esciencecenter.nl>
RUN apt-get update -y

# INSTALL compilers and build toold
RUN apt-get install -y apt-utils software-properties-common git cmake build-essential gcc g++ python-numpy python-dev python-pip lsb wget

# INSTALL libraries
RUN apt-get install -y libboost-all-dev libncurses5-dev libncursesw5-dev freeglut3-dev qtdeclarative5-dev libqwt-dev libqwt-headers xsdcxx
RUN pip install --upgrade pip
RUN pip install docopt
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
RUN apt-get update
RUN apt install -y libgdal-dev gdal-bin python-gdal libgdal20
# Configure & build
# WORKDIR /opt
# RUN apt purge -y --auto-remove cmake
# ENV version=3.12
# ENV build=1
# RUN wget https://cmake.org/files/v$version/cmake-$version.$build-Linux-x86_64.sh 
# RUN mkdir /opt/cmake
# RUN sh cmake-$version.$build-Linux-x86_64.sh --prefix=/opt/cmake --skip-license
# RUN ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake

WORKDIR /opt
RUN git clone https://github.com/DeltaresProjects/HYD_SIM-pcraster.git

WORKDIR /opt/HYD_SIM-pcraster
RUN git submodule update --init --recursive
RUN mkdir build

WORKDIR /opt/HYD_SIM-pcraster/source/fern
# RUN echo 'set( CURSES_LIBRARY "/usr/lib/i386-linux-gnu/libncurses.so")' | cat - CMakeLists.txt > temp && mv temp CMakeLists.txt
# RUN echo 'set( CURSES_INCLUDE_PATH "/usr/include/curses.h")' | cat - CMakeLists.txt > temp && mv temp CMakeLists.txt
RUN sed -i '10i set( CURSES_LIBRARY "/usr/lib/i386-linux-gnu/libncurses.so")' CMakeLists.txt
RUN sed -i '11i set( CURSES_INCLUDE_PATH "/usr/include/curses.h")' CMakeLists.txt


WORKDIR /opt/HYD_SIM-pcraster/build
RUN cmake .. -DGDAL_LIBRARY=/usr/lib/libgdal.so.20 -DGDAL_INCLUDE_DIR=/usr/include/gdal -DCMAKE_CXX_FLAGS="-Wno-deprecated"
# RUN make
RUN make install