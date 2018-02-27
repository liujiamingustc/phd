# Docker

Dockerfile, Docker Hub, Source Codes.

# Table of Contents

- [**Dockerfile Reference**](#dockerfile-reference-link)
  - [FROM](#from-dockerfile-reference)
  - [RUN](#run-dockerfile-reference)
  - [CMD](#cmd-dockerfile-reference)
  - [LABEL](#label-dockerfile-reference)
  - [EXPOSE](#expose-dockerfile-reference)
  - [ENV](#env-dockerfile-reference)
  - [ADD](#add-dockerfile-reference)
  - [COPY](#copy-dockerfile-reference)
  - [ENTRYPOINT](#entrypoint-dockerfile-reference)
  - [VOLUME](#volume-dockerfile-reference)
  - [USER](#user-dockerfile-reference)
  - [WORKDIR](#workdir-dockerfile-reference)
  - [ARG](#arg-dockerfile-reference)
  - [ONBUILD](#onbuild-dockerfile-reference)
  - [STOPSIGNAL](#stopsignal-dockerfile-reference)
  - [HEALTHCHECK](#healthcheck-dockerfile-reference)
  - [SHELL](#shell-dockerfile-reference)
- [**Compose file version 3 reference**](#compose-file-version-3-reference-link)
  - [Service configuration reference](#service-configuration-reference-link)
    - [build](#build-link)
    - [cap\_add, cap\_drop](#cap_add-cap_drop-link)
    - [command](#command-link)
    - [configs](#configs-link)
    - [cgroup\_parent](#cgroup_parent-link)
    - [container\_name](#container_name-link)
    - [credential\_spec](#credential_spec-link)
    - [deploy](#deploy-link)
    - [devices](#devices-link)
    - [depends\_on](#depends_on-link)
    - [dns](#dns-link)
    - [dns\_search](#dns_search-link)
    - [tmpfs](#tmpfs-link)
    - [entrypoint](#entrypoint-link)
    - [env\_file](#env_file-link)
    - [environment](#environment-link)
    - [expose](#expose-link)
    - [external\_links](#external_links-link)
    - [extra\_hosts](#extra_hosts-link)
    - [healthcheck](#healthcheck-link)
    - [image](#image-link)
    - [isolation](#isolation-link)
    - [labels](#labels-link)
    - [links](#links-link)
    - [logging](#logging-link)
    - [network\_mode](#network_mode-link)
    - [networks](#networks-link)
    - [pid](#pid-link)
    - [ports](#ports-link)
    - [secrets](#secrets-link)
    - [security\_opt](#security_opt-link)
    - [stop\_grace\_period](#stop_grace_period-link)
    - [stop\_signal](#stop_signal-link)
    - [sysctls](#sysctls-link)
    - [ulimits](#ulimits-link)
    - [userns\_mode](#userns_mode-link)
    - [volumes](#volumes-link)
    - [restart](#restart-link)
  - [Specifying durations](#specifying-durations-link)
  - [Specifying byte values](#specifying-byte-values-link)
  - [Volume configuration reference](#volume-configuration-reference-link)
  - [Network configuration reference](#network-configuration-reference-link)
  - [configs configuration reference](#configs-configuration-reference-link)
  - [secrets configuration reference](#secrets-configuration-reference-link)
  - [Variable substitution](#variable-substitution-link)
  - [Extension fields](#extension-fields-link)
- [**Recap and cheat sheet**](#recap-and-cheat-sheet)
  - [Containers](#containers)
  - [Services](#services)
  - [Swarms](#swarms)
  - [Stacks](#stacks)

# Dockerfile Reference [link](https://docs.docker.com/engine/reference/builder/)

These recommendations help you to write an efficient and maintainable `Dockerfile`.

[_Back to TOC_](#table-of-contents)

## FROM [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#from)
   
   `FROM <image> [AS <name>]`
   
   `FROM <image>[:<tag>] [AS <name>]`
   
   `FROM <image>[@<digest>] [AS <name>]`
   
[_Back to TOC_](#table-of-contents)

## RUN [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#run)
   
   `RUN <command>` _(shell form, the command is run in a shell, which by default is `/bin/sh -c` on Linux_ or _`cmd /S /C` on Windows)_
   
   `RUN ["executable", "param1", "param2"]` _(exec form)_
   
[_Back to TOC_](#table-of-contents)

## CMD [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#cmd)
   
   `CMD ["executable","param1","param2"]` _(exec form, this is the preferred form)_
   
   `CMD ["param1","param2"]` _(as default parameters to ENTRYPOINT)_
   
   `CMD command param1 param2` _(shell form)_
   
[_Back to TOC_](#table-of-contents)

## LABEL [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#label)
   
   `LABEL <key>=<value> <key>=<value> <key>=<value> ...`
   
   ```
   LABEL "com.example.vendor"="ACME Incorporated"
   LABEL com.example.label-with-value="foo"
   LABEL version="1.0"
   LABEL description="This text illustrates \
   that label-values can span multiple lines."
   ```
   
[_Back to TOC_](#table-of-contents)

## EXPOSE [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#expose)
   
   `EXPOSE <port> [<port>/<protocol>...]`
   
[_Back to TOC_](#table-of-contents)

## ENV [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#env)
   
   ```
   ENV <key> <value>
   ENV <key>=<value> ...
   ```
   
[_Back to TOC_](#table-of-contents)

## ADD [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#add)
   
   * `ADD [--chown=<user>:<group>] <src>... <dest>`
   * `ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]` _(this form is required for paths containing whitespace)_
   
[_Back to TOC_](#table-of-contents)

## COPY [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#copy)
   
   * `COPY [--chown=<user>:<group>] <src>... <dest>`
   * `COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]` _(this form is required for paths containing whitespace)_
   
[_Back to TOC_](#table-of-contents)

## ENTRYPOINT [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#entrypoint)
   
   * `ENTRYPOINT ["executable", "param1", "param2"]` _(exec form, preferred)_
   * `ENTRYPOINT command param1 param2` _(shell form)_
   
   |                              | No ENTRYPOINT                | ENTRYPOINT exec\_entry p1\_entry | ENTRYPOINT [“exec\_entry”, “p1\_entry”]            |
   |------------------------------|------------------------------|----------------------------------|----------------------------------------------------|
   | No CMD                       | error, not allowed           | /bin/sh -c exec\_entry p1\_entry | exec\_entry p1\_entry                              |
   | CMD [“exec\_cmd”, “p1\_cmd”] | exec\_cmd p1\_cmd            | /bin/sh -c exec\_entry p1\_entry | exec\_entry p1\_entry exec\_cmd p1\_cmd            |
   | CMD [“p1\_cmd”, “p2\_cmd”]   | p1\_cmd p2\_cmd              | /bin/sh -c exec\_entry p1\_entry | exec\_entry p1\_entry p1\_cmd p2\_cmd              |
   | CMD exec\_cmd p1\_cmd        | /bin/sh -c exec\_cmd p1\_cmd | /bin/sh -c exec\_entry p1\_entry | exec\_entry p1\_entry /bin/sh -c exec\_cmd p1\_cmd |
   
[_Back to TOC_](#table-of-contents)

## VOLUME [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#volume)
   
   `VOLUME ["/data"]`
   
   For more information/examples and mounting instructions via the Docker client,
   refer to [Share Directories via Volumes](https://docs.docker.com/storage/volumes/) documentation.
   
[_Back to TOC_](#table-of-contents)

## USER [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#user)
   
   ```
   USER <user>[:<group>]
   USER <UID>[:<GID>]
   ```
   
[_Back to TOC_](#table-of-contents)

## WORKDIR [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#workdir)
   
   `WORKDIR /path/to/workdir`
   
   The `WORKDIR` instruction can resolve environment variables previously set using `ENV`.
   You can only use environment variables explicitly set in the `Dockerfile`. 
   
   ```
   ENV DIRPATH /path
   WORKDIR $DIRPATH/$DIRNAME
   RUN pwd
   ```
   
   The output of the final `pwd` command in this `Dockerfile` would be `/path/$DIRNAME`
   
[_Back to TOC_](#table-of-contents)

## ARG [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#arg)
   
   `ARG <name>[=<default value>]`
   
   **Using ARG variables**
   
   _constant\_image\_version_
   
   ```
   FROM ubuntu
   ARG CONT_IMG_VER
   ENV CONT_IMG_VER ${CONT_IMG_VER:-v1.0.0}
   RUN echo $CONT_IMG_VER
   ```
   
   **--build-arg \<varname\>=\<value\>**
   
   `docker build --build-arg CONT_IMG_VER=v2.0.1 .`
   
   **Predefined ARGs**
   
   * `HTTP_PROXY`
   * `http_proxy`
   * `HTTPS_PROXY`
   * `https_proxy`
   * `FTP_PROXY`
   * `ftp_proxy`
   * `NO_PROXY`
   * `no_proxy`
   
[_Back to TOC_](#table-of-contents)

## ONBUILD [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#onbuild)
   
   `ONBUILD [INSTRUCTION]`
   
[_Back to TOC_](#table-of-contents)

## STOPSIGNAL [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#stopsignal)
   
   `STOPSIGNAL signal`
   
[_Back to TOC_](#table-of-contents)

## HEALTHCHECK [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#healthcheck)
   
   * `HEALTHCHECK [OPTIONS] CMD command` _(check container health by running a command inside the container)_
   * `HEALTHCHECK NONE` _(disable any healthcheck inherited from the base image)_
   
   The options that can appear before CMD are:
   
   * `--interval=DURATION` (default: `30s`)
   * `--timeout=DURATION` (default: `30s`)
   * `--start-period=DURATION` (default: `0s`)
   * `--retries=N` (default: `3`)
   
   ```
   HEALTHCHECK --interval=5m --timeout=3s \
     CMD curl -f http://localhost/ || exit 1
   ```
     
[_Back to TOC_](#table-of-contents)

## SHELL [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#shell)
   
   `SHELL ["executable", "parameters"]`
   
   The default shell
   
   * on Linux is `["/bin/sh", "-c"]`
   * on Windows is `["cmd", "/S", "/C"]`

[_Back to TOC_](#table-of-contents)

# Compose file version 3 reference [link](https://docs.docker.com/compose/compose-file/)

| Compose file format | Docker Engine release |
|---------------------|-----------------------|
| 3.6                 | 18.02.0+              |
| 3.5                 | 17.12.0+              |
| 3.4                 | 17.09.0+              |
| 3.3                 | 17.06.0+              |
| 3.2                 | 17.04.0+              |
| 3.1                 | 1.13.1+               |
| 3.0                 | 1.13.0+               |
| 2.3                 | 17.06.0+              |
| 2.2                 | 1.13.0+               |
| 2.1                 | 1.12.0+               |
| 2.0                 | 1.10.0+               |
| 1.0                 | 1.9.1.+               |

[_Back to TOC_](#table-of-contents)

## Service configuration reference [link](https://docs.docker.com/compose/compose-file/#service-configuration-reference)

### build [link](https://docs.docker.com/compose/compose-file/#build)

Configuration options that are applied at build time.

build can be specified either as a string containing a path to the build context:

```
version: '3'
services:
  webapp:
    build: ./dir
```

Or, as an object with the path specified under `context` and optionally `Dockerfile` and `args`:

```
version: '3'
services:
  webapp:
    build:
      context: ./dir
      dockerfile: Dockerfile-alternate
      args:
        buildno: 1
```

* [CONTEXT](https://docs.docker.com/compose/compose-file/#context)
* [DOCKERFILE](https://docs.docker.com/compose/compose-file/#dockerfile)
* [ARGS](https://docs.docker.com/compose/compose-file/#args)
* [CACHE_FROM](https://docs.docker.com/compose/compose-file/#cache_from)
* [LABELS](https://docs.docker.com/compose/compose-file/#labels)
* [SHM_SIZE](https://docs.docker.com/compose/compose-file/#shm_size)

[_Back to TOC_](#table-of-contents)

### cap\_add, cap\_drop [link](https://docs.docker.com/compose/compose-file/#cap_add-cap_drop)

Add or drop container capabilities. See `man 7 capabilities` for a full list.

```
cap_add:
  - ALL

cap_drop:
  - NET_ADMIN
  - SYS_ADMIN
```

[_Back to TOC_](#table-of-contents)

### command [link](https://docs.docker.com/compose/compose-file/#command)

Override the default command.

```
command: bundle exec thin -p 3000
```

The command can also be a list, in a manner similar to dockerfile:

```
command: ["bundle", "exec", "thin", "-p", "3000"]
```

[_Back to TOC_](#table-of-contents)

### configs [link](https://docs.docker.com/compose/compose-file/#configs)

Grant access to configs on a per-service basis using the per-service `configs` configuration.

Two different syntax variants are supported.

* [SHORT SYNTAX](https://docs.docker.com/compose/compose-file/#short-syntax)
* [LONG SYNTAX](https://docs.docker.com/compose/compose-file/#long-syntax)

[_Back to TOC_](#table-of-contents)

### cgroup\_parent [link](https://docs.docker.com/compose/compose-file/#cgroup_parent)

Specify an optional parent cgroup for the container.

```
cgroup_parent: m-executor-abcd
```

[_Back to TOC_](#table-of-contents)

### container\_name [link](https://docs.docker.com/compose/compose-file/#container_name)

Specify a custom container name, rather than a generated default name.

```
container_name: my-web-container
```

[_Back to TOC_](#table-of-contents)

### credential\_spec [link](https://docs.docker.com/compose/compose-file/#credential_spec)

Configure the credential spec for managed service account.

This option is only used for services using Windows containers.
The `credential_spec` must be in the format `file://<filename>` or `registry://<value-name>`.

```
credential_spec:
  file: my-credential-spec.json
```

[_Back to TOC_](#table-of-contents)

### deploy [link](https://docs.docker.com/compose/compose-file/#deploy)

Specify configuration related to the deployment and running of services.

This only takes effect when deploying to a `swarm` with `docker stack deploy`,
and is ignored by `docker-compose up` and `docker-compose run`.

```
version: '3'
services:
  redis:
    image: redis:alpine
    deploy:
      replicas: 6
      update_config:
        parallelism: 2
        delay: 10s
      restart_policy:
        condition: on-failure
```

[_Back to TOC_](#table-of-contents)

### devices [link](https://docs.docker.com/compose/compose-file/#devices)

List of device mappings. Uses the same format as the `--device` docker client create option.

```
devices:
  - "/dev/ttyUSB0:/dev/ttyUSB0"
```

[_Back to TOC_](#table-of-contents)

### depends\_on [link](https://docs.docker.com/compose/compose-file/#depends_on)

Express dependency between services, Service dependencies cause the following behaviors:

* `docker-compose up` starts services in dependency order. In the following example, `db` and redis are started before `web`.
* `docker-compose up SERVICE` automatically includes `SERVICE`’s dependencies.
  In the following example, `docker-compose up web` also creates and starts `db` and `redis`.

```
version: '3'
services:
  web:
    build: .
    depends_on:
      - db
      - redis
  redis:
    image: redis
  db:
    image: postgres
```

[_Back to TOC_](#table-of-contents)

### dns [link](https://docs.docker.com/compose/compose-file/#dns)

Custom DNS servers. Can be a single value or a list.

```
dns: 8.8.8.8
dns:
  - 8.8.8.8
  - 9.9.9.9
```

[_Back to TOC_](#table-of-contents)

### dns_search [link](https://docs.docker.com/compose/compose-file/#dns_search)

Custom DNS search domains. Can be a single value or a list.

```
dns_search: example.com
dns_search:
  - dc1.example.com
  - dc2.example.com
```

[_Back to TOC_](#table-of-contents)

### tmpfs [link](https://docs.docker.com/compose/compose-file/#tmpfs)

Mount a temporary file system inside the container. Can be a single value or a list.

**Version 3.6 file format and up.**

```
 - type: tmpfs
     target: /app
     tmpfs:
       size: 1000
```

[_Back to TOC_](#table-of-contents)

### entrypoint [link](https://docs.docker.com/compose/compose-file/#entrypoint)

Override the default entrypoint.

```
entrypoint: /code/entrypoint.sh
```

The entrypoint can also be a list, in a manner similar to dockerfile:

```
entrypoint:
    - php
    - -d
    - zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20100525/xdebug.so
    - -d
    - memory_limit=-1
    - vendor/bin/phpunit
```

[_Back to TOC_](#table-of-contents)

### env\_file [link](https://docs.docker.com/compose/compose-file/#env_file)

Add environment variables from a file. Can be a single value or a list.

```
env_file: .env

env_file:
  - ./common.env
  - ./apps/web.env
  - /opt/secrets.env
```

[_Back to TOC_](#table-of-contents)

### environment [link](https://docs.docker.com/compose/compose-file/#environment)

Add environment variables. You can use either an array or a dictionary.

Any boolean values; true, false, yes no, need to be enclosed in quotes to ensure they are not converted to True or False by the YML parser.

```
environment:
  RACK_ENV: development
  SHOW: 'true'
  SESSION_SECRET:

environment:
  - RACK_ENV=development
  - SHOW=true
  - SESSION_SECRET
```

[_Back to TOC_](#table-of-contents)

### expose [link](https://docs.docker.com/compose/compose-file/#expose)

Expose ports without publishing them to the host machine - they’ll only be accessible to linked services.

Only the internal port can be specified.

```
expose:
 - "3000"
 - "8000"
```

[_Back to TOC_](#table-of-contents)

### external\_links [link](https://docs.docker.com/compose/compose-file/#external_links)

Link to containers started outside this `docker-compose.yml` or even outside of Compose, especially for containers that provide shared or common services.

`external_links` follow semantics similar to the legacy option `links` when specifying both the container name and the link alias (`CONTAINER:ALIAS`).

```
external_links:
 - redis_1
 - project_db_1:mysql
 - project_db_1:postgresql
```

[_Back to TOC_](#table-of-contents)

### extra\_hosts [link](https://docs.docker.com/compose/compose-file/#extra_hosts)

Add hostname mappings. Use the same values as the docker client `--add-host` parameter.

```
extra_hosts:
 - "somehost:162.242.195.82"
 - "otherhost:50.31.209.229"
```

[_Back to TOC_](#table-of-contents)

### healthcheck [link](https://docs.docker.com/compose/compose-file/#healthcheck)

Configure a check that’s run to determine whether or not containers for this service are “healthy”.

See the docs for the `HEALTHCHECK Dockerfile instruction` for details on how healthchecks work.

```
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost"]
  interval: 1m30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

[_Back to TOC_](#table-of-contents)

### image [link](https://docs.docker.com/compose/compose-file/#image)

Specify the image to start the container from. Can either be a repository/tag or a partial image ID.

```
image: redis
image: ubuntu:14.04
image: tutum/influxdb
image: example-registry.com:4000/postgresql
image: a4bc65fd
```

[_Back to TOC_](#table-of-contents)

### isolation [link](https://docs.docker.com/compose/compose-file/#isolation)

Specify a container’s isolation technology.

* On Linux, the only supported value is default.
* On Windows, acceptable values are `default`, `process` and `hyperv`.

Refer to the Docker Engine docs for details.

[_Back to TOC_](#table-of-contents)

### labels [link](https://docs.docker.com/compose/compose-file/#labels-2)

Add metadata to containers using Docker labels. You can use either an array or a dictionary.

```
labels:
  com.example.description: "Accounting webapp"
  com.example.department: "Finance"
  com.example.label-with-empty-value: ""

labels:
  - "com.example.description=Accounting webapp"
  - "com.example.department=Finance"
  - "com.example.label-with-empty-value"
```

[_Back to TOC_](#table-of-contents)

### links [link](https://docs.docker.com/compose/compose-file/#links)

[_Back to TOC_](#table-of-contents)

### logging [link](https://docs.docker.com/compose/compose-file/#logging)

Logging configuration for the service.

```
logging:
  driver: syslog
  options:
    syslog-address: "tcp://192.168.0.42:123"
```

[_Back to TOC_](#table-of-contents)

### network\_mode [link](https://docs.docker.com/compose/compose-file/#network_mode)

Network mode. Use the same values as the docker client `--net` parameter, plus the special form `service:[service name]`.

```
network_mode: "bridge"
network_mode: "host"
network_mode: "none"
network_mode: "service:[service name]"
network_mode: "container:[container name/id]"
```

[_Back to TOC_](#table-of-contents)

### networks [link](https://docs.docker.com/compose/compose-file/#networks)

Networks to join, referencing entries under the top-level `networks` key.

```
services:
  some-service:
    networks:
     - some-network
     - other-network
```

[_Back to TOC_](#table-of-contents)

### pid [link](https://docs.docker.com/compose/compose-file/#pid)

Sets the PID mode to the host PID mode.

This turns on sharing between container and the host operating system the PID address space.

Containers launched with this flag can access and manipulate other containers in the bare-metal machine’s namespace and vise-versa.

```
pid: "host"
```

[_Back to TOC_](#table-of-contents)

### ports [link](https://docs.docker.com/compose/compose-file/#ports)

Expose ports.

SHORT SYNTAX

```
ports:
 - "3000"
 - "3000-3005"
 - "8000:8000"
 - "9090-9091:8080-8081"
 - "49100:22"
 - "127.0.0.1:8001:8001"
 - "127.0.0.1:5000-5010:5000-5010"
 - "6060:6060/udp"
```

LONG SYNTAX

```
ports:
  - target: 80
    published: 8080
    protocol: tcp
    mode: host
```

[_Back to TOC_](#table-of-contents)

### secrets [link](https://docs.docker.com/compose/compose-file/#secrets)

Grant access to secrets on a per-service basis using the per-service secrets configuration.

Two different syntax variants are supported.

SHORT SYNTAX

```
version: "3.1"
services:
  redis:
    image: redis:latest
    deploy:
      replicas: 1
    secrets:
      - my_secret
      - my_other_secret
secrets:
  my_secret:
    file: ./my_secret.txt
  my_other_secret:
    external: true
```

LONG SYNTAX

```
version: "3.1"
services:
  redis:
    image: redis:latest
    deploy:
      replicas: 1
    secrets:
      - source: my_secret
        target: redis_secret
        uid: '103'
        gid: '103'
        mode: 0440
secrets:
  my_secret:
    file: ./my_secret.txt
  my_other_secret:
    external: true
```

[_Back to TOC_](#table-of-contents)

### security\_opt [link](https://docs.docker.com/compose/compose-file/#security_opt)

Override the default labeling scheme for each container.

```
security_opt:
  - label:user:USER
  - label:role:ROLE
```

[_Back to TOC_](#table-of-contents)

### stop\_grace\_period [link](https://docs.docker.com/compose/compose-file/#stop_grace_period)

Specify how long to wait when attempting to stop a container if it doesn’t handle SIGTERM (or whatever stop signal has been specified with stop_signal), before sending SIGKILL.

Specified as a duration.

```
stop_grace_period: 1s
stop_grace_period: 1m30s
```

[_Back to TOC_](#table-of-contents)

### stop\_signal [link](https://docs.docker.com/compose/compose-file/#stop_signal)

Sets an alternative signal to stop the container.
By default `stop` uses SIGTERM.

Setting an alternative signal using stop_signal causes stop to send that signal instead.

```
stop_signal: SIGUSR1
```

[_Back to TOC_](#table-of-contents)

### sysctls [link](https://docs.docker.com/compose/compose-file/#sysctls)

Kernel parameters to set in the container. You can use either an array or a dictionary.

```
sysctls:
  net.core.somaxconn: 1024
  net.ipv4.tcp_syncookies: 0

sysctls:
  - net.core.somaxconn=1024
  - net.ipv4.tcp_syncookies=0
```

[_Back to TOC_](#table-of-contents)

### ulimits [link](https://docs.docker.com/compose/compose-file/#ulimits)

Override the default ulimits for a container.

You can either specify a single limit as an integer or soft/hard limits as a mapping.

```
ulimits:
  nproc: 65535
  nofile:
    soft: 20000
    hard: 40000
```

[_Back to TOC_](#table-of-contents)

### userns\_mode [link](https://docs.docker.com/compose/compose-file/#userns_mode)

Disables the user namespace for this service, if Docker daemon is configured with user namespaces.

See dockerd for more information.

```
userns_mode: "host"
```

[_Back to TOC_](#table-of-contents)

### volumes [link](https://docs.docker.com/compose/compose-file/#volumes)

Mount host paths or named volumes, specified as sub-options to a service.

You can mount a host path as part of a definition for a single service, and there is no need to define it in the top level `volumes` key.

But, if you want to reuse a volume across multiple services, then define a named volume in the top-level volumes key. Use named volumes with services, swarms, and stack files.

```
version: "3.2"
services:
  web:
    image: nginx:alpine
    volumes:
      - type: volume
        source: mydata
        target: /data
        volume:
          nocopy: true
      - type: bind
        source: ./static
        target: /opt/app/static

  db:
    image: postgres:latest
    volumes:
      - "/var/run/postgres/postgres.sock:/var/run/postgres/postgres.sock"
      - "dbdata:/var/lib/postgresql/data"

volumes:
  mydata:
  dbdata:
```

[_Back to TOC_](#table-of-contents)

### restart [link](https://docs.docker.com/compose/compose-file/#restart)

`no` is the default restart policy, and it does not restart a container under any circumstance.

When `always` is specified, the container always restarts.

The `on-failure` policy restarts a container if the exit code indicates an on-failure error.

```
restart: "no"
restart: always
restart: on-failure
restart: unless-stopped
```

[_Back to TOC_](#table-of-contents)

## Specifying durations [link](https://docs.docker.com/compose/compose-file/#specifying-durations)

[_Back to TOC_](#table-of-contents)

## Specifying byte values [link](https://docs.docker.com/compose/compose-file/#specifying-byte-values)

[_Back to TOC_](#table-of-contents)

## Volume configuration reference [link](https://docs.docker.com/compose/compose-file/#volume-configuration-reference)

[_Back to TOC_](#table-of-contents)

## Network configuration reference [link](https://docs.docker.com/compose/compose-file/#network-configuration-reference)

[_Back to TOC_](#table-of-contents)

## configs configuration reference [link](https://docs.docker.com/compose/compose-file/#configs-configuration-reference)

[_Back to TOC_](#table-of-contents)

## secrets configuration reference [link](https://docs.docker.com/compose/compose-file/#secrets-configuration-reference)

[_Back to TOC_](#table-of-contents)

## Variable substitution [link](https://docs.docker.com/compose/compose-file/#variable-substitution)

[_Back to TOC_](#table-of-contents)

## Extension fields [link](https://docs.docker.com/compose/compose-file/#extension-fields)

[_Back to TOC_](#table-of-contents)

# Recap and cheat sheet

_Here are some commands you might like to run to interact with your swarm and your VMs a bit_

## [Containers](http://devdocs.io/docker~17/get-started/part2/index)

```
docker build -t friendlyhello .                    # Create image using this directory's Dockerfile
==============
docker run -p 4000:80 friendlyhello                # Run "friendlyhello" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello             # Same thing, but in detached mode
docker run username/repository:tag                 # Run image from a registry
==============
docker container ls                                # List all running containers
docker container ls -a                             # List all containers, even those not running
docker container ls -q                          # List container IDs
docker container stop <hash>                       # Gracefully stop the specified container
docker container kill <hash>                       # Force shutdown of the specified container
docker container rm <hash>                         # Remove specified container from this machine
docker container rm $(docker container ls -a -q)   # Remove all containers
==============
docker image ls -a                                 # List all images on this machine
docker image rm <image id>                         # Remove specified image from this machine
docker image rm $(docker image ls -a -q)           # Remove all images from this machine
==============
docker login                                       # Log in this CLI session using your Docker credentials
==============
docker tag <image> username/repository:tag         # Tag <image> for upload to registry
docker push username/repository:tag                # Upload tagged image to registry
```

[_Back to TOC_](#table-of-contents)

## [Services](http://devdocs.io/docker~17/get-started/part3/index)

```
docker stack ls                                 # List stacks or apps
docker stack deploy -c <composefile> <appname>  # Run the specified Compose file
docker stack rm <appname>                       # Tear down an application
==============
docker service ls                               # List running services associated with an app
docker service ps <service>                     # List tasks associated with an app
==============
docker inspect <task or container>              # Inspect task or container
```

[_Back to TOC_](#table-of-contents)

## [Swarms](https://docs.docker.com/get-started/part4/)

```
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1                  # Win10
& "C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1 | Invoke-Expression   # Windows command to connect shell to myvm1
==============
docker-machine create --driver virtualbox myvm1                                           # Create a VM myvm1 (Mac, Win7, Linux)
docker-machine create --driver virtualbox myvm2                                           # Create a VM myvm2 (Mac, Win7, Linux)
==============
docker-machine ls                                                                         # list VMs, asterisk shows which VM this shell is talking to
==============
docker-machine env myvm1                                                                  # View basic information about your node, show environment variables and command for myvm1
                                                                                          # myvm1 ACTIVE -
docker-machine ssh myvm1                                                                  # Open an SSH session with the VM; type "exit" to end
docker-machine ssh myvm1 "docker swarm init --advertise-addr <node manager ip> "          # Manager
docker-machine ssh myvm2 "docker swarm join --token <SWMTKN> <node manager ip>:<port>"    # Worker
docker-machine ssh myvm1 "docker node ls"                                                 # List the nodes in your swarm
docker-machine ssh myvm1 "docker node inspect <node ID>"                                  # Inspect a node
docker-machine ssh myvm1 "docker swarm join-token -q worker"                              # View join token
==============
eval $(docker-machine env myvm1)                                                          # Mac command to connect shell to myvm1
                                                                                          # myvm1 ACTIVE *
docker node ls                                                                            # View nodes in swarm (while logged on to manager)
==============
eval $(docker-machine env -u)                                                             # Disconnect shell from VMs, use native docker
==============
docker-machine ssh myvm2 "docker swarm leave"                                             # Make the worker leave the swarm
docker-machine ssh myvm1 "docker swarm leave -f"                                          # Make master leave, kill swarm
==============
docker-machine stop myvm1                                                                 # Stop a VM that is currently not running
docker-machine start myvm1                                                                # Start a VM that is currently not running
==============
docker-machine stop $(docker-machine ls -q)                                               # Stop all running VMs
docker-machine rm $(docker-machine ls -q)                                                 # Delete all VMs and their disk images
==============
docker stack deploy -c docker-compose.yml getstartedlab                                   # Deploy an app;
docker stack deploy -c <file> <app>                                                       # Deploy an app; command shell must be set to talk to manager (myvm1), uses local Compose file
docker stack ps <app>                                                                     # List
docker stack rm <app>                                                                     # Remove
docker-machine scp docker-compose.yml myvm1:~                                             # Copy file to node's home dir (only required if you use ssh to connect to manager and deploy the app)
docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"                            # Deploy an app using ssh (you must have first copied the Compose file to myvm1)
```

[_Back to TOC_](#table-of-contents)

## [Stacks](https://docs.docker.com/get-started/part5/)

[_Back to TOC_](#table-of-contents)
