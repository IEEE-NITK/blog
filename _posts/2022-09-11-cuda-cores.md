---
layout: post
title: "Cuda Cores"
author_github: Jayasrivastava345
date: 2022-09-11 00:00:00
description: 'CUDA is a proprietary technology developed by NVIDIA and stands for Compute Unified Device Architecture ,these are mainly used for parallel computing'

tags:
- IEEE NITK
- Blog
- Cuda cores
categories:
- Diode
github_username: 'Jayasrivastava345'
---

# Parallel processing -Cuda Cores

## What are cores? 

You've probably come across the term **CUDA cores** if you've spent any time looking at graphic card specifications.
In this article, I'll go over CUDA cores in further detail.
But first, let's figure out **what are cores?**

A core is the beating heart of any CPU or GPU, allowing it to focus on only one task at a time while performing it fast and efficiently. The number of cores present in a CPU can determine its overall processing power. The ability of a computer to manipulate data is referred to as processing power.

A single-core CPU is analogous to a human who can either breathe or talk, but not both at the same time. To extend the example, a single-core CPU stops talking when it needs to breathe. It also stops breathing when it needs to talk. Multi-core CPUs, on the other hand, can perform everything at once. Having several cores allows the computer to do a particular type of multitasking called parallel processing.

## What is parallel processing and why parallel processing?

We must first comprehend the concept of parallel processing before writing more on cores. 

Parallel processing is a computing technique that uses two or more processors (CPUs) to perform different sections of a larger operation. Breaking up different parts of a task among multiple processors can help reduce the amount of time to run a program. Typically, a computer scientist will use a software tool to break a complex work into many sections and allocate each part to a processor. Each CPU will solve its section, and the data will be reassembled by a software tool in order to read the answer or do the task. Usually, each CPU will normally run and conduct activities in parallel as directed, retrieving data from the computer's memory. Processors will also use software to communicate to stay in sync with one another. Assuming that all of the processors are in sync, the software will combine all of the data components at the end of a task. Computers without multiple processors can still be used in parallel processing if they are networked together to form a cluster.

Parallel processing can take many different forms. SIMD and MIMD are two of the most widely utilized varieties. SIMD (single instruction multiple data) is a parallel processing technique. Two or more processors in a computer will follow the same instruction set while handling distinct data. SIMD is most commonly used to examine big data sets with the same set of benchmarks. Another frequent type of parallel processing is MIMD or multiple instructions for multiple data. Each computer contains two or more processors and receives data from several different data streams.

MISD, or multiple instruction single data, is a less common type of parallel processing in which each processor uses a separate method with the same input data. Serial processing (also known as sequential processing) can only perform one task at a time using one processor, but parallel processing can complete numerous tasks using two or more processors. A computer that uses serial processing will take longer to finish a complex task than one that uses parallel processing.
 
## Cuda cores description

A single-core CPU is quick, but it has its limitations. A multi-core CPU is slower per task, but it can perform multiple tasks simultaneously. 

Imagine, instead of a CPU with a few cores, a processor with thousands of cores all operating in parallel for specific tasks rather than the more generalized duties that a conventional CPU is faced with. GPUs are equipped with this capability. That's why GPUs are so much slower than CPUs for serial computing yet so much faster for parallel computation.
The cores on a GPU about which this blog is focussed on are **CUDA Cores**.

CPU cores and GPU cores have many commonalities, but they also have numerous distinctions. CPU cores are built to execute many instructions at the same time. They're made for general-purpose calculations and can be used for various tasks. GPU cores are only used for one thing: graphics processing.CPUs have a small number of powerful cores, but GPUs have many cores that are substantially less powerful. A GPU excels at parallel tasks, such as calculating the appearance of hundreds of pixels in fractions of a second. The difference between CPUs and GPUs is that each is purpose-built to do different types of processing.

**CUDA** is a proprietary technology developed by NVIDIA and stands for Compute Unified Device Architecture. CUDA Cores are used for many things, but they’re mainly used for enabling efficient parallel computing. A single CUDA core is analogous to a single CPU core. The main distinction is that it is less powerful but has many implementations, allowing for parallel computation.
A normal CPU has anything from two to sixteen cores, yet even the most fundamental current NVIDIA GPUs have hundreds of CUDA cores. High-end cards, on the other hand, now have thousands of them. CUDA is an interface for accessing those cores and communicating with the rest of your system, not just a group of cores. CUDA cores are the processors that execute those instructions.

## Resources

- [Nice to know: What is CUDA?](https://www.spo-comm.de/en/blog/know-how/what-is-cuda)
- [CUDA Cores](https://www.gamersnexus.net/dictionary/2-cuda-cores#:~:text=CUDA%20Cores%20are%20parallel%20processors,visually%20to%20the%20end%2Duser)