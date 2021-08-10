---
layout: post
title: "Where's the Bot Now?"
author_github: ramyashri1887
date: 2021-08-09 00:00:00
image: '/assets/img/'
description: ''
tags:
- IEEE NITK
- Diode
- Robotics
categories:
- diode
github_username: 'ramyashri1887'
---

Have you ever wondered how life was way before GPS was introduced.I remember taking an OLA ride to a place back in 2013s when google map was not incorporated into the OLA app, and both the driver and I were new to the location and although we were right in front of the location , we didn't know where exactly we were!!!.

We kept driving around the same location for over 30 min only to find that we were at the right location way before. The bill amounted to 1000 and I was devastated. **So answering the question of what we did before GPS was mounted in our devices. We got lost!** Now you get the essence and importance of Localisation. GPS is a life saver but is not the most reliable technology for indoor localisation.By the end of this article you'll know the answers for all the Ws of localisation. Have a basic intuition of different models and filters used for localisation.

## WHAT'S LOCALISATION FIRSTLY ?

Localisation provides an answer to the question "Where's the robot now"?

So by localisation we mean estimating the position and the orientation of an "object" in a given coordinate frame.So essentially it is the building block for all navigation systems.

The "object" could be a robot navigating through an environment or a self-driving car or a drone, it could be anything.

Localisation is often performed given a map of the environment.

### MAPS ARE EVERYWHERE IN ROBOTICS

Maps are required for most of the robotic tasks like path planning and localisation . The map could be represented in various forms as below.

#### 1) Feature based maps

An image based representation using coordinates of known landmarks or features.

![img](/blog/assets/img/localization-robotics/feature-map.png)


#### 2) Occupancy grid maps

An image based representation of the environment in terms of occupied and unoccupied regions. White pixels represent unoccupied regions and black pixels represent occupied regions.

![img](/blog/assets/img/localization-robotics/grid-map.png)

Let's say you are new to the NITK campus and have to navigate to the swimming pool inside the campus. You are given a map of the campus alongside. How do you know where you are exactly with respect to the map ?

You use your vision(Sensor) to perceive the environment around you and compare it with the landmarks provided in the map to find that you are close to the sports complex.You also figure out that to reach the swimming pool you have to walk 3000m forward and take a right and move another 200m/s. You begin to move with a uniform speed of 5m/s.

You have your sensors(Your vision), you have a model with you and hence you can estimate your current location with respect to the sports complex using a simple equation x=vt.

Great job, that's what a robot does, a mobile robot equipped with sensors to monitor its own motion (e.g., wheel encoders and inertial sensors) can compute an estimate of its location relative to where it started if a mathematical model of the motion is available.This is called **DEAD RECKONING**.But dead reckoning is not a truly reliable process due to sensor noises etc.

So , Errors in dead reckoning are corrected using environment perception i.e. by correlating the information from sensors( **Laser range** finders, **ultrasonic sensors** , **Cameras** are most common sensors used for obtaining range and bearing measurements to landmarks) with the map available.

So as we saw the most important components of a localisation problem are the **motion model** describing the motion of the bot using simple kinematics equations and the **sensor model** which is the relationship between the observations from the sensors and the location of the robot in the map.

For instance ,the kinematic equation governing your motion is a simple x=vt. similarly,

the equations governing the motion of the **differential drive robot** are given by

𝑥̇ (𝑡)=(𝑣(𝑡) + 𝛿𝑣(𝑡)) cos(𝜙𝑟 (𝑡))

𝑦̇ (𝑡)=(𝑣(𝑡) + 𝛿𝑣(𝑡)) sin(𝜙𝑟 (𝑡))

𝜙̇ (𝑡) = 𝜔(𝑡) + 𝛿𝜔(𝑡)

We can have various sensor models based on the sensors mounted and the representation of the environment; either feature based map or grid occupancy based map and obtain location estimate based on the landmark observation.

The sensor based positioning includes WiFi based positioning systems, Bluetooth systems,Infrared systems,proximity based or Acoustic based (Sound followers)

The main caveat is ,

## WHO TO LISTEN TO? 

The estimate based on sensor information or the estimate from the kinematic model (motion information)?

The answer is **Bayesian filtering**.

It takes into account the uncertainties involved in both the measurement models and obtains an estimate of the robot location and the associated uncertainty! Extended Kalman filter (EKF) and particle filter provide complaint approximations to Bayesian filtering. Both are recursive probabilistic frameworks.

## EKF vs PARTICLE FILTER

GLOBAL LOCALISATION (initial position of the bot is unknown) cannot be performed using EKF

EKF can't be employed if the representation of the map is an occupancy grid.

EKF assumes Gaussian probability distribution, while Particle filters can handle arbitrary probability distributions.

## THE TAKEAWAY

Localisation is highly relevant in robotics, autonomous driving cars, computer vision, achieving intelligent connectivity,even smartphone requires pose information to make use of certain services

## FURTHER READING

### Implementation of Mapping and localisation Algorithms on ROS

1. [ROS NAVIGATION IN 5 DAYS #3 - Robot Localization](https://www.youtube.com/watch?v=NANc8CkGI2U)
2. [ROS Developers LIVE-Class #49: How to Map & Localize a Robot (ROS)](https://www.youtube.com/watch?v=RknTTpga64s)

### Maths behind Extended Kalman filters ,Particle filters and Monte Carlo localisation Algorithm

1. [Particle Filters and Their Applications](https://web.mit.edu/16.412j/www/html/Advanced%20lectures/Slides/Hsaio_plinval_miller_ParticleFiltersPrint.pdf)
2. [Monte Carlo Localization Algorithm](https://www.mathworks.com/help/nav/ug/monte-carlo-localization-algorithm.html)

## BIBLIOGRAPHY

1. [Robot Localization: An Introduction](https://onlinelibrary.wiley.com/doi/full/10.1002/047134608X.W8318).
2. [Particle Filter and Monte Carlo Localization (Cyrill Stachniss, 2020)](https://www.youtube.com/watch?v=MsYlueVDLI0&amp;list=PLgnQpQtFTOGSeTU35ojkOdsscnenP2Cqx&amp;index=13)
