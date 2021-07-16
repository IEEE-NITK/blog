---
layout: post
title: "What is Reinforcement Learning capable of?"
author_github: Aryaman2912
date: 2021-05-07 17:41:00
image: '/assets/img/'
description: 'Applications of reinforcement learning in games, robotics and multi-agent systems'
tags:
- Reinforcement Learning
- Games
- Robotics
- Multi-Agent Systems
categories:
- CompSoc
github_username: 'Aryaman2912'
---

Have you ever been so lazy that you thought, “it would be great if there wes a robot to get me food from the kitchen”? Or have you ever wondered what it would be like if there were robots to do your daily chores for you? Well, the good news is, it is indeed possible to make such an intelligent robot. But if we are to achieve this, reinforcement learning will play a big part in it. In this blog, we will explore the potential of reinforcement learning and how it can be useful in various fields. 

## What is Reinforcement Learning?

Machine learning can be broadly classified into three paradigms - supervised learning, unsupervised learning, and machine learning. In supervised learning, we are given input and output data using which we derive a function between the input data and output data. This function is then used to make predictions on sets of unseen input data. Supervised learning is used in computer vision, speech recognition, etc. In unsupervised learning, we are not given the output labels in the training data. Instead, the task is centered around finding patterns and trends in the data. Unsupervised learning is instrumental in clustering, targeted advertisements, etc. The third paradigm is what we are most interested in for this blog. Reinforcement learning is concerned with how an agent takes actions in an environment to maximize the total reward. Reinforcement learning(RL) differs from supervised learning in that it does not need labeled input and output pairs, and it does not need suboptimal actions to be corrected by any human influence. RL is similar to unsupervised learning as the agent tries to find patterns in the environment. However, the goal in RL is not just finding patterns, but also finding an optimal policy that maximizes the reward. This makes it different from unsupervised learning. Also unlike most unsupervised learning problems, we are not given any data apriori, instead, we need to generate it by interacting with the environment.

Typically, we have an agent following a policy/strategy in an environment, using which it takes actions/decisions to improve its cumulative reward over the interaction with the environment. Reinforcement learning tasks are usually modeled as Markov Decision Processes(MDP). This consists of:
* a set of states for the environment and the agent, S
* a set of actions for the agent, A
* probability of transitions from one state to another based on the current state and the action taken
* a reward function to decide the reward that needs to be assigned on a transition from one state to another when a particular action is taken

