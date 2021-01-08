layout: post
title: "Why GraphQL is a big thing"
author_github: dharmicksai
date: 2021-01-07 19:00:00
image: '/assets/img/'
description: 'Neural Style Transfer'
tags:
- IEEE NITK
- CompSoc
- Style Transfer
- Deep Learning
- Unsupervised Learning
categories:
- Compsoc
github_username: 'dharmicksai'
---
# Neural Style Transfer

Neural Style Transfer is the problem of applying the style of an image/painting onto a content image. For Humans the process of painting is seamless . In this blog we will look into the loss functions which capture style representations, feed forward networks which produces styled images given style and contnent image, we will look into style representation and how this can be used to produce new encodings for unseen paintings

## Style and Content loss

As Loss function captures the objective of a model, we shall first look into style and content loss functions. When Training CNN model for object classification ,each layer captures certain featrures of the input image .the lower layers capture low lewel information whereas the higher level layers capture the  high-level content in terms of objects and their arrangement in the input image but do not constrain the exact pixel values of the reconstruction. So we can say that the activations of Higher layers contain information about content of an input image. Gram Matrix of a layer contains the dot product between different channel activativations of a given layer this contains information on corelation of features extracted by different channels of a layer. So we use Gram matrix of lower layers as style representation of a input image.

Style Representation

![Style Representation from Gats et al](/blog/assets/img/Neural-Style-Transfer/style_rep.png) 

Here G<sub>ij</sub><sup>l</sup> is the ij<sup>th</sup> entry in the gram matrix of Layer l. F<sub>i</sub><sup>l</sup> is the activations of i<sup>th</sup> channel in l<sup>th</sup> layer. 
We use the pre traind VGG16 Network for activations

![Style Reconstruction from Gats et al](/blog/assets/img/Neural-Style-Transfer/VGG_style.png)

We consider the content representation of content image to bo the target for content loss and we consider the style representation of style image as target for style loss.

Content Loss given P<sup>l</sup> is target content activation of layer l:

![content loss from Gats et al](/blog/assets/img/Neural-Style-Transfer/content_Loss.png)

Style loss given A<sup>l</sup> is target style representationof layer l:

![style loss per layer from Gats et al](/blog/assets/img/Neural-Style-Transfer/style_loss1.png)

![Total style loss from Gats et al](/blog/assets/img/Neural-Style-Transfer/style_loss2.png)

Total Loss given content representation p, style representation a , styled image representation x: 

![Total loss from Gats et al](/blog/assets/img/Neural-Style-Transfer/Total_Loss.png)

## Image Transformation Network

![Image Transformation Network from Jonson et al](/blog/assets/img/Neural-Style-Transfer/Feed_Forward.png)

Here the image transformation network learns to map the content image to the style of the painting image, using this network we can generate images of an particular style. An image transformation network f<sub>W</sub> and a loss network φ that is used to define several loss functions `1, . . . , `k. The image transformation network is a deep residual convolutional neural network parameterized by weights W; it transforms input images x into output images ˆy via the mapping ˆy = f<sub>W</sub> (x) , by convention x is same as content image. Each loss function computes a scalar value l<sub>i</sub>(ˆy, y<sub>i</sub>) measuring the difference between the output image ˆy and a target image y . 

## Conditional Instance normalisation

We can see that many paintings share some common features like brush strokes etc , conditional Instance normalisation helps us to encode style into a emmbeding and a common image transformation network for multiple styles. To understand about Instance Normalisation please look at this blog [link](https://medium.com/techspace-usict/normalization-techniques-in-deep-neural-networks-9121bf100d8). We see in this [paper](https://arxiv.org/pdf/1607.08022.pdf) that Instance Normalisation is better than Batch Normalisation in Image Transformation Network. For using a single Image Transformation network for multiple styles ,we see the work in this [paper](https://arxiv.org/pdf/1610.07629.pdf), where they found a surprising fact about role of normalisation in Transformation network: to model a style, it is sufficient to specialize scaling and shifting parameters after normalization to each specific style. In other words, all convolutional weights of a style transfer network can be shared across many styles, and it is sufficient to tune scaling and shifting parameters for an affine transformation after normalization for each style.
 
This approach is conditional instance normalization. The goal of the procedure is transform a layer’s activations x into a normalized activation z specific to painting style s. Building off the instance normalization technique proposed in [Ulyanov et al. (2016b)](https://arxiv.org/pdf/1607.08022.pdf),For each style we have a different γ<sub>s</sub> and β<sub>s</sub>:

![Conditional Instance Normalisation](/blog/assets/img/Neural-Style-Transfer/Instance_Normalisation.png) where µ and σ are x’s mean and standard deviation.

So for each style we can train γ<sub>s</sub> and β<sub>s</sub> and keep the weights of Image Transformation net constant.

![Applying Instance Normalisation](/blog/assets/img/Neural-Style-Transfer/Normalisation.png)

The Image Transformation Network Details given in this [paper](https://arxiv.org/pdf/1610.07629.pdf) For implimenting Multi style Transfer

![Image Transformation Network Details](/blog/assets/img/Neural-Style-Transfer/Network_Details.png)

## References
- [A Neural Algorithm of Artistic Style](https://arxiv.org/abs/1508.06576)
- [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/abs/1603.08155)
- [Instance Normalization: The Missing Ingredient for Fast Stylization](https://arxiv.org/abs/1607.08022)
- [A Learned Representation For Artistic Style](https://arxiv.org/abs/1610.07629)
- [Normalization Techniques in Deep Neural Networks](https://medium.com/techspace-usict/normalization-techniques-in-deep-neural-networks-9121bf100d8)


