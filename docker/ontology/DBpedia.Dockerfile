FROM aksw/dld-bootstrap

MAINTAINER Markus Ackermann <ackermann@informatik.uni-leipzig.de>

RUN dnf install -y findutils wget rasqal

COPY DBpedia/run.sh DBpedia/dbpedia-dld.yml DBpedia/download.sh /

RUN chmod +x /run.sh

VOLUME ["/dld-dbpedia-wd/models/"]

ENTRYPOINT ["/run.sh"]
