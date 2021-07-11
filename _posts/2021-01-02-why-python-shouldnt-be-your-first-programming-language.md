---
layout: post
title: "Why Python Shouldn't be your First Programming Language"
author_github: nishant-nayak
date: 2021-01-02 22:09:24
image: '/assets/img/'
description: 'An overview of the shortcomings of Python for programming beginners'
tags:
- IEEE NITK
- Python
- Programming
categories:
- CompSoc
github_username: 'nishant-nayak'
---

## Introduction

Python is a programming language that has found its way into practically every field of software development. With its immense collection of openly available libraries, easy to learn syntax, and a plethora of available resources to learn from, both online and offline, the knowledge of Python has become one of the most sought-out skills in the industry. The beauty of the language lies in the ability to perform tasks with simple, readable syntax and lesser code to write.

![Python Logo](/blog/assets/img/why-python-shouldnt-be-your-first/python-logo.png)

All the hype around Python is what attracts a lot of beginners to pick up the language as their first programming language. However, the *pythonic* way of writing code usually abstracts a lot of essential information about the very basics of programming, which is crucial for beginners to understand. Here’s a few points on why Python shouldn’t be your first programming language:

### Variables don’t require a type

In Python, variables can simply be declared by assigning any value to a variable name of the user's choice. Under the hood, Python stores all variables, irrespective of its datatype, in the form of objects. The Python interpreter then binds names to these objects. This makes the syntax of declaring variables simpler, but it abstracts the way the data is stored in memory. For example, C programming language gives you the option to define the datatype of the variable you are storing, which allows the user to understand how many bytes of data that specific variable is taking up. This enables users to understand how the data is stored at the bit level. For beginners, understanding how memory allocation works for specific data types can help in building good coding habits.

### Pointers do not exist

Another abstracted feature that deals with memory is pointers. Pointers are invaluable while accessing members of a list-like data structure, creating certain data-structures like linked lists and trees, or passing variables to a function. In Python, there are two types of objects, namely **mutable objects** that can be changed and **immutable objects** which cannot be changed. When a function is called with an object as a parameter, mutable objects such as lists or dictionaries are passed by reference, and immutable objects such as strings(str) or integers(int) are passed by value. This does not give the user the ability to choose how to pass variables to functions. This interaction with memory locations, and the user defined dynamic allocation of memory are important concepts to be familiar with in order to create memory efficient programs.

### Encapsulation isn’t safeguarded

Data Encapsulation is one of the key features of object oriented programming. In Python, however, the only encapsulation of features within a class is a convention that is to be upheld (putting underscores before the function name). There is no definition of private and public class members, which means that certain members which should actually be immutable can easily be changed by any function in the program. The concepts behind private, public and protected class members are essential for beginners to fully understand, so that they can properly implement data encapsulation.

### The speed isn’t real, and errors show up at the last second

Python is an interpreted language, and therefore runs much slower than a language like C, which is a compiled language. Due to Python’s interpreted nature, each line of code is executed in succession, which means that if there are any errors in the code it won’t show up until the program executes all the lines of code before the line with the bug. This can be frustrating and discouraging for beginners when they are learning the language.

### Parallel Processing is not supported

CPython, which is the standard implementation of Python, has a feature known as the Global Interpreter Lock (GIL), which essentially locks one flow of execution to hold control of the Python interpreter. This means that two separate flows of execution, more commonly known as threads, cannot be run on the same CPU. Since Python programs run as a single process with a single thread of execution, only one CPU core is used, regardless of the number of cores the CPU contains. This increases the runtime of programs that require heavy CPU computation, when compared to languages which support multithreading.


In conclusion, we can all agree that Python has found good use in many fields of computer science, and it is definitely an asset to learn the language in today’s day and age. Nonetheless, a beginner in programming should consider learning a different Object Oriented Programming language like C++ or Java to gain a better grasp on the core concepts of OOPs. Although this is advice from a programming perspective, if the user’s goal is to learn Python only for a specific application like Machine Learning or Data Science, they can go ahead and learn the language to start off.

## References

- [Python Variable Types](https://www.tutorialspoint.com/python/python_variable_types.htm)
- [Pointers in Python: What's the Point?](https://realpython.com/pointers-in-python/)
- [Example of Python's Data Encapsulation](https://www.quora.com/Why-do-some-people-say-that-object-oriented-programming-in-Python-is-a-joke/answer/Antonio-Nesic)
- [Python - Compiled or Interpreted?](https://www.geeksforgeeks.org/python-compiled-or-interpreted/)
- [What is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)