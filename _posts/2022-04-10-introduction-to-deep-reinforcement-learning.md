---
layout: post
title: "Introduction to Deep Reinforcement Learning"
date: 2022-04-10 00:05:00
image: '/assets/img/'
description: 'Introduction to Deep Reinforcement Learning'
tags:
- IEEE NITK
- CompSoc
- Reinforcement Learning
- Deep Learning
categories:
- CompSoc
github_username: 'anirudhprabhakaran3'
---

In March 2016, a small company based out of London shook the computer science world. They had built a program that defeated the world champion, Lee Sedol, at the ancient Chinese game of Go. The game Go is considered the most challenging game for artificial intelligence to master, because of its complex nature. Scientists said that a breakthrough would be at least ten years in the making. That was, until AlphaGo came along.

Now, I could talk on about how great the five-match tournament was, or how AlphaGo has now matured into MuZero. Instead, today we'll talk about what powers AlphaGo and all its successors - Deep Reinforcement Learning.

## Deep Reinforcement Learning

Deep Reinforcement Learning is basically what it says on the box - it is a mixture of Deep Learning and Reinforcement Learning. While RL focuses on solving tasks and finding solutions based on trial-and-error, DL focuses on getting information about the state from the input. Combining these two together give us a great tool, DRL, which allows the agents to make decisions based on the unstructured input data without explicitly programming it.

DRL has been used for a varied set of applications like robotics, video games, natural language processing, computer vision, education, transportation, finance and healthcare. It is one of the hottest topics in the ML/AI world, has lots of research being poured into it and a lot of scope for it in the future.

## History

Once common thread lies between all the researchers in different subfields of artificial intelligence - to find out, model and simulate the human brain. With the rise in neural networks in the 1980s, we came a step closer to achieving that goal, and the obvious next step was to take a look at DRL.

Along with the rise in usage of neural networks and deep learning, the next part of the puzzle was placed when in 2012, there was a revival of the Deep Learning revolution. People started looking into using deep neural networks to learn and understand the policy, value and/or Q functions for reinforcement learning algorithms.

## Types

There are primary two types of DRL algorithms.

In **model-based** DRL algorithms, a forward model of the environment is estimated, usually using supervised learning. Future actions are obtained by model predictive control using the learned model. This leads to some interaction of the agent with the environment, causing a change in the environment, which leads to a new future action; and the loop continues.

In **model-free** DRL algorithms, a policy is learnt without explicitly modelling the forward dynamics. The policy can be optimised to maximize returns by estimating the policy gradient, but that comes with its own drawbacks. Another class of algorithms are rely on dynamic programming, inspired by Q-learning.


## Case Study - AlphaGo

![AlphaGo vs Lee Sedol](/blog/assets/img/deep-reinforcement-learning/alphago-vs-lee-sedol.jpeg)

Let's return back to AlphaGo. We'll try to examine how DeepMind used DRL to make their program, and what made it possible to make the program so amazing.

AlphaGo takes in the Go board as the input. The neural networks try to learn and extract information from the input. One of the neural networks, called the _policy network_, selects the next move to play. The other network, called the _value network_, predicts the winner of the game. Sounds simple, right? This approach is sort of how our brain also processes information and takes a decision - one part thinks about what we should do next, and the other part figures out what the outcome would be if we made that move, and if the outcome was favourable to us. This bicameralism makes the program very powerful, and sort of mimics the human brain.

AlphaGo was trained with some amateur games, so that it could learn the rules and get more information about Go. Then, DeepMind had it play with different versions of itself, thousands of times. This lead to AlphaGo becoming stronger and stronger, until it was proficient enough to beat the current word champion, Lee Sedol.

## Where do we go from here?

Deep Reinforcement Learning is an exploding subfield, with research being done at a massive scale and pace. There are lots of topics on which research is happening, including but not limited to off-policy RL, Inverse RL and Multi-agent RL. The real world applications include robotics, sustainability, and helping make scientific and mathematical advancements that were thought to be years away.

DRL might be the closest that we have come to modelling the function of human brain, and taking inspiration from nature to create something magnificent.