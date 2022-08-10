---
layout: post
title: "The Qubit Report"
date: 2022-08-10 00:00:00
author_github: anirudhprabhakaran3
description: 'An introduction to the world of Quantum Computing, the physics that powers it, and what it will power in the future.'
tags:
- IEEE NITK
- Blog
- Quantum
categories:
- Compsoc
github_username: 'anirudhprabhakaran3'
---

# The Qubit Report

In part 1, we looked at quantum computing and its workings. Now, we’re going to look at a few places where this magical technology is being used!

Quantum computing has been around for some time now. The first quantum computer was made in 1998 as a collaboration between three fellows:  Isaac Chuang (Los Alamos National Laboratory), Neil Gershenfeld (Massachusetts Institute of Technology), and Mark Kubinec (University of California, Berkeley). This primitive machine had two qubits and was the first quantum computer that could load some data and give some output. Since then, the field has not hit the breaks yet. The most powerful quantum computer currently has 216 qubits.

![alt_text](/blog/assets/img/qubit-report/image1.png)

## Why Quantum Computing?

Before we look into where all quantum computers are used, we first must understand why we use them. And the answer to that question is simple - for some tasks, the supercomputers we have are not “super” enough.

![alt_text](/blog/assets/img/qubit-report/image2.png)

Some systems are very complex and involve lots of variables. Modelling such systems is difficult for even the supercomputers that we have. In such cases, quantum computers might be of help.

But beware! Quantum computing is not a magic wand that can be applied to any problem. There are specific types of problems that can be handled with the power of quantum computing. But it will not offer much of an advantage for unoptimised problems.

One field in which this technology performs well is modelling the behaviour of individual atoms in a molecule. The infinite complexity of this system is well modelled and handled by the powers of quantum computers.

Let's look into the other fields in which these powerful machines can be deployed.

## Cryptography

Imagine one fine day you wake up. When you check your phone, you see an SMS stating that your bank account has been wiped out. When you check your mail, you find out most of your accounts have been compromised. Sounds scary, right?

The technology that keeps us and our data safe on the Internet. Be it backups of our files, cat videos, or financial transactions. Cryptography is the most critical component of the modern internet - with billions of users, and trillions of requests, making sure your data or request is read only by the intended recipient is critical.

The core of such an essential aspect of modern computing is a very simple concept - factorisation. Risking oversimplification, cryptography is just multiplication. Yes, the numbers multiplied are large prime numbers (nearly 300 digits long), which makes it impossible for classical computers to break.

However, this is a type of task at which quantum computers excel. These machines excel at factorisation and wouldn’t have difficulty breaking modern encryption. Because of this, post-quantum cryptography is now an active research field. This aims to find encryption methods that are not based on prime factorisation or logarithmic arithmetic, thus rendering quantum computers ineffective against this. The following illustration briefly describes one way that quantum cryptography can be leveraged.

![alt_text](/blog/assets/img/qubit-report/image3.png)

Another group researching this is going on another path. They are trying to find a *quantum* method of encryption. This is analogous to the current system - making an encryption algorithm impossible for even quantum computers to break. Similar to the classical case, these algorithms will also resist quantum hacking.

## Machine Learning

![alt_text](/blog/assets/img/qubit-report/image4.png)

At its core, all machine learning is matrix operations. Whether using a standard linear regression or a deep neural network, linear algebra is the essential math underlying machine learning. And this is why we are in luck.

Turns out that most quantum computation techniques use the same mathematics required for artificial intelligence - linear algebra. Because of this, machine learning algorithms and models can be run on such computers, leveraging quantum mechanics' processing power. Popular machine learning frameworks in Python, like TensorFlow, are actively developing quantum counterparts to their normal features. There is an ongoing project for making a quantum version of the PyTorch library, headed by the Massachusetts Institute of Technology (MIT)’s Hardware, AI and Neural Networks (HAN) Lab.

The most recent experiments display the significant speedup and time saved for implementing a reinforcement learning model on a quantum computer compared to a classical one, with either the same or better results and accuracies. More research is being done every day in quantum neural networks and reinforcement learning, and it is a booming research space. The introduction of quantum computing might provide the necessary firepower to make great leaps in machine learning and artificial intelligence. It might even work as the stepping stone to a generalised artificial intelligence (GAI).

![alt_text](/blog/assets/img/qubit-report/image5.png)

<center>The above image is of a quantum chip created by D-Wave. This particular chip acts as a 128-qubit processor. The first machine learning application to run on a quantum computer was an object detection model that could identify cars from digital images. Although not run on this particular machine, the model was first to run on an adiabatic D-Wave quantum computer in 2009.</center>

## Computational Biology

It is pretty fitting - poetic even - that the most advanced computer made by mankind is to be used to improve knowledge about mankind. Living organisms are undoubtedly some of the most complex machines created by nature, whose secrets remain to be revealed. And quantum computers are helping us take a step in that direction.

One of the major domains that computational biologists are looking to leverage is computational genomics. This field tries to find the properties of various organisms using their genome. The computation of the human genome is one of the “grand challenges” of modern biology. With their immense processing capabilities, Quantum computers are helping us get to the bottom of these problems faster.

![alt_text](/blog/assets/img/qubit-report/image6.png)

But this is far from the only application. Some research into MicroRNA functioning is also very active, and there is a scope for many computational biology problems to be tackled by quantum computers.

## Computer-Aided Drug Design

We all are still acutely aware of the situation during COVD-19. Hundreds of scientists worldwide spent hours painstakingly trying to find a vaccine and cure for the virus. After a few candidates were designed, they went through a system of trials to ensure that the drugs worked and were released for public use.

![alt_text](/blog/assets/img/qubit-report/image7.png)

Imagine if, instead of trying so many different combinations of chemicals manually, you could run a software program that would tell the properties of a particular drug and how effective it would be against a particular disease. It would make the lives of every person involved in the process much easy. Also, it would drastically reduce the time needed to design drugs, allowing the process to go to the trial stage much quicker.

Since drug design needs a computer to model the various interactions that molecules and atoms can have with other biological organisms, the processing power of quantum computers is a significant boost for this field. Some algorithms are being developed, like quantum deep neural networks and Quantum Variational Autoencoders (QVA), to help with this process.

## So what is stopping us?

We mentioned many advantages that quantum computers would provide and their real-world implications. But you might have a very logical question after that - why hasn’t this happened yet? Why have the real-world implications stated happened yet? What is stopping us?

Well, the answer to that question is simple. These applications depend on quantum computers, which is the bottleneck. It is extremely difficult to make, run and maintain a quantum computer. The most prominent manufacturers and maintainers of quantum computers, Google and IBM, have around 20 quantum computers each. This is very low compared to the availability of classical computers and hardware. This is very low compared to the availability of classical computers and hardware. The superconducting cables required to build these machines are made only by one company in the world - a Japanese company called Coax Co.

![alt_text](/blog/assets/img/qubit-report/image8.png)
<center>One of Google's Quantum Computers</center>

Apart from this, there are also a few difficulties relating to the physics of these computers. It is a challenge to scale the number of qubits physically. As the number of qubits increases, it also becomes challenging to initialise these with random values. As the number increases, we also need some quantum controller that enables interfacing with them.

![alt_text](/blog/assets/img/qubit-report/image9.png)
<center>One of IBM's Quantum Computers</center>

There are difficulties. However, there is also a lot of work and research in this field to make it more viable to build more such machines. Once we can make more devices like this, human technology will get a considerable boost. Now, it is only a matter of time!
