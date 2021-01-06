---
 layout: post
 title: "Introduction to Kubernetes Architecture"
 author_github: sravanireddy1102
 date: 2020-12-30 13:52:30
 image: '/assets/img/'
 description: ''
 tags:
 - IEEE NITK
 - CompSoc
 - Kubernetes
 categories:
 - Compsoc
 github_username: 'sravanireddy1102'
 ---
This blog post will give you a basic idea of what Kubernetes is,its applications and infrastructure.

## **Containers**

As the era of microservices began,the use of containers has gained much popularity . We basically encapsulate each application with its dependencies and libraries as a **container image** which can be executable on any machine.We can spin up multiple applications on a single system without any environment conflicts. 

## **Motivation to read about Kubernetes**

So far everything is good with containers. One can use runtime softwares like Docker and deploy the application containers. 
However communication between containers become difficult if we are deploying hundred's of containers (it's a gigantic mess), and what if a container dies?
Container Orchestration tool comes into action to address the above problems.

## **Kubernetes as a container orchestration tool**

Kubernetes is  a platform designed to completely manage the life cycle of containerized applications and services using methods that provide predictability, scalability, and high availability.

Suppose if a container dies,Kubernetes API server notices it and deploys another container in place of the dead, preventing the downtime of the application.
Kubernetes also has an inbuilt mechanism that allows individual containers in the cluster to communicate with each other. 

To understand how Kubernetes is able to provide these facilities,it is important to get a sense of how it is designed and organized at a high level. One can visualize kubernetes as a system built on layers,with each layer abstracting the complexity of lower layers 

At the base of the system, Kubernetes brings together the individual computers and Virtual machines into a cluster using a shared network for server communication.

Kubernetes cluster has one server as a master server, which acts as a gateway or brain for the cluster. Master node has an (Kube-apiserver) API for user and client interactions, maintaining the other servers,allocating the resources to nodes.
We communicate with the cluster(basically with the API server) using kubectl commands.

The nodes are responsible for running workloads using external and local resources. Kubernetes runs apps and services in containers, so each node has a container runtime(example Docker) and also has kubelet (think of this like a captain of a ship) which listens to the master node for instructions like creating or destroying pods as need.

The most important design principle in Kubernetes is we simply define the desired state of our system and Kubernetes works to ensure that the actual state is reflects the desired state. So we don't need to necessarily log in to cluster and check for the things broken and fix.
All we got to do is to state what our system or cluster should look like. We submit a declarative plan in JSON or YAML defining what to create and how it should be managed.
Below is an example pod deployment file.
 
```yaml
#pod.yaml file
apiVersion: v1
kind: Pod
metadata: 
   name: site
   labels:
      app: my-app
spec:
    containers:
    - name: front-end
      image: nginx
      ports:
      - containerPort: 80
    - name: reader
      image: 
      ports: sravani/php-ngnix:v1
      - containerPort: 88
```
The components on the master server work together to accept user requests, determine the best ways to schedule workload containers, authenticate clients and nodes, adjust cluster-wide networking, and manage scaling and health checking responsibilities. We will look at each of the individual components in the master node and try to understand their functionalities.

![architecture](/blog/assets/img/Introduction-to-Kubernetes-Architecture/architecture.png)



## **etcd**

etcd is a key-value store used to store the state of our cluster and it acts like a backend service discovery and database,it  runs on different servers in Kubernetes clusters at the same time to monitor changes in clusters and to store state/configuration data.

We use etcd to persist information regarding our cluster configuration, object(example pods) specifications, object statuses, nodes on the cluster, and which nodes the objects are assigned to run on.

## **kube-apiserver**

It is the most important component of the master node as it acts as a bridge between various components to maintain cluster health and is also responsible for making sure that the data in etcd store and service details of the deployed objects are in agreement. 

For example,we have specified that we need two replicas (instances) of a pod and now one pod died,the etcd store updates the state of the pod, kube-apiserver notices the change in etcd and jumps into action to restore the desired state.

## **kube-scheduler**
It is the process that actually assigns workloads to specific nodes in the cluster is the scheduler. This service reads in a workload’s operating requirements, analyzes the current infrastructure environment, and places the work on an acceptable node or nodes.

The scheduler is responsible for tracking available capacity on each host to make sure that workloads are not scheduled in excess of the available resources. The scheduler must know the total capacity as well as the resources already allocated to existing workloads on each server.
 
## **Kube-controller-manager**
There are many controller managers like Replication controller manager ,node controller manager,Endpoints controller etc.
This is the component on the master node that runs all the controllers(imagine this as an office of all controllers).
### Some functionalities of the controllers include:
  * Checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding.(Node controller)

  * Responsible for maintaining the correct number of pods for every replication controller object in the system(Replication Controller)

## **Kubernetes Node Components**
Node components run on every node, maintaining running pods and providing the Kubernetes runtime environment.

## **Container Runtime**:
The container runtime is the underlying software that is used to run containers. In our case, it happens to be Docker. The container runtime is the software that is responsible for running containers.
 Kubernetes supports several runtimes like Docker, containerd, cri-o, rktlet, and any implementation of the Kubernetes CRI (Container Runtime Interface).

## **Kubelet**:
Kubelet is the agent that runs on each node in the cluster. The agent is responsible for making sure that the containers are running on the nodes as expected.
It’s a small service in each node responsible for relaying information to and from control plane service. It interacts with etcd store to read configuration details and write values. This communicates with the master component to receive commands and work. The kubelet process then assumes responsibility for maintaining the state of work and the node server. It manages network rules, port forwarding, etc.
The kubelet takes a set of PodSpecs that are provided through various mechanisms and ensures that the containers described in those PodSpecs are running and healthy. The kubelet doesn’t manage containers which were not created by Kubernetes.
## **Kube-Proxy** :
This is a proxy service which runs on each node and helps in making services available to the external host. It helps in forwarding the request to correct containers and is capable of performing primitive load balancing. It makes sure that the networking environment is predictable and accessible and at the same time it is isolated as well. It manages pods on node, volumes, secrets, creating new containers’ health checkup, etc.



## References
[Introduction to Kubernetes](https://www.digitalocean.com/community/tutorials/an-introduction-to-kubernetes)

[Kubernetes Documentation](https://kubernetes.io/docs/home/)