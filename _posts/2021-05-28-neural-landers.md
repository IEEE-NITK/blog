---
layout: post
title: "Neural Landers"
date: 2021-05-28 00:00:00
image: '/assets/img/'
description: ""
tags:
- IEEE NITK
- Piston
categories:
- Piston
github_username: 'viba-r-udupa'
---
> “When I meet God, I am going to ask him two questions: Why relativity? And why turbulence? I really believe he will have an answer for the first."
-Horace Lamb

Landing any aircraft smoothly is difficult. It is an energy-management challenge. The aircraft must make the transition from a vast open sky to a relatively constricted environment. It is subject to strong crosswinds increasing the turbulence. There is complex turbulence created as the airflow from the wing/rotor bounces off and interacts with the ground. We do not have a good enough understanding of turbulence yet, and pilots should have excellent judgment skills to make a smooth landing. Coming to autonomous flight, it is a very challenging task to develop a system to account for the turbulence and make the right adjustments to land smoothly.

## Understanding Ground Effects

The ground effect is a phenomenon that causes reduced induced drag when hovering close to the ground.  Below is an image of a section of a wing.

![img-1](/blog/assets/img/neural-landers/image1.png)

A wing generates lift by deflecting incoming airflow downward. According to Bernoulli's principle, the region above the airfoil has high-speed winds at low pressure compared to the low speed-high pressure winds below the airfoil. This difference in pressure causes lift. The high-pressure air below the wing tries to rush to the low-pressure region above the wing, but the wing comes in between, obstructing it, except at the wingtips, which causes the airflow below the wings to spill around the wingtips above the wings, forming a twisting vortex. This can be visualized in the image below.

![img-2](/blog/assets/img/neural-landers/image2.png)

The formation of the vortices increases the downwash. The lift generated is perpendicular to the direction of relative wind flow. And with increased downwash, the lift vector tilts backward, and its horizontal component is called induced drag, as seen in the image below. This reduces the net lift force and increases the drag on the aircraft.

![img-3](/blog/assets/img/neural-landers/image3.png)

When an aircraft is closer to the ground, the downwash is restricted as the ground is a rigid surface. As a result, even wingtip vortices are restricted. This causes the airflow below the wing to be nearly horizontal, and the lift vector now is not much tilted back. As a result, the induced drag is reduced, which means less power is required to maintain the same airspeed. However, due to an increase in lift, cushioning effect is experienced by the aircraft. The aircraft tends to float and takes longer to land. This effect is noticeable when the aircraft is at a height equal to its wingspan.

![img-4](/blog/assets/img/neural-landers/image4.png)

In fixed-wing aircraft, a solution is to have Winglets, which are vertical extensions of the wingtips to reduce the vortices and the associated induced drag. Below image shows the effects of winglets on vortices.

![img-5](/blog/assets/img/neural-landers/image5.png)

However, if we talk about rotorcraft, using winglets is not a very efficient idea. This is because the propellers are rotating at a very high RPM. The winglet would be acting as a cantilever beam, which would cause instability and material failure due to fatigue. The ground effect in helicopters is shown in the image below and is more complicated for drones.

![img-6](/blog/assets/img/neural-landers/image6.png)

## Neural Landers

Due to complex interactions of the rotors and the wind flow with the grounds, which can cause flight instability, the automatic landing of a drone is risky. Typically drones wobble and slowly move towards the dock until power is cut off and then drop the remaining distance to the ground, which is about 15-20cm of free fall.

![img-7](/blog/assets/img/neural-landers/image7.png)

Unmanned Aerial Vehicles require high precision control of aircraft positions during takeoff and landing. Artificial Intelligence experts from Caltech’s center for autonomous systems and technologies have used Deep Neural Networks(DNN) to develop a system that aids the UAVs to learn how to land efficiently.

The system created is a learning-based controller that tracks the position and speed of the drone and modifies its landing trajectory and rotor speed accordingly to achieve the smoothest possible landing. The existing systems are mathematical models based on steady flow assumption, while it is never the case in practice. Integral and adaptive control methods give delayed feedback.

To incorporate a Machine Learning approach to the system's development, a lot of data is required, for which, they used a giant array of 1296 computer fans to generate different sorts of winds and repeatedly landed the drone to study the controllers' performance. Neural networks are a series of algorithms that detect underlying relationships between data. DNN is used as a feedforward prediction term in the controller; that is, the disturbances are measured and accounted for before they have time to affect the system. The input for the neural network is knowledge about the drone's location, velocities, and angular rate, along with the landing location. The output is the additional force required to make the drone land smoothly at the desired location. The result can sometimes be widely varying predictions or condition shifts. To compensate for this, spectral normalization of data is used. The output is used to separately control each of the rotors to adjust the thrust and correct the trajectory to make a smooth landing. Below is an image that was taken during the testing of the neural lander.

![img-8](/blog/assets/img/neural-landers/image8.png)

We know that landing is the trickiest maneuver for any aircraft. Even more so for vertical take-off and landing(VTOL) aircraft as apart from ground effects, the side winds can make it difficult to control its orientation perfectly.  The deep neural controller will significantly contribute to solving these challenges. Future uses of these could be to effectively incorporate this controller into the aircraft to make landings smoother and can be used for 3D mapping, search-rescue missions, and delivery services.