The eventual goal for the agent is to maximize its overall reward. It does this by balancing exploring new states and exploiting already available knowledge.This is popularly known as the [exploration-exploitation dilemma](https://towardsdatascience.com/intro-to-reinforcement-learning-the-explore-exploit-dilemma-463ceb004989).

Reinforcement learning can be applied to many fields, including game theory, robotics, multi-agent systems, economics, and many more. Let us now explore a few interesting applications of reinforcement learning.

## Applications

### Games

In all the applications of RL, we have made the most progress with games. This is partially because the rules are predefined, and there is not much room for unexpected activities happening, unlike in real life. Nevertheless, we can take the learnings and concepts from the successes in games and use them as a foundation in other real-life tasks. In 2016, [Deep Mind's AlphaGo](https://deepmind.com/research/case-studies/alphago-the-story-so-far) defeated the Go world champion Lee Sedol 4-1 in a convincing victory. In the second game of the five-match series, AlphaGo made an unexpected move([Move 37](https://www.wired.com/2016/03/two-moves-alphago-lee-sedol-redefined-future/)) that had a probability of 1 in 10000 of being made by humans. Most people initially thought that the move was bad. But later, this turned out to be an important factor in swaying the game towards AlphaGo’s. So AlphaGo could find moves that humans generally ignored.This gives us an insight into what reinforcement learning and artificial intelligence can offer us as we improve the technology and algorithms. If we can use reinforcement learning for building tools that can help us in real life, those tools will be able to help us resolve problems and issues in a way that might have never been imagined by humanity. On the other hand, in game 4 of the above mentioned series, the machine made some poor moves and ended up losing the game in a way that made AlphaGo look very silly. This shows that we still have a long way to go in making our systems more robust and error-free. Like AlphaGo, there are other machines like [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero) (for chess, shogi, and go) and [AlphaStar](https://en.wikipedia.org/wiki/AlphaStar_(software)) (for the strategy-based video game StarCraft II). Both these machines use deep reinforcement learning techniques and have achieved success to a high degree. It is also worth mentioning [Agent57](https://deepmind.com/blog/article/Agent57-Outperforming-the-human-Atari-benchmark), the deep reinforcement learning agent that plays the Atari57 suite of games. Agent57 has successfully outperformed the human atari benchmark.

### Robotics

Robotics is a more exciting field than games because, unlike gaming, it applies a lot to the real world and the challenges faced in robotics are harder to solve. In principle, RL can enable real-world robots to acquire large repertoires of skills. More importantly, reinforcement learning can allow such systems to continuously improve the proficiency of their skills from experience without much human intervention. Agents trained using reinforcement learning have the potential to adapt to unstructured and very complex environments. This is because, in a real-world scenario, the agent might not know how the environment is going to be, and hence, it has no data. The agent must be able to collect data on its own and then learn to behave accordingly. In such cases, it is not possible to use supervised and unsupervised algorithms as they usually work well when there is enough data available. Reinforcement learning allows the agent to learn to behave in situations accordingly based on its experience.

RL today has mostly been used for simplistic and less cost consuming tasks. This is important to note because trying to apply RL directly to high level tasks might result in extreme damages either in financial terms or for humans. Hence, it is important to master the little things first before moving to more ambitious ideas. [Kormushev et al](https://kormushev.com/papers/Kormushev_Humanoids-2010.pdf) demonstrates a robot that learns archery using reinforcement learning algorithms. [Kormushev et al](http://vigir.missouri.edu/~gdesouza/Research/Conference_CDs/IEEE_IROS_2010/data/papers/1230.pdf) also uses the state-of-the-art EM based PoWER algorithm for learning the pancake flipping task. It is very likely that reinforcement learning will become a very important tool in improving robotic systems because algorithms are always ever improving. [This](https://www.youtube.com/watch?v=O4WV1WP6bTk) video offers a small insight into the work and experiments being conducted on robotic reinforcement learning in UC Berkeley.

A popular and commonly used approach for robot learning is simulation to real-world transfer. In this, an agent is first trained in a simulated environment and then let out into the real world after learning appropriate behaviors. However, the policies trained entirely in simulation may fail to generalize on a robot in the real world. It is hard to simulate the real-world exactly in a simulation because there is always a degree of unpredictability in the real-world which may not be modeled in the simulation. Physical factors like friction, air resistance, humidity, etc are hard to simulate. Even though these can be simulated in good simulators, in real-world, these factors are dynamic which makes training much harder. This gap in an impressive performance in simulation and poor performance in the real world is known as reality gap. Training robots with reinforcement learning directly in the real world eliminates these problems. However, this method comes with its own set of challenges. 

Challenges associated with real-world robotic reinforcement learning are:
* As mentioned earlier, an RL task is usually modeled as an MDP. In such a task, all the states are reset after an episode, and the agent is allowed to attempt the same task again. In a real-world environment, such a reset is not possible.
* The states are not directly available in a form suitable for applying in an MDP. The agent usually has cameras, motion sensors, etc. The data obtained from it must be converted to a state ideal for MDPs.
* Typically, rewards are expressed as a function of states or are given by an external supervisor. However, it is more effective if the agent can infer rewards from its sensory inputs.

Solving these challenges is essential to have scalable, efficient, and practical robotic systems.

So how do we build systems for real-world robotic RL? We need three things:

* **Reset free learning**: Essentially, this means the agent should be able to learn the optimal policy without needing to reset all the states after each episode. This can be done by learning a ‘perturbation controller’ which changes the agent’s state so that it is never stuck in a particular state for too long, which can happen in some cases, including when it reaches the goal. Also, once the task is completed, the agent is then transferred to a state that has been less explored. 
* **Unsupervised learning for state estimation**: Findings and observations taken from the cameras and other sensors are often hard to use in reinforcement learning and slow the entire process. The algorithms would require data in numerical terms such as coordinates of the agent but this is not easy to extract from cameras and other sensors due to the fact that these are usually higher dimensional. In order to resolve this issue, we use unsupervised learning techniques to condense images into only the necessary features. This can then be fed into the reinforcement learning algorithm for learning the optimal behavior.
* **Classifier-based rewards**: To minimize external influence in the learning process, we need to have a system that assigns rewards to itself based on a human’s desired outcome. Once these outcomes are given, the agent can self assign rewards based on the probabilities of the agent reaching its goal state from the current state.

Once these three ingredients are put together, we can have a robotic system that works well without human interference. This system can learn to perform several tasks without instrumentation. Although these systems are currently able to perform limited and simplistic tasks, it is important to note that the concepts laid above are essential to building any robotic systems of any desired complexity. 

### Multi-Agent Systems

Until now, what we saw was restricted to single-agent systems. We had only one agent in the environment, and its goal was to maximize its own reward and find the best policy. If we can succeed in creating intelligent robotic systems using reinforcement learning, it is very likely that we will also be inclined towards creating a system where there are multiple robots focussed on one task or various tasks. This is where the concept of multi-agent systems comes in. Multi-agent systems consist of multiple autonomous entities (artificial agents or humans or both) with computational abilities interacting in an environment with distributed/decentralized information with similar, conflicting, or mixed interests. Typically, these agents refer to software agents. When it comes to reinforcement learning, we attempt to make the agents intelligent and study how agents can collectively learn, collaborate, and interact with each other in an environment. RL in multi-agent systems is also known as Multi-Agent Reinforcement Learning (MARL). MARL is a domain that has existed for many years. But the progress that has been made in deep RL (via powerful and scalable function approximators like neural networks) has catalyzed work and progress in this field. 

MARL has a lot of potential for real-world applications. One area of application is [resource allocation and task allocation](https://www.scitepress.org/papers/2017/63934/63934.pdf). MARL can help in devising optimal strategies to divide available resources among different agents/processes. This could potentially offer a new insight into optimally utilizing computing resources. Another application is for [traffic signal control](https://arxiv.org/pdf/1903.04527.pdf). AI-based approaches have been investigated in order to optimize traffic flow in junctions. MARL offers a solution to minimize traffic delays using efficient strategies to allocate time for each lane of an intersection in a traffic network. MARL has also seen improvement in games like Dota, Starcraft,  Go, etc. MARL could also be applied for the task of [energy sharing optimization](https://arxiv.org/pdf/1810.03679.pdf). [Youngwoon Lee et al](https://arxiv.org/pdf/1911.07246.pdf) applied MARL to robotics to assemble IKEA furniture but this direction is currently beyond our scope.

These applications show not only the power that MARL possesses but also the diverse nature of problems that it can be applied to. However, MARL comes with its own set of challenges and hurdles. 

Challenges with MARL:
* In single-agent RL, the environment reacts (via observations and rewards) in response to just a single agent's actions. However, when there are multiple agents, it depends on the actions of all the agents. This introduces a notion of non-stationarity where if an agent just myopically optimizes its own objective function without taking into account the behavior of the other agents, it generally fails. This is one of the core problems with RL in multi-agent systems and is difficult to tackle.
* In order to resolve the above issue of non-stationarity, it is possible to have a single policy that can give the actions for all the agents. That way, we can keep the policy of an agent stationary. But in this case, the number of state-action pairs increases exponentially, and hence the algorithm slows down drastically. Also, one of the key aspects of multi-agent systems is that the agents should be able to take actions via decentralized information available to them in the form of their local observations. This gets violated if we have a single global policy that takes actions for all agents. 

In recent years, there have been a few positive results towards solving the above mentioned issues. For example, [Thanh Thi Nguyen et al](https://arxiv.org/pdf/1812.11794.pdf) have offered solutions to the non-stationarity problem using Lenient Deep Q-Network or LDQN. 

## What Next for Reinforcement Learning?
In this blog, we have seen the applications of reinforcement learning in just three areas. However, reinforcement learning can be applied to a lot more fields, including stocks and finance, medicine, and others. When compared to the other paradigms of machine learning, we can say that reinforcement learning is still in its early stages, and that leaves it with a lot of opportunities that can be explored by scientists and researchers. We have seen in history that given enough time, any problem in science can be overcome if there is enough research going into it. It is no different with RL. We will continue to see a lot of progress in this field, and a future where robots are a part of our everyday lives is waiting for us.

## References
* [AlphaGo: The story so far](https://deepmind.com/research/case-studies/alphago-the-story-so-far)
* [The Ingredients of Real World Robotic Reinforcement Learning](https://bair.berkeley.edu/blog/2020/04/27/ingredients/)
* [Deep Reinforcement Learning for Multi-Agent Systems: A Review of Challenges, Solutions and Applications](https://arxiv.org/pdf/1812.11794.pdf)



