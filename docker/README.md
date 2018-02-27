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

## Service configuration reference [link](https://docs.docker.com/compose/compose-file/#service-configuration-reference)

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
