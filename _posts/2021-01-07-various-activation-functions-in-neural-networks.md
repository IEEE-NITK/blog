---
layout: post
title: "Various Activation Functions in Neural Networks"
author_github: SidharthLanka
date: 2021-01-07 20:00:34
image: '/assets/img/SidharthLanka.jpg'
description: 'A look into the various activation functions and their applications.'
tags:
- IEEE NITK
- Machine Learning
- Neural Networks

categories:
- CompSoc
github_username: 'SidharthLanka'

---



## What is a neural network?

A neural network is a series of algorithms that performs machine learning over a dataset through a procedure that artificially mimics the way the human brain functions. Neural networks consist of an input layer, multiple hidden layers, and an output layer. Each of these layers consists of neurons, and the neurons of one layer are connected to the neurons of the next and previous layer forming a deep network.



![Simple Neural Network](/blog/assets/img/Activation-Functions/NN.png)

In the above image, the network consists of an input layer which takes in 4 inputs and an output layer which gives out 3 outputs. There are 2 hidden layers in between. In this neural network, all the neurons from one layer are passed as inputs to neurons of the next layer. Each of these neurons takes in the input values from the previous layer and uses them along with parameters known as weights in an activation function, to get a resultant hypothesis. The hypothesis is the value stored in the neuron and is used as an input for the neurons in the next layer which have their own set of weights. This process continues until the hypotheses for the final output layer are obtained. The model is tuned for several epochs and the weights are updated on the basis of the error obtained at the output.

## What is an activation function?

An activation function takes the inputs into a neuron from other neurons, and its output is stored in the neuron. It has a set of weights or parameters which are fixed in such a way that they determine whether the neuron should be activated or not by calculating weighted sum and by further adding bias with it. Activation functions are used to introduce non-linearity into the neural network, so they can be tuned for complex datasets.

So, it is important for us to know the different activation functions and the situations in which they can be used, so as to improve the accuracy of the dataset, and the overall working of the model, and ensure that overfitting or under-fitting don’t occur.



## Linear Function

#### Mathematical Expression - f(x) = mx + c

![Graph](/blog/assets/img/Activation-Functions/linear.png)

This is the simplest activation function and brings no real change to the output.
The derivative of this function is a constant, and the output constantly increases with respect to the input.
If all the activation functions in the neural network are linear functions, the final effective function between the input and output layer turns out to be a linear function, thus destroying the purpose of a multi-layered neural network.
Linear activation functions are generally only used in the output layer.

## Sigmoid Function

#### Mathematical Expression -

![Mathematical Expression](/blog/assets/img/Activation-Functions/sigmoid_equation.png)

![Graph](/blog/assets/img/Activation-Functions/sigmoid.png)

This is a nonlinear function that takes always gives an output between 0 and 1.
For a range of input between approximately -2.5 to 2.5, the derivative is relatively high, the function is rapidly increasing, and it is easy to differentiate between small changes in the values of input. However, outside this range the rate of increase in the function is very low, and becomes almost negligible as we go farther away from 0 on either side.This is known as the vanishing gradient problem. This makes the learning very slow, and thus the model comes inefficient if the input is too high, and the small difference in output for large changes in input values in these areas in the graph results in generation of predictions which have lower accuracy.

Another problem is that the function becomes difficult to optimise for multilayer neural networks as all the output values are positive and range between 0 and 1.
This function is most useful when there are only 2 outputs, or a binary classification model, to find the probability of the outputs between 0 and 1.
It is usually used for the output layer and sometimes the later hidden layers. The softmax function is an extension of the sigmoid function which is used when there are multiple outputs and gives the probability of the most likely output.

## Tanh Function



![Mathematical Expression](/blog/assets/img/Activation-Functions/tanh_equation.png)


![Graph](/blog/assets/img/Activation-Functions/tanh.png)

The tanh function also known as the Tangent Hyperbolic Function, is a shifted version of the sigmoid function. It is a nonlinear function and the output is bounded between -1 and 1. However, even in this function the rate of increase rapidly slows down outside an input range of approximately -2.5 to 2.5.
This function almost always works better than the sigmoid function as the derivative of the graph is steeper, and this really helps tune the weights while performing gradient descent.
This activation function is also used in some hidden layers as the mean of its output values is 0, and this helps to centre the data and make learning easier for the next layers.

## Rectified Linear Unit Function (ReLU)

#### Mathematical Expression - f(x) = max(0,x)

![Graph](/blog/assets/img/Activation-Functions/relu.png)

The ReLU function (or Rectified Linear Unit Function) is the most commonly used activation function in deep learning neural networks.
As shown in the figure above, the output is 0 for all the negative values, and is constantly increasing in a straight line for all positive values.
This function has a range from 0 to infinity. However, it is still a nonlinear function, so we can easily back-propagate the errors and have multiple layers of neurons being activated.

The vanishing gradient problem does not exist here as the derivative is 0 for negative numbers and 1 for positive numbers.
As it involves a mathematical simple function, it is computationally far less expensive than both the tanh and the sigmoid functions. The learning for this function is also much faster when compared to the other activation functions. Also, only a few neurons being activated per epoch makes the overall working of the neural network far more efficient.
The ReLU function is most useful in the hidden layers of the deep neural network and is usually avoided in the input and output layers.

The only issue with this function is the dying ReLU problem. When the input to the activation function is negative, the output is always 0, and the tuning of the weights does not occur during back-propagation in this region. The network thus stops responding to variations in error.
This problem is solved by modifying the ReLU function to a Leaky ReLU function, where the output value on the negative side of the graph is not 0 at all points, but is also a straight line with a very small gradient.


![Leaky ReLU](/blog/assets/img/Activation-Functions/leakyrelu.jpg)

The function can be mathematically represented as :
#### f(x) = max( a*x, x )

Here, ‘a’ may have an extremely small value (like 0.01).

## Conclusion

We have gone through several different activation functions. There is no fixed rule as to which activation function should be used, as it depends on the nature of the neural network, number of neurons, hidden layers, and the several other hyper-parameters of the model.
However, this article gives a rough intuition on the various common activation functions and the situations in which they are commonly used.
