# DockerFile for wflow
# the input data root directory should be mounted as /data
FROM pcraster
MAINTAINER Quan Pan <quanpan302@hotmail.com>
COPY . /opt/wflow/
RUN pip install netCDF4 gdal pyproj matplotlib scipy cython && pip install netcdftime
WORKDIR /opt/wflow/wflow-py
RUN python setup.py install
VOLUME /data
ENV PYTHONPATH /usr/local/python/
WORKDIR /
ENTRYPOINT ["python","/usr/local/bin/wflow_sbm.py","-C","/data"]