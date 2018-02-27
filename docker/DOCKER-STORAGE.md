# Docker Storage

# Table of Contents

- [**Manage data in Docker**](#manage-data-in-docker)
  - [Choose the right type of mount](#choose-the-right-type-of-mount-link)
  - [Good use cases](#good-use-cases)
- [**Volumes**](#volumes-link)
- [**Bind Mounts**](#bind-mounts-link)
- [**tmpfs Mounts**](#tmpfs-mounts-link)
- [**Troubleshoot volume errors**](#troubleshoot-volume-errors-link)
- [**Store data within containers**](#store-data-within-containers-link)
- [**Docker storage drivers**](#docker-storage-drivers-link)
  - [Use the AUFS storage driver](#use-the-aufs-storage-driver-link)
  - [Use the BTRFS storage driver](#use-the-btrfs-storage-driver-link)
  - [Use the Device Mapper storage driver](#use-the-device-mapper-storage-driver-link)
  - [Use the OverlayFS storage driver](#use-the-overlayfs-storage-driver-link)
  - [Use the ZFS storage driver](#use-the-zfs-storage-driver-link)
  - [Use the VFS storage driver](#use-the-vfs-storage-driver-link)

# Manage data in Docker

[link](https://docs.docker.com/storage/)

It is possible to store data within the writable layer of a container, but there are some downsides:

* The data doesn’t persist when that container is no longer running,
  and it can be difficult to get the data out of the container if another process needs it.
* A container’s writable layer is tightly coupled to the host machine where the container is running.
  You can’t easily move the data somewhere else.
* Writing into a container’s writable layer requires a storage driver to manage the filesystem.
  The storage driver provides a union filesystem, using the Linux kernel.
  This extra abstraction reduces performance as compared to using data volumes, which write directly to the host filesystem.

[_Back to TOC_](#table-of-contents)

## Choose the right type of mount [link](https://docs.docker.com/storage/#choose-the-right-type-of-mount)

* **Volumes** are stored in a part of the host filesystem which is managed by Docker (/var/lib/docker/volumes/ on Linux).
  > Non-Docker processes should not modify this part of the filesystem. Volumes are the best way to persist data in Docker.
* **Bind mounts** may be stored anywhere on the host system. They may even be important system files or directories.
  > Non-Docker processes on the Docker host or a Docker container can modify them at any time.
* **tmpfs mounts** are stored in the host system’s memory only, and are never written to the host system’s filesystem.

![types-of-mounts](https://raw.githubusercontent.com/quanpan302/phd/master/docker/assets/img/docker-storage/types-of-mounts.png)

[_Back to TOC_](#table-of-contents)

## Good use cases

[_Back to TOC_](#table-of-contents)

### volumes
  
Volumes are the preferred way to **persist data in Docker containers and services**.
Some use cases for volumes include:

* **Sharing data among multiple running containers.**
  If you don’t explicitly create it, a volume is created the first time it is mounted into a container.
  When that container stops or is removed, the volume still exists.
  Multiple containers can mount the same volume simultaneously, either read-write or read-only.
  Volumes are only removed when you explicitly remove them.
* When the Docker host is not guaranteed to have a given directory or file structure.
  **Volumes help you decouple the configuration of the Docker host from the container runtime.**
* When you want to **store your container’s data on a remote host or a cloud provider, rather than locally**.
* When you need to **back up, restore, or migrate data from one Docker host to another**, volumes are a better choice.
  You can stop containers using the volume, then back up the volume’s directory (such as `/var/lib/docker/volumes/<volume-name>`).

[_Back to TOC_](#table-of-contents)

### bind mounts

In general, you should **use volumes where possible**.
Bind mounts are appropriate for the following types of use case:

* **Sharing configuration files from the host machine to containers.**
  This is how Docker provides DNS resolution to containers by default, by mounting `/etc/resolv.conf` from the host machine into each container.
* **Sharing source code or build artifacts between a development environment on the Docker host and a container.**
  For instance, you may mount a Maven target/ directory into a container,
  and each time you build the Maven project on the Docker host,
  the container gets access to the rebuilt artifacts.
  
    > If you use Docker for development this way, your production Dockerfile would copy the production-ready artifacts directly into the image, rather than relying on a bind mount.
  
* When the file or directory structure of the Docker host is guaranteed to be **consistent** with the bind mounts the containers require.

[_Back to TOC_](#table-of-contents)

### tmpfs mounts

`tmpfs` mounts are best used for cases when you do not want the data to persist either on the host machine or within the container.
This may be for security reasons or to protect the performance of the container when your application needs to write a large volume of non-persistent state data.

[_Back to TOC_](#table-of-contents)

### Tips for using bind mounts or volumes

* **If you mount an empty volume** into a directory in the container in which files or directories exist,
  these files or directories are propagated (copied) into the volume.
* Similarly, **if you start a container and specify a volume which does not already exist**,
  an empty volume is created for you.
  This is a good way to pre-populate data that another container needs.
* **If you mount a bind mount or non-empty volume** into a directory in the container in which some files or directories exist,
  these files or directories are obscured by the mount,
  just as if you saved files into `/mnt` on a Linux host and then mounted a **USB drive** into `/mnt`.
  
    The contents of `/mnt` would be obscured by the contents of the USB drive until the USB drive were unmounted.
    The obscured files are not removed or altered, but are not accessible while the bind mount or volume is mounted.

[_Back to TOC_](#table-of-contents)

# Volumes [link](https://docs.docker.com/storage/volumes/)

[_Back to TOC_](#table-of-contents)

# Bind Mounts [link](https://docs.docker.com/storage/bind-mounts/)

[_Back to TOC_](#table-of-contents)

# tmpfs Mounts [link](https://docs.docker.com/storage/tmpfs/)

[_Back to TOC_](#table-of-contents)

# Troubleshoot volume errors [link](https://docs.docker.com/storage/troubleshooting_volume_errors/)

[_Back to TOC_](#table-of-contents)

# Store data within containers [link](https://docs.docker.com/storage/storagedriver/)

[_Back to TOC_](#table-of-contents)

## Docker storage drivers [link](https://docs.docker.com/storage/storagedriver/select-storage-driver/)

[_Back to TOC_](#table-of-contents)

## Use the AUFS storage driver [link](https://docs.docker.com/storage/storagedriver/aufs-driver/)

[_Back to TOC_](#table-of-contents)

## Use the BTRFS storage driver [link](https://docs.docker.com/storage/storagedriver/btrfs-driver/)

[_Back to TOC_](#table-of-contents)

## Use the Device Mapper storage driver [link](https://docs.docker.com/storage/storagedriver/device-mapper-driver/)

[_Back to TOC_](#table-of-contents)

## Use the OverlayFS storage driver [link](https://docs.docker.com/storage/storagedriver/overlayfs-driver/)

[_Back to TOC_](#table-of-contents)

## Use the ZFS storage driver [link](https://docs.docker.com/storage/storagedriver/zfs-driver/)

[_Back to TOC_](#table-of-contents)

## Use the VFS storage driver [link](https://docs.docker.com/storage/storagedriver/vfs-driver/)

[_Back to TOC_](#table-of-contents)
