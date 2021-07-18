---
 layout: post
 title: "Introduction to Kubernetes Architecture"
 author_github: sravanireddy1102
 date: 2021-07-26 00:00:30
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

Let's take a look at how application development and deployment has changed over time.

![container_evolution](/blog/assets/img/Introduction-to-Kubernetes-Architecture/containerevolution.png)

### **Traditional deployment era**

Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. For example, if multiple applications run on a physical server, there can be instances where one application would take up most of the resources, and as a result, the other applications would underperform. A solution for this would be to run each application on a different physical server. But this did not scale as resources were underutilized, and it was expensive for organizations to maintain many physical servers.

### **Virtualized deployment era**

As a solution, virtualization was introduced. It allows you to run multiple Virtual Machines (VMs) on a single physical server's CPU. Virtualization allows applications to be isolated between VMs and provides a level of security as the information of one application cannot be freely accessed by another application.

Virtualization allows better utilization of resources in a physical server and allows better scalability because an application can be added or updated easily, reduces hardware costs, and much more. With virtualization you can present a set of physical resources as a cluster of disposable virtual machines.

Each VM is a full machine running all the components, including its own operating system, on top of the virtualized hardware.

### **Container deployment era**

Containers are similar to VMs, but they have relaxed isolation properties to share the Operating System (OS) among the applications. Therefore, containers are considered lightweight. Similar to a VM, a container has its own filesystem, share of CPU, memory, process space, and more. As they are decoupled from the underlying infrastructure, they are portable across clouds and OS distributions.

## Containers have become popular because they provide extra benefits, such as

* **Agile application creation and deployment**:
Increased ease and efficiency of container image creation compared to VM image use.
* **Continuous development, integration, and deployment**:
provides for reliable and frequent container image build and deployment with quick and easy rollbacks (due to image immutability).
* **Dev and Ops separation of concerns**:
create application container images at build/release time rather than deployment time, thereby decoupling applications from infrastructure.
Observability not only surfaces OS-level information and metrics, but also application health and other signals.
* **Environmental consistency across development, testing, and production**: Runs the same on a laptop as it does in the cloud.
* **Cloud and OS distribution portability**:
 Runs on Ubuntu, RHEL, CoreOS, on-premises, on major public clouds, and anywhere else.
* **Application-centric management**:
Raises the level of abstraction from running an OS on virtual hardware to running an application on an OS using logical resources.
* **Loosely coupled, distributed, elastic, liberated micro-services**:
applications are broken into smaller, independent pieces and can be deployed and managed dynamically – not a monolithic stack running on one big single-purpose machine.
* **Resource isolation**: predictable application performance.

Now that we have understood what container is and what VM is.

**Let's understand why we use Kubernetes.**

Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers that run the applications and ensure that there is no downtime. For example, if a container goes down, another container needs to start. Wouldn't it be easier if this behavior was handled by a system?

That's how Kubernetes comes to the rescue!. It takes care of scaling and failover for your application, provides deployment patterns, and more.

The components on the master server work together to accept user requests, determine the best ways to schedule workload containers, authenticate clients and nodes, adjust cluster-wide networking, and manage scaling and health checking responsibilities. We will look at each of the individual components in the master node and try to understand their functionalities.

![architecture](/blog/assets/img/Introduction-to-Kubernetes-Architecture/architecture.png)

As you can see in the diagram, there are a lot of terms that you might not understand. I will explain it one by one.

## Master

Master is the controlling element or brain of the cluster.Master has 3 main components in it:

### API Server

The application that serves Kubernetes functionality through a RESTful interface and stores the state of the cluster.

### Scheduler

Scheduler watches API server for new Pod requests. It communicates with Nodes to create new pods and to assign work to nodes while allocating resources or imposing constraints.

### Controller Manager

Component on the master that runs controllers. Includes Node controller(basically checks if desired number of nodes are active), Endpoint Controller, Namespace Controller, etc.

## Worker Nodes

These machines perform the requested, assigned tasks. The Kubernetes master controls them. There are 4 component inside Nodes:

### Pod

 All containers will run in a pod. Pods abstract the network and storage away from the underlying containers. Your app will run here.
This is how we deploy pods on the node.

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

### Kubelet

Kubectl registering the nodes with the cluster, watches for work assignments from the scheduler, instantiate new Pods, report back to the master.

### Container Engine

Responsible for managing containers, image pulling, stopping the container, starting the container, destroying the container, etc.

### Kube Proxy

Responsible for forwarding app user requests to the right pod.
I’m not going to describe the detailed concept here, cause it will lead to a boring situation.
You can read the official documentation for more details information.[Click here](https://kubernetes.io/docs/home)

## References

[Introduction to Kubernetes](https://www.digitalocean.com/community/tutorials/an-introduction-to-kubernetes)

[Kubernetes Documentation](https://kubernetes.io/docs/home/)
