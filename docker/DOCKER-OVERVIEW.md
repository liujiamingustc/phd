# Docker

# Table of Contents

- [**Docker Overview**](#docker-overview)
  - [Docker Engine](#docker-engine)
  - [Docker Architecture](#docker-architecture)
- [**The Underlying Technology**](#the-underlying-technology)
  - [Namespaces](#namespaces)

# Docker Overview

[_Back to TOC_](#table-of-contents)

## Docker Engine

Docker Engine is a client-server application with these major components:

* A server which is a type of long-running program called a daemon process (the dockerd command).
* A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.
* A command line interface (CLI) client (the docker command).

![engine-components-flow](https://raw.githubusercontent.com/quanpan302/phd/master/docker/engine-components-flow.png)

[_Back to TOC_](#table-of-contents)

## Docker Architecture

Docker uses a client-server architecture.

The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers.

The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon.

The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface.

<img src="https://raw.githubusercontent.com/quanpan302/phd/master/docker/architecture.svg?sanitize=true">

[_Back to TOC_](#table-of-contents)

# The Underlying Technology

Docker is written in `Go` and takes advantage of several features of the Linux kernel to deliver its functionality.

[_Back to TOC_](#table-of-contents)

## Namespaces

Docker uses a technology called namespaces to provide the isolated workspace called the container.
When you run a container, Docker creates a set of namespaces for that container.

Docker Engine uses namespaces such as the following on Linux:

* **The `pid` namespace**: Process isolation (PID: Process ID).
* **The `net` namespace**: Managing network interfaces (NET: Networking).
* **The `ipc` namespace**: Managing access to IPC resources (IPC: InterProcess Communication).
* **The `mnt` namespace**: Managing filesystem mount points (MNT: Mount).
* **The `uts` namespace**: Isolating kernel and version identifiers. (UTS: Unix Timesharing System).

[_Back to TOC_](#table-of-contents)
