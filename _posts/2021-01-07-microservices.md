---
layout: post
title: "A Beginner's Guide to Microservices"
author_github: gaurang2001
date: 2021-05-14 00:00:00
image: '/assets/img/'
description: 'An overview of an architectural style quickly taking over the world'
tags:
- Microservices
- Cloud
- Systems
categories:
- CompSoc
github_username: 'gaurang2001'
comments: true
---

We live in a world that’s constantly growing. There are new applications and services that come up everyday. Existing ones evolve to constantly meet the demands of today’s world and to keep up with the latest trends in technology. This essentially means that there is hardly any time devoted to the maintenance of such applications and services. Nobody likes down-times. If a service is down for sometime, its users would naturally start looking for alternatives, and with such a huge network of service providers available over the internet, they would quite obviously even find one. This is where Microservices comes into the picture.

This blog delves into the “What” and “Why” of Microservices in detail.

## What are Microservices?

If you are not very new to the world of The Cloud or Systems, then you would’ve heard the term “Microservices” quite frequently. Microservices, as the name suggests, is an architectural style that branches out an application into several small independent applications or services. These individual modules are independently built and deployed. Going by the official definition, 

> Microservices - also known as the microservice architecture - is an architectural style that structures an application as a collection of services that are
> - Highly maintainable and testable
> - Loosely coupled
> - Independently deployable
> - Organized around business capabilities
> - Owned by a small team

The microservice architecture enables rapid, frequent and reliable delivery of large, complex applications.

Let’s go through each of these points one by one.

1. *Highly maintainable and testable* - Since a huge application is broken down into several chunks, it’s not only easier to spot bugs, but also fix them without getting the entire application down. It is also possible to scale up or scale down a component easily, since each of them is completely independent of each other. Scaling up is making a component larger or faster to handle a greater load. In contrast, scaling down refers to decreasing your system resources.
2. *Loosely coupled* - Each of the individual components, as mentioned before, are independent and isolated. They cannot communicate with each other, except through APIs. None of the components have any say on the structure of another communication. This gives the developers working on each of the components complete freedom to build the service as they would like it. A new stack can be added to a service to avail larger benefits at the application level.
3. *Independently deployable* - Each of the components are independently deployed. I had mentioned earlier that it’s possible to scale up or scale down an individual service. This necessarily means that each component has its own set of dependencies. Two components can also work with different versions of the same dependency. This is possible with the use of containers. Each component is containerised along with its dependencies and configurations and independently deployed. (Containerisation simply means that the application, along with all its dependencies, is put into a “container” and is treated as a single unit during deployment)
4. *Organized around business capabilities* - Microservices introduce a massive change in the organisational structure of a business group. Since the overall goal is a good user experience, development teams are no longer divided into web teams, systems teams, database teams and so on. Rather, they are cross functional teams that work towards fulfillment of one single functionality.
5. *Owned by a small team* - A cleaner distribution of functionality into microservices allows for more streamlined organisations with smaller teams.

Now that we know what Microservices are, we need to know why they are required in today’s world. But for that, we first need to know what monoliths are.

## What are Monoliths?

In software engineering, a monolithic application describes a single-tiered software application in which the user interface and data access code are combined into a single program from a single platform. In simple words, it’s an architectural style that does not treat modules independently in an application. The application is deployed as a whole, and all the different components of an application use the same dependencies, etc. It contains a single executable that performs all of the server-side functions for an application. Let me explain with the help of an example.

Let’s consider an e-commerce application. It can have several components to it - a catalogue of products, an ordering system, a payment system, etc. This would mean there are three different containers, one for each service, deployed independently under the Microservices Architecture. Using the Monolithic Architecture, we would need only one container to bundle up the entire application for deployment. 

![Monoliths vs Microservices](/blog/assets/img/microservices/monolith-vs-microservices.png)

## Why Microservices?

We’ve read in detail about what microservices and monoliths are. But why are microservices preferred over monoliths?

Let’s consider a monolithic application with a huge codebase. A small bug somewhere brings the entire application down. It would naturally be difficult to pin-point the location of the bug because of the huge codebase. It also does not make sense to bring the entire application down because of the bug, when the rest of the application is working completely fine. Issues may also arise when scaling up or scaling down the application. All components of the application would have to use the same versions of dependencies. Any conflicts with dependencies can break the entire application.

Now let’s consider the same scenario with Microservices. A small bug in the codebase need not bring the entire application down, since each component is independently deployed. This also means that bugs are easier to trace and fix. Scaling up and scaling down the application is much easier as each component is bundled together with its dependencies and containerised for deployment.

## Conclusion

Although microservices have an edge over traditional monoliths due to the aforementioned reasons, it does come with several drawbacks. As each component is deployed independently and communication between components happens only via APIs, there’s the problem of consistency. It also uses up a lot of resources, as there are multiple deployments, and not just one.

However, the reason microservices are preferred over traditional monoliths is because of its ability to cleverly deal with bugs, and ease of maintenance. It may take up a lot of resources, but with cloud providers like Google Cloud, AWS, MS Azure providing resources at a nominal price, it is a welcome trade-off. After all, nobody likes down-times, and hence, microservices are the way to go.

### References

- [What are Microservices?](https://microservices.io)
- [An Overview of Microservices](https://www.tothenew.com/blog/an-overview-of-microservice-architecture-part-i/)
- [Monolithic Software](https://www.thorntech.com/2017/12/microservices-vs-monoliths-whats-right-architecture-software/)
