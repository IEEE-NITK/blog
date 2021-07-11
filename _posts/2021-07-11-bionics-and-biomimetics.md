---
layout: post
title: "Bionics, Biomimetics and Robotics"
author_github: Shobuj-Paul
date: 2021-07-11 00:00:00
image: '/assets/img/'
description: ''
tags:
- IEEE NITK
- Diode
- Robotics
- Automation
categories:
- Diode
github_username: 'Shobuj-Paul'
---

Let us get the boring part out of the way and define those three terms in the title. Biomimetics is when we look at how biological systems work and try to replicate the same movements and systems with electromechanical components. Bionics is when we integrate these artificial systems with human bodies. Robotics is when we take mechatronics and try to make it smart. Why do we do that? It could be for a multitude of reasons. To fix disability due to a lost limb is a good example. Or to provide extra strength and support in situations that require heavy work like construction. Or to help patients with paralysis walk and allow them to have a fulfilling life.

The first thing to consider is locomotion in robots, which could be on four-legs (like the Boston Dynamics spot robot), on two-legs (Atlas by Boston Dynamics) or maybe just even hopping on a single leg.

![Quadruped Robot](/blog/assets/img/bionics-and-biomimetics/Four_Legged_Robot.jpg)

All of these motions are usually simulated by simplified versions, which could be easily analysed called "templates". 

Biped walking uses a template called the rimless wheel, and the template for a limb in running motion is a single spring. These templates seem arbitrary but are very useful in analysing the internal dynamics of the systems and approximating them for designing controllers for such systems.

![Rimless Wheel](/blog/assets/img/bionics-and-biomimetics/Rimless_Wheel.png)

The genesis of more intelligent and more powerful sensors helps robot-sensing to become more effective. Another factor is more sophisticated machine learning and deep learning algorithms, which help to make the robots smarter and also helps in computer vision which again improves robot sensing and provides it with a sense of "sight". We can also use computer vision in applications such as mapping and path planning which are very important for robotics because these algorithms are how robots can move around without crashing into objects. Another advancement in bionic technology that is still in its infancy is the neural control of robots.

Soft Robotics is a sub-field that focuses on the use of polymeric "muscles" to create systems that more closely resemble biological systems than just electromechanical contraptions. For example, Micro UAVs can be created using this kind of tech, which resemble insects in nature and can manoeuvre increasingly dangerous environments. There is a lot of research scope in these field as such systems are usually under-actuated and require other methods to work than traditional actuators. Another research area in biomimetics is non-linear control engineering since most jointed systems are non-linear for large angles and require more sophisticated control and state estimation techniques. 

![Control System Diagram](/blog/assets/img/bionics-and-biomimetics/Control_System.png)

## References 
1. Robotics: Mobility MOOC by UPenn on Coursera
2. [J. Oehlke, M. A. Sharbafi, P. Beckerle and A. Seyfarth, "Template-based hopping control of a bio-inspired segmented robotic leg," 2016 6th IEEE International Conference on Biomedical Robotics and Biomechatronics (BioRob), 2016, pp. 35-40, doi: 10.1109/BIOROB.2016.7523595](https://doi.org/10.1109/BIOROB.2016.7523595).