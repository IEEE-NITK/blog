---
layout: post
title: "Introduction to 3D Biometrics"
author_github: gayatri1705
date: 2022-07-21 00:00:00
description: 'Biometrics is the science of recognizing the identity of a person based on the physical or behavioral attributes of the individual such as the face, fingerprints, etc. This blog gives more insight about 3D biometrics.'
tags:
- IEEE NITK
- Blog
- 3D Biometrics
categories:
- Diode
github_username: 'gayatri1705'
---

# 3D Biometrics

## Abstract 

With the development in technology, automatic personal authentication is being used in many fields such as security, forensics, banking, etc. Many kinds of authentications techniques are available based on the different biometric characteristics. Mostly all the developed techniques use 2d Biometrics. Recently, the method of 3D biometrics for the use of authentication has been in use. Some of them are the face, palm, and fingerprint recognition.

## What is 3D Biometrics?
Biometrics is the science of identifying a person based on the physical features of a person. There are 2 types of biometrics: 2D and 3D. In 2D biometrics, the data acquired is 2D. 2D data does not construct a depth map instead, it captures a 2D image and stores it as the data. In 3D biometrics, a detailed 3D cloud map of the target features is made. 

The newly developed 3D biometrics could overcome the limitations existing in 2D. Compared to 2D; much more geometric information can be contained in 3D, which can substantially improve the accuracy. For this reason, many researchers have turned their attention to this newly developing field.

A general flow diagram for 3D biometrics is shown:

![IMG 1](https://user-images.githubusercontent.com/78913478/166979211-82a499f8-77c3-4b21-8b39-91f79e4baf1a.png)


The workflow can be split up into 2 phases and 5 stages.

In the first phase, the 3D data is acquired and pre-processed to obtain clean 3D faces. Then the acquired data is processed to find features that could be used to differentiate faces. This is done by extraction algorithms. The features are then stored in each feature database. Then comes the testing phase. Where the acquisition, pre-processing, and extraction happened, were almost similar to the first stage. Next is the feature matching stage, where the features are matched with the feature database. If the matching percentage is sufficiently high, then we say that the face is matched.

## 3D face acquisition
For the acquisition of face samples, special hardware is required. This hardware can be classified into 2 parts; Active and Passive Systems according to the technology used.

The active system emits nonvisible infrared light beams and measures their reflection. The 3D face can be constructed using this reflected data. According to the different illumination methods, the active system can be further classified into triangular or structured light-based.

In the triangular method, the emitting and receiving angles are measured. Using that data, the exact point of reflection is calculated. Using this process, a precise map is formed with many points. This is a high-precision method, but the only disadvantage is that it is slow. Therefore, it would be required for the target person to hold still for a minute. Therefore, this method can’t be used for video authentication.
 
Compared to triangular systems, structured light-based systems are more popular on consumer levels. In this method, a system emits a light grid. It then measures the deformation of that light grid to measure the surface structure. This method is much faster than the triangular method but is not as accurate as compared to triangular systems. 

## Preprocessing
The acquired data cannot be directly used for the authentication, because there are many extra features such as hair, ear, and eyeglasses. When we humans want to identify each other, these extra features and jewelry can be helpful. Although these features would be helpful for humans to identify each other, they would serve as a distraction or mislead the 3D face recognition system and hence should be removed. This is done through pre-processing.  

The first step of pre-processing is to detect the correct position and orientation of the human face. Different algorithms are used to turn the face to directly face the camera axis. Then clearly identifiable features such as the nose, and eyes, are used to isolate the human face area out of these distracting features, this operation is called segmentation.

There are different model formats such as depth image, point cloud, and mesh.

![IMG 2](https://user-images.githubusercontent.com/78913478/166979331-d3338e88-a975-41db-b399-48c571ebd913.png)

## Feature extraction, feature database, and feature matching
One of the most straightforward way of feature extraction is to take the entire face as a single feature vector. This is called the Global approach. In this approach, the entire face is stored in the database. In the matching stage, the target faces are compared with the database statistical classification functions. 

Apart from the Global approach, the other one is called the Component-based approach. In this approach, important facial characteristics such as the eyes, and nose are extracted. These recognizable features are stored in the database. During the matching process, the features on the target face are compared with the database. 

There are also hybrid approaches that combine both these methods to provide greater accuracy and security. 


## Newer Technologies 

Even as the methods of these biometric methods are still developing, a new method of 3D biometric using finger veins is being developed. Such type of authentication which uses unique anatomical features is soon replacing tradition methods of security. 

Although this new technique involving finger veins is being developed, it is based on 3D biometrics. The addition data and depth given by 3D images will make it more difficult to fake an identity. 

To accomplish this 3D biometrics involving finger veins, a new method called photoacoustic tomography, an imaging technique that combines light and sound id being developed. In this method, a light source is used to illuminate the target. When the light hits the target surface, it creates a unique sound. This sound is then detected by a sensor, then a 3D image is constructed using this data. 

## Resources and links

- [3D Biometric Authentication Based on Finger Veins Almost Impossible to Fool](https://www.optica.org/en-us/about/newsroom/news_releases/2020/3d_biometric_authentication_based_on_finger_veins/)
- [3D face recognition: a survey](https://hcis-journal.springeropen.com/articles/10.1186/s13673-018-0157-2#Sec1)