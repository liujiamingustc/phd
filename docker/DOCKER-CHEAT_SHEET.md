# Recap and cheat sheet

* Dockerfile Reference [link](https://docs.docker.com/engine/reference/builder/)
* Compose file version 3 reference [link](https://docs.docker.com/compose/compose-file/)

# Table of Contents

- [**Recap and cheat sheet**](#recap-and-cheat-sheet)
  - [Containers](#containers)
  - [Services](#services)
  - [Swarms](#swarms)
  - [Stacks](#stacks)

# Recap and cheat sheet

_Here are some commands you might like to run to interact with your swarm and your VMs a bit_

[_Back to TOC_](#table-of-contents)

## [Containers](http://devdocs.io/docker~17/get-started/part2/index)

```
docker build -t friendlyhello .                                                           # Create image using this directory's Dockerfile
==============
docker run -it <image> /bin/bash                                                          # Run interactive an interactive Bash session
docker run -v /host/dir:/container/dir -it <image> /bin/bash                              # Mount a volume
docker run -v /Users/quanpan/Documents/mac-Docker/data:/delft3d/examples/data -it quanpan302/phd:delft3d_v6686 /bin/bash
                                                                                          # Mount a volume for delft3d
docker run -p 4000:80 friendlyhello                                                       # Run "friendlyhello" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello                                                    # Same thing, but in detached mode
docker run username/repository:tag                                                        # Run image from a registry
==============
docker container ls                                                                       # List all running containers
docker container ls -a                                                                    # List all containers, even those not running
docker container ls -q                                                                    # List container IDs
docker container stop <hash>                                                              # Gracefully stop the specified container
docker container kill <hash>                                                              # Force shutdown of the specified container
docker container rm <hash>                                                                # Remove specified container from this machine
docker container rm $(docker container ls -a -q)                                          # Remove all containers
==============
docker image ls -a                                                                        # List all images on this machine
docker image rm <image id>                                                                # Remove specified image from this machine
docker image rm $(docker image ls -a -q)                                                  # Remove all images from this machine
==============
docker login                                                                              # Log in this CLI session using your Docker credentials
==============
docker tag <image> username/repository:tag                                                # Tag <image> for upload to registry
docker push username/repository:tag                                                       # Upload tagged image to registry
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
docker-machine ssh myvm1 "docker swarm join-token -q manager"                             # View manager join token
docker-machine ssh myvm1 "docker swarm join-token -q worker"                              # View worker join token
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
