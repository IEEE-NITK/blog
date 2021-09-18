---
layout: post
title: "Brain-Machine Interfaces"
author_github: achintya-k-n
date: 2021-08-09 00:00:00
image: '/assets/img/'
description: ''
tags:
- IEEE NITK
- Diode
- Medical Electronics
categories:
- diode
github_username: 'achintya-k-n'
use_math: true
---
# Brain-Machine Interfaces

With Artificial Intelligence and assisted technologies improving as rapidly as they are, many scientists and tech pioneers feel that AI might become 'better' than humans sooner than we think (some even say that they can take over the world!). But would that be the case if our minds could directly connect with AI, robots and other minds? Maybe we need to become cyborgs to stay relevant in an AI ruled age and this is exactly what Brain-Machine Interfaces hope to bring to the table.

As the name suggests, Brain-Machine Interfaces (also called Brain-Computer Interfaces) are devices that enable users to interact with computers by means of brain activity (in layman terms, you can do stuff just by thinking about it). BCIs are capable of a lot of things that would otherwise seem impossible to say a common man of the 20th century. For instance, they can replace lost functions (speaking, moving), they can restore functionality in organs by stimulating certain nerves and they can also enhance and improve general human physical capabilities (better reflexes and awareness). 
So when did this, seemingly revolutionary technology come to the fore? 
Research and innovations in this field date back as far as 1924 when Hans Berger discovered electrical signals being emitted from the brain and the subsequent development of the EEG as a result. Berger analyzed the interrelation of his EEG wave diagrams with some brain disorders and found that EEG opened up completely new possibilities for research on human brain activity. Not only were opportunities opened up in the field of research but also early diagnosis of various disorders and diseases which were earlier thought to be 'untreatable and incomprehensible' was possible now. 

Now, let us try to define a proper, rigid classification basis for BCIs to better understand the content that follows,
Mainly, BCIs have a broad classification into 3 categories, namely,
#### a) Invasive BCI
This kind of BCI require surgery to implant various electrodes and sensors in the brain (yes, way inside the skull). This provides great accuracy in readings however the disadvantages are obviously the side-effects of such surgerical procedures. In some cases, scar tissues can form as well, which defeats the whole purpose of invasive BCI by weakening the signals.
#### b) Partially Invasive BCI
These BCIs also require surgery and implants inside the skull but these reside outside the grey matter in the brain. Risk of scar tissue formation is lesser but this is at the cost of reduced accuracy but is still better than non-invasive BCI where the bone tissue interferes greatly with the brain signals.
#### c) Non-invasive BCI
This is the safest type of BCI with no scary implants in the brain but of course, accuracy is greatly reduced. Most research and publications are based on these BCI. They have relatively poor spatial resolution and cannot effectively use higher-frequency signals because the skull dampens signals, dispersing and blurring the electromagnetic waves created by the neurons. The best BCI for a particular user depends on various parameters.

There are many kinds of BCIs out there but most of them grapple with both or either of these 2 questions namely: How do I recieve relevant information from the brain? and How do I send relevant information to the brain? Now, this is basically what neurons do and the BCI industry wants to somehow replicate this artificially, which is far easier said than done. There are roughly 100 billion neurons in the brain and 50 times more glial cells (they hold the nerves together and aid neurotransmission and maintain the chemical stability of the brain) and all these neurons are connected to many other neurons so it is safe to say that 'complicated' doesn't even begin to describe it. 
![img](/blog/assets/img/brain-computer-interface/img8.jpg)

 So how do BCIs tackle (or hope to tackle) all of this? Well, they do the best that can be done with the tools available today. Firstly, let us look at some of the tools BCIs use and their basic features.
