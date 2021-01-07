
---

layout: post

title: "Introduction to Optimisers"

author_github: jkk2000

date: 2021-01-07 19:09:24

image: '/assets/img/'

description: 'What optimisers in dl are and its types'

tags:

- IEEE NITK

- Optimisers

- Deep learning

categories:

- CompSoc

github_username: 'jkk2000'

---

  

## What is an Optimiser

In Layman terms, an Optimiser is an algorithm which tweaks and changes the parameters _(weights)_ of the model and try to minimise the loss function _(A function which mathematically measures how wrong the model's predictions are)_. In simpler terms, optimizers shape and mold your model into its most accurate possible form by futzing with the weights. The loss function is the guide to the terrain, telling the optimizer when it’s moving in the right or wrong direction.

  

## Machine Learning as Optimisation

Almost all machine learning algorithms can be constructed as an optimization problem to find the minima of a objective function _(ie loss, error, etc)_. Building models and constructing reasonable objective functions are the first step in machine learning methods. With the determined objective function, appropriate numerical or analytical optimization methods are usually used to solve the optimization problem.

  

Optimization is one of the core components of machine learning. The essence of most machine learning algorithms is to build an optimization model and learn the parameters in the objective function from the given data. In the era of immense data, the effectiveness and efficiency of the numerical optimization algorithms dramatically influence the popularization and application of the machine learning models. In order to promote the development of machine learning, a series of effective optimization methods were put forward, which have improved the performance and efficiency of machine learning methods.

  

## Gradient Descent
![Grad decent](https://hackernoon.com/hn-images/1*f9a162GhpMbiTVTAua_lLQ.png)
When we initialize our weights, we are at point A in the loss landscape. The first thing we do is to check, out of all possible directions in the x-y plane, moving along which direction brings about the steepest decline in the value of the loss function. This is the direction we have to move in.

  

Now, once we have the direction we want to move in, we must decide the size of the step we must take. The the size of this step is called the learning rate. We must chose it carefully to ensure we can get down to the minima.

  

If we go too fast, we might overshoot the minima, and keep bouncing along the ridges of the _valley_ without ever reaching the minima. Very slow learning rates make the algorithm more prone to get stuck in a minima.

  

Once we have our gradient and the learning rate, we take a step, and recompute the gradient at whatever position we end up at, and repeat the process. Often, we stop our iterations when the loss values haven't improved in a pre-decided number, say, 10, or 20 iterations. When such a thing happens, we say our training has converged, or convergence has taken place.

  

### Intuition for Gradient Descent
![Blind Hiker](https://miro.medium.com/proxy/1*N5WjbzwsCFse-KPjBWZZ6g.jpeg =600x400)
Imagine you’re blind folded in a rough terrain, and your objective is to reach the lowest altitude. One of the simplest strategies you can use, is to feel the ground in every direction, and take a step in the direction where the ground is descending the fastest. If you keep repeating this process, you might end up at the lake, or even better, somewhere in the huge valley.

  

The rough terrain is analogous to the cost function. Minimizing the cost function is analogous to trying to reach lower altitudes. You are blind folded, since we don’t have the luxury of evaluating _(seeing)_ the value of the function for every possible set of parameters. Feeling the slope of the terrain around you is analogous to calculating the gradient, and taking a step is analogous to one iteration of update to the parameters.


### Steps of Gradient Descent

1. Use model parameters $(m_j,b_j)$ to calculate the error $E(m,b)$

2. Calculate the partial derivatives $∂E/m_j$ and $∂E/b_j$

3.  Calculate the new estimates:


$$
m_{j+1}  := m_j - \gamma\frac{\partial}{\partial m_j} E(m,b)
$$
$$
b_{j+1}  := b_j - \gamma\frac{\partial}{\partial b_j} E(m, b)
$$
> where γ is the learning rate.

We repeat these three steps till the model converges.

## Faster Optimizers
![Comparision](https://i.pinimg.com/originals/63/62/8f/63628f546ad55fd31091e23c623cb9f5.gif)
Training a very large deep neural network can be painfully slow. A huge speed boost comes from using a faster optimizer than the regular Gradient Descent optimizer. In this section we will present the most popular ones: Momentum optimization, Nesterov Accelerated Gradient, RMSProp, and finally Adam optimization.

  

### Momentum Optimization

Imagine a bowling ball rolling down a gentle slope on a smooth surface: it will start out slowly, but it will quickly pick up momentum until it eventually reaches terminal velocity _(if there is some friction or air resistance)_. This is the very simple idea behind Momentum optimization.

  

The gradient is used for acceleration, not for speed. To simulate some sort of friction mechanism and prevent the momentum from growing too large, the algorithm introduces a new hyperparameter $β$, simply called the momentum, which must be set between $0$ _(high friction)_ and $1$ _(no friction)_. A typical momentum value is $0.9$.

  

We are using exponentially weighted which would kinda denoise the gradients and get us close to the real value, we need to do this because gradient decent is applied on mini-batches and their gradients may not point in the direction of the whole training dataset as they might be noisy. Because we estimate the gradient which is closer to the actual derivative than the standard noisy gradient, it performs better than vanilla SGD _(Gradient Descent with momentum)_.

  

### Nesterov Accelerated Gradient

One small variant to Momentum optimization, proposed by Yurii Nesterov in 1983, 13 is almost always faster than vanilla Momentum optimization. The idea of Nesterov Momentum optimization, or Nesterov Accelerated Gradient (NAG), is to measure the gradient of the cost function not at the local position but slightly ahead in the direction of the momentum. The only difference from vanilla Momentum optimization is that the gradient is measured at $w + βm$ rather than at $w$ ($w$ is the weight of the model).

  

### RMSProp

The basic idea is that if there is one parameter in the neural network that makes the estimate of the Loss $E$ oscillate a lot, you want to penalize the update of this parameter during optimization, so to avoid the gradient descent algorithm adapt too quickly to changes in this parameter, as compared to the others.

  

The fact the parameter in question makes $E$ oscillate a lot is an indicator that the derivative of $E$ with respect to this parameter is much larger than the derivatives for the rest of parameters. Hence, the normalization factor applied in RMSprop to the update of this parameter (i.e. its root mean square) will be larger compared to the rest of parameters, and the result of the normalization (and the update) smaller.

  

### Adam

Adam, which stands for adaptive moment estimation, combines the ideas of Momentum optimization and RMSProp. Like Momentum optimization it keeps track of an exponentially decaying average of past gradients, and just like RMSProp it keeps track of an exponentially decaying average of past squared gradients

  

This algorithm is very popular because it makes the model converge very fast. Hence is one of the best choices for Optimisation algorithms.

  

## References
- [Ml as Optimisation](https://arxiv.org/pdf/1906.06821.pdf)
- [Gradient Descent](https://builtin.com/data-science/gradient-descent)
- [Intuition](https://www.kdnuggets.com/2018/06/intuitive-introduction-gradient-descent.html)
- Géron, A. (2017). _Hands-on machine learning with Scikit-Learn and TensorFlow : concepts, tools, and techniques to build intelligent systems_. Sebastopol, CA: O'Reilly Media. ISBN: 978-1491962299
- [Adam](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/#:~:text=Adam%20is%20an%20optimization%20algorithm,iterative%20based%20in%20training%20data.&text=The%20algorithm%20is%20called%20Adam,derived%20from%20adaptive%20moment%20estimation.)
- [CS231 notes](https://cs231n.github.io/neural-networks-3/)
- [RMSProp](https://towardsdatascience.com/understanding-rmsprop-faster-neural-network-learning-62e116fcf29a)
- [Momentum](https://towardsdatascience.com/stochastic-gradient-descent-with-momentum-a84097641a5d)

