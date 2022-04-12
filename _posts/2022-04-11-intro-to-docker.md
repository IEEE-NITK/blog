---
 layout: post
 title: "Intro to Docker"
 author_github: pranavsubrahmanya
 date: 2022-04-11 00:00:00
 image: '/assets/img/'
 description: ''
 tags:
 - IEEE NITK
 - CompSoc
 - Docker
 categories:
 - Compsoc
 github_username: 'pranavsubrahmanya'
---
 
# What is Docker?

Docker is one of the most popular tools for application containerization. Docker enables efficiency and reduces operational overheads so that any developer, in any dev environment, can build stable and reliable applications.

The process of developing and managing applications in a company typically includes one or more teams. There's a development team that creates the software, and an operations team responsible for the deployment of these applications. The operations team is also responsible for the management of the application hosting infrastructure.

Several environments host applications during the app's development and publish process. First, the development team develops and tests the software in a development environment. Finally it needs to be deployed on the client end too. 
In this process of deploying applications across various environments, we come acroos many challenges :

* The different environments all require both software and hardware management. We have to ensure that both the installed software and configured hardware in each is the same. 

* If various versions of the applications are being built, the deployment of these versions should take place smoothly without disturbing the existing version and its usage. 

* We need to be able to run the deployed application in isolated environments as various environments have various other applications running, this should not affect the results in the deployed application.

**Docker is a Linux-based, open-source containerization platform that developers use to build, run, and package applications for deployment using containers.**

Docker containers modularize an application’s functionality into multiple components that allow deploying, testing, or scaling them independently when needed.

## Docker architecture
Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the building, running, and distributing Docker containers. The Docker client and daemon can run on the same system, or we can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface. 
Docker client in another docker client using ehich we can work with docker containers.

![docker-architecture](/blog/assets/img/Intro-to-Docker/docker-architecture.png)


* **Docker Daemon** : It is a persistent background process that manages Docker images, containers, networks, and storage volumes. The Docker daemon constantly listens for Docker API requests and processes them.

* **Docker Client** : The Docker client enables users to interact with Docker. The Docker client can reside on the same host as the daemon or connect to a daemon on a remote host. A docker client can communicate with more than one daemon. The Docker client provides a command line interface (CLI) that allows us to issue build, run, and stop application commands to a Docker daemon.

Common commands issued by a client are:

```bash

docker build
docker pull
docker run

```

* **Docker registries** : Docker registry stores Docker images. Docker Hub is a public registry, Docker by default looks for images on Docker hub. We can have private registries too. 

* **Docker Images** : Image is a template containing instructions for creating a Docker container. It can also be called the skeleton of the conatiner which is built upon it. Users can create own Docker images by using **Dockerfile**. Each instruction in a Dockerfile creates a layer in the image. 

* **Containers** : A container is a runnable instance of an image. We can create, start, stop, move, or delete a container using the Docker API or CLI.A container is relatively well isolated from other containers and its host machine.When a container is removed, any changes to its state that are not stored in persistent storage disappear.

![docker-architecture](/blog/assets/img/Intro-to-Docker/Docker-image-build.png)


### Conlcusion:
In this blog I have tried to explain the basics of Docker, its architecture and uses. Hope it is conveyed well to the readers. For further resources and learning, you can look into the links below. 

## Resources

[Docker-documentation](https://docs.docker.com/)
[What-is-docker?](https://docs.microsoft.com/en-us/learn/modules/intro-to-docker-containers/2-what-is-docker)
[Docker-architecture](https://www.aquasec.com/cloud-native-academy/docker-container/docker-architecture/)