### 1) fMRIs
Functional MRIs are devices which use magnetic fields to generate images concerning blood flow. Blood flow indicates which parts of the brain is recieving blood and some superficial analyses can be done on the brain and its activities. 
![img](/blog/assets/img/brain-computer-interface/img3.jpg)
However, the resolution of fMRIs is pretty low (we can't know where exactly as fMRIs are taken of the entire brain). Nevertheless, since fMRIs have good scale and have been instrumental in understanding which parts of the brain influence what kind of functions.
### 2) EEGs
EEG (electroencaphalography) basically puts electrodes to your head (specifically, on the scalp) and records the electrical activity in various regions of the brain and is very useful in determining how the brain uses electrical signals to transmit data. 
![img](/blog/assets/img/brain-computer-interface/img4.jpg)
Though this has better resolution than fMRIs, it is still very low. Considering the complexity of the brain, it barely scratches the surface in terms of resolution but it does help us understand the electrical patterns of the brain for carrying out certain tasks like, 
![img](/blog/assets/img/brain-computer-interface/img4a.jpg)
### 3) ECoG
In ECoG (electrocorticography), electrodes are inserted under the scalp and similar circuits as EEG are used for the detection of electrical activity in the brain. This has much better resolution but it is kind of invasive to the user (it might seem very invasive but this is just an incision on the scalp, the following ones are much worse).
![img](/blog/assets/img/brain-computer-interface/img5.jpg)
### 4) Low Field Potential
In LFPs, thin needle-like electrodes (made of silicon wafers or other materials from the integrated circuits industry) are stuck 1 or 2 mm in the cortex (cortex makes up for 80% of the brain, it is the whole jelly-like squiggly mass which makes up most of your brain).Though this has incredibly high resolution, it is horrible when it comes to scale and invasiveness. There have been further innovations in this fields, for example, Multielectrode arrays which use the same idea as LFPs but 100 electrodes are situated next to one another so this improves the scale of the device. These electrodes are of course, very thin and sharp as they are of the size and scale of cells.
![img](/blog/assets/img/brain-computer-interface/img6.jpg)
### 5) Single-Unit Recording
Single-Unit Recording also uses thin electrodes but their tips are ultra thin and the resistance values are made to be super high. Thus it will only achieve connection when it gets really close to a neuron and other noise won't be heard due to the high resistance wall. This gives the best resolution possible however it is very invasive and scale is practically null. Some new designs of the SUR take it to the next level using a technique called Patch Clamp where it clamps on to a membrane patch of the neuron using a glass tip which is located at the tip of the needle instead of an electrode (this also takes advantage of the high resistance value of the patch clamp tip).
![img](/blog/assets/img/brain-computer-interface/img7.png)

This can give us much better readings and values. Also, since it physically touches the neuron, this can be improvised to stimulate the neuron.
There are also other designs like Sharp Electrode Recording which pierces the neuron and the tip is so sharp that, a membrane forms around this tip and this allows us to effectively read the voltage values on the neuron and also stimulate it as and when required.

That was about it on the tools used in BCIs, there are various BCIs out there today, so let's check out some of them,

## BCI with LOCOMOTORY OUTPUTS
One of the most exciting application of these tools is to implement a BCI device would be those which can be controlled by the user's thoughts. Firstly, let's look at those controlled by the Motor Cortex which has huge implications especially for disabled people. Now, bringing about movement in people who can't move is a very challenging task. First, the brain signal of such a person will have to be interpreted and then carried out physically. For this, the user will have to be trained to visualize moving their appendages as vividly as possible and later our device needs to incorporate Machine Learning algorithms to successfully learn to relate these brain signals to that of arm or leg movement. This algorithm can then be integrated with a software and connected to a robotic arm which can carry out these functions for the user. Similar concepts can be used to enable disabled people to type, use computers, write, etc.. (provided such an algorithm can be developed successfully)
Check out this video where a quadriplegic woman uses BCIs to carry out locomotory tasks: 

<iframe width="560" height="315" src="https://www.youtube.com/embed/QRt8QCx3BCo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## BCI with SENSORY INPUTS
These can really be a revolutionary innovation for people whose senses have been impaired. One of the most basic and primitive forms of these BCIs are Cochlear Implants. Cochlea is an essential part of the hearing system in mammals. Now, for an average person, sound waves enter the ear and pass through the eardrums and several other pathways (Cochlea being one of them) and then pass on to the Auditory Nerves which recieve an electrical input of these sound waves. In some cases, these hearing pathways might be damaged whereas the Auditory nerve might still be intact, in such a scenario, the Cochlear implants can do the 'hearing' for the subject and output electrical signals into the auditory nerves, enabling the subject to hear again to some extent. Similar processes can be carried out to create artificial eyes but it is far more challenging since the visual system is much more sophisticated but it is definitely possible to do so by using 2 camera-like devices as eyes in theory.

A more detailed flowchart for carrying out these algorithms can be seen below,
![img](/blog/assets/img/brain-computer-interface/img1.jpeg)

As you can see, AI/ML and Signal Processing plays a huge role in this and can be used to solve many problems in this domain but the problems are very, well, problematic. For instance, there will be loads of noise (unless you are okay with patch-clamping) for proper signal processing and creating ML models to understand brain waves amidst all of the noise (remember, our brain does a whole lot of things simultaneously which also becomes part of the noise) is a challenge of its own.

## Convolutional Neural Networks and BCIs
CNN is a type of AI neural network based on the visual cortex of the mammalian brain. It has the capacity to learn the appropriate features from the input data automatically by optimizing the weight parameters of each filter through the forward and backward propagation steps in order to minimize the classification error. Using such Deep learning frameworks for BCI applications is advantageous in many ways, it requires minimal pre-processing as optimal settings are learned automatically, feature extraction and classification are integrated into a single structure and optimized automatically. Moreover, Convolutions are integrated in a slide-show manner which can retain temporal information while extracting features from the CNN. However, it is still very difficult to find reliable patterns in brain wave functions due to reasons mentioned before (the brain is the biggest baddest multitasker out there making pattern recognition hugely complicated).
![img](/blog/assets/img/brain-computer-interface/img2.jpeg)

Thus, it is safe to conclude that BCIs have a long way to go but decent inroads have been made in recent times which can surely be built upon in the near future (well, they are already being worked on..eg. Neuralink.. to know more, click [here](https://en.wikipedia.org/wiki/Neuralink)).

## References:
- [Brain-Computer Interface](https://en.wikipedia.org/wiki/Brain%E2%80%93computer_interface)
- [This Is a Computer on Your Brain](https://www.wired.com/2006/07/this-is-a-computer-on-your-brain/)
- [Neuralink and the Brain’s Magical Future](https://waitbutwhy.com/2017/04/neuralink.html#part3)
- [A Beginner's Guide to Brain-Computer Interfaces and CNNs](https://towardsdatascience.com/a-beginners-guide-to-brain-computer-interface-and-convolutional-neural-networks-9f35bd4af948)
- [How Brain-computer Interfaces Work](https://computer.howstuffworks.com/brain-computer-interface.htm)