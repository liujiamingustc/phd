Docker Hub, Docker Cloud, Dockerfile, Docker Compose, Docker Swarm.

# Table of Contents

- [**Docker Documentation**](https://docs.docker.com)
  - [Docker Guides](https://docs.docker.com)
  - [Docker Product and tool manuals](https://docs.docker.com/manuals/)
  - [Docker glossary](https://docs.docker.com/glossary/)
  - [Docker Reference documentation](https://docs.docker.com/reference/)
  - [Docker Samples](https://docs.docker.com/samples/)
  - [**Docker Overview**](DOCKER-OVERVIEW.md)
    - [Dockerfile](DOCKER-DOCKERFILE.md)
    - [Compose file](DOCKER-COMPOSE.md)
  - [**Docker Storage**](DOCKER-STORAGE.md)
  - [**Cheat Sheet**](DOCKER-CHEAT_SHEET.md)
- [**datascience**](./datascience)
- [**microservices**](./microservices)
  - [blockchain](./microservices/blockchain)
  - [caffe](./microservices/caffe)
  - [cfd](./microservices/cfd)
  - [docker](./microservices/docker)
  - [gcc](./microservices/gcc)
  - [geodocker](./microservices/geodocker)
  - [geonode](./microservices/geonode)
  - [geoserver](./microservices/geoserver)
  - [hadoop](./microservices/hadoop)
  - [hpc](./microservices/hpc)
  - [influxdata](./microservices/influxdata)
  - [jupyter](./microservices/jupyter)
  - [kafka](./microservices/kafka)
  - [keras](./microservices/keras)
  - [kubernetes](./microservices/kubernetes)
  - [mapserver](./microservices/mapserver)
  - [mean](./microservices/mean)
  - [mongodb](./microservices/mongodb)
  - [nodejs](./microservices/nodejs)
  - [nvidia](./microservices/nvidia)
  - [opencv](./microservices/opencv)
  - [openshift](./microservices/openshift)
  - [postgis](./microservices/postgis)
  - [redis](./microservices/redis)
  - [scada](./microservices/scada)
  - [spark](./microservices/spark)
  - [tensorflow](./microservices/tensorflow)
  - [ubuntu](./microservices/ubuntu)
- [**ontology**](./ontology)
  - [00-xmlns](./ontology/00-xmlns)
  - [DBpedia](./ontology/DBpedia)
  - [NASA](./ontology/NASA)
  - [socio](./ontology/socio)
  - [water](./ontology/water)
- [**optimization**](./optimization)
  - [pyOpt](./optimization/pyOpt)
- [**server**](./server)
  - [laradock](./server/laradock)
- [**sociotechnical**](./sociotechnical)
  - [mesa](./sociotechnical/mesa)
  - [netlogo](./sociotechnical/netlogo)
- [**surrogate**](./surrogate)
- [**water**](./water)
  - [delft3d](./water/delft3d)
  - [xbeach](./water/xbeach)
  - [epanet](./water/epanet)
  - [sph](./water/sph)
  - [swmm](./water/swmm)

[_Back to TOC_](#table-of-contents)

# Node.js

```
$ docker pull node:8-alpine

$ docker run -it --rm --name myNodeApp node:8-alpine
>
> .help
```

```
$ cd /Users/quanpan/Documents

$ docker run -it --rm --name myNodeApp -v "$PWD":/usr/src/app -w /usr/src/app node:8-alpine node test.js
```

```
$ cd ~

$ docker run -it --rm --name myNodeApp -v /Users/quanpan/Documents:/usr/src/app -w /usr/src/app node:8-alpine node test.js
```

## Best Practice Docker and Node.js

### Docker Run

Here is an example of how you would run a default Node.JS Docker Containerized application:

```
$ docker run \
  -e "NODE_ENV=production" \
  -u "node" \
  -m "300M" --memory-swap "1G" \
  -w "/home/node/app" \
  --name "my-nodejs-app" \
  node [script]
```

## Best Practice Links

* [Dockerizing a Node.js web app](https://nodejs.org/en/docs/guides/nodejs-docker-webapp/)
* [Official Node.js Docker Image](https://registry.hub.docker.com/_/node/)
* [Node.js Docker Best Practices Guide](https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md)
* [Official Docker documentation](https://docs.docker.com/)
* [Docker Tag on StackOverflow](https://stackoverflow.com/questions/tagged/docker)
* [Docker Subreddit](https://reddit.com/r/docker)
