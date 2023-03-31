---
 layout: post
 title: "Transformers"
 author_github: Ayman161803
 date: 2023-03-31 00:00:00
 image: '/assets/img/halting-problem'
 description: ''
 tags:
 - IEEE NITK
 - Blog
 - Computability Theory
 categories:
 - CompSoc
 github_username: 'Ayman161803'
---

## Introduction

In today's world, we see computers doing amazing stuff. They can drive cars, walk like humans, talk like humans and even analyse sentiments. The computational abilities of computers are also increasing at a fast pace. This might make us wonder- Is there really anything that the computers CANNOT do?
Is there really something that a massive supercomputer with the best computional abilities fails to achieve?

![Powerful Machine](http://kinooze.com/wp-content/uploads/2012/12/computers-main.jpg)

## Halting Problem

Enter - The Halting Problem. The halting problem asks whether it is possible to write a program that determines whether another program can halt given certain inputs? Notice that we do not care whether the answer is right or not. Some answer is better than no answer. A program that halts will return with an answer and exit computation. A program that never halts will run forever. It turns out that no computer can solve such a problem. In 1936, Alan Turing constructed such a model and considered the question of determining whether a program will finish running or will continue to run forever i.e. halt. This is known as the Halting Problem.


![Halting Machine](/blog/assets/img/halting-problem/1.png)



Suppose we do end up writing a program H which can scan through a program P with input I and determine whether the P will halt or will run forever. 

![H](/blog/assets/img/halting-problem/2.png)

Now lets consider another program D that encompasses H. D takes a program P and inputs I as parameters. D then passes on these parameters to H. If H returns true i. e. if H determines that P runs forever, D will halt. But if H returns False,  i. e. if H determines that P halts, D will runs forever. So far. So good.

![D](/blog/assets/img/halting-problem/3.png)

The problem arises when we try to feed in D into the program D. If D runs forever, H will have to correctly determine that D runs forever which will then halt the program D giving us a contradiction. If D halts with input I, H will determine that D halts which will then make D run forever. There must be something here. It all started when we assumed that we could write a program H that can correctly deterime whether an program P will halt given inputs I. Therefore, our assumption must be wrong proving that no program however powerful can determine whether another will halt or not given certain inputs. So the next someone is fascinated with how programs can achieve anything and everything, introduce them to The Halting Problem. 

![D to D](/blog/assets/img/halting-problem/4.png)