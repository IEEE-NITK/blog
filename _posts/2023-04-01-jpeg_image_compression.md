---
layout: post
title: "The JPEG Image Compression Algorithm"
author_github: pranavmkoundinya
date: 2023-03-31 00:00:00
description: ''
tags:
- IEEE NITK
- Image Processing
- Compression
- Discrete Cosine Transform
- Huffman Encoding
categories:
- Diode
github_username: 'pranavmkoundinya'
---
# The JPEG Image Compression Algorithm

## Abstract

### Introduction

Have you ever wondered how images, which initially seem to require a large amount of memory space, have surprisingly less space? Consider the following image shown
![image 1](/blog/assets/img/jpeg-image-compression/dog.jpg)

This is a 1920 x 1080 RGB image. Theoretically, this image should require about 6.2MB of memory space. But when we examine its memory contents, we see the following


![image 2](/blog/assets/img/jpeg-image-compression/dog_mem.jpg)

Just 206 KB!!! We see that there is reduction in memory space by a factor of about 30! How is this possible? The answer to this is image compression, a technique that reduces the memory size of an image, with minimal or no loss in quality. One such compression algorithm was developed by the Joint Photographic Experts Group(JPEG), and is famously known as the JPEG Image Compression Algorithm.

Before moving on to the actual algorithm itself, let’s familiarize ourselves with a very few basics of what digital images actually are, how they are represented in the computer, and so on.


### What is an Image?

An image is a 2-dimensional array of numbers, where each array element represents the intensity of the image at that point. Each of the array elements is called a picture element, or a pixel for short. A monochromatic image where the intensity value is now referred to as the gray value, is called a grayscale image. Shown below is a grayscale image of a dog.
![image 3](/blog/assets/img/jpeg-image-compression/B2DBy.jpg)
The following diagram correlates the matrix representation with its digital image counterpart:
![image 4](/blog/assets/img/jpeg-image-compression/mona_lisa.jpg)

The image below depicts 16 gray levels, which can be represented by 4 bits; 0000 being pure


![image 5](/blog/assets/img/jpeg-image-compression/Greyscale-Test-Image.png)
black to 1111 being pure white. Typically, in a computer, grayscale values range between 0 and 255(8 bits).







A color image, on the other hand, has three channels- one each Red, Green and Blue channels of the image, and is thus referred to as an RGB image.

![image 6](/blog/assets/img/jpeg-image-compression/lenna.jfif)
So, now that we’ve acquainted ourselves with the basics of digital images, let’s explore the amazing image compression tool that is JPEG.



### What is JPEG?

JPEG stands for Joint Photographic Experts Group, which was a group of image processing experts that devised a standard for compressing images (ISO).
So, JPEG (or JPG) is not really a file format but rather an image compression standard.

Underlying Assumptions of the JPEG Compression:

The JPEG algorithm is designed specifically for the human eye. It exploits the following biological properties of human sight:
(1) We are more sensitive to the illuminocity of color, rather than the chromatic value of an image, and
(2) We are not particularly sensitive to high-frequency content in images.


The algorithm can be neatly broken up into several stages: There is an input image I, which goes through the following process:
1. A color transform,
2. A 2D discrete cosine transform on 8x8 blocks,
3. A quantization (filtering) stage, 
4. Huffman encoding.
Finally, a compressed image is returned in the .jpg file format. This format contains the compressed image as well as information that is needed to uncompressed, with other information to allow for re expanding the image.
#Process of JPEG compression:
Firstly, we convert the R, G, B color format to Y, Cb, Cr(Brightness, Color Blueness, Color Redness) format. Some colors are more sensitive to human eyes and thus are high-frequency colors. Some colors of chromium compounds like Cb and Cr are less sensitive to human eyes thus can be ignored. Then we reduce the size of pixels in downsampling. We divide our image into 8x8 pixels and perform forward DCT(Discrete Cosine Transformation). Then, we perform quantization using quantum tables and we compress our data using various encoding methods like run-length encoding and Huffman encoding. 
In the second stage, we decompress our data. It involves decoding where we decode our data, and we again de-quantize our data by referring to the quantization table. Then we perform Inverse DCT and upsampling to convert it into its original pixels and finally, color transformation takes place to convert the image into its original color format. 

### JPEG Image Compression Algorithm:
![image 7](/blog/assets/img/jpeg-image-compression/chart.png)
1. Splitting – 
We split our image into blocks of 8x8 blocks. It forms a total of 64 blocks in which each block is referred to as 1 pixel. 
2. Color Space Transform – 
In this phase, we convert the RGB image to Y, Cb, Cr model. Here Y stands for brightness, Cb for color blueness, and Cr for color redness. We transform the image into chromium colors as these are less sensitive to human eyes, and therefore can be removed. 
3. Apply DCT – 
We apply Discrete Cosine Transform(DCT) on each block. The DCT represents an image as a sum of sinusoids of varying magnitudes and frequencies. This allows us to represent an image in the frequency domain(whereas earlier, it was represented in the spatial domain). 
4. Quantization – 
In the Quantization process, we quantize our data using the quantization table. 
5. Serialization – 
In serialization, we perform the zig-zag scanning pattern to exploit redundancy. 
6. Vectoring – 
We apply DPCM (Differential Pulse Code Modeling) on DC elements. DC elements are used to define the strength of colors. 
7. Encoding – 
In the last stage, we encode the image using either run-length encoding or Huffman encoding. The main aim is to convert the image into text and by applying any encoding we convert it into binary form (0, 1) to compress the data by exploiting redundancy in data values. 

### Is the JPEG Compression limitless?
The JPEG Compression is, unfortunately, a lossy compression algorithm i.e, the more we compress it, the more the quality worsens, as is evident in the figure below. 
![image 8](/blog/assets/img/jpeg-image-compression/quality.jpg)
There are other alternatives to JPEG, such as PNG(Portable Network Graphics), which supports lossless compression. There is always the Vector Graphics, which supports scaling of the image by any factor, without any loss in the quality. Unlike normal images which are represented as matrices of pixels, the components of vector graphics images are represented by mathematical equations. Nevertheless, JPEG image compression was one of the first image compression techniques developed, and continues to be utilized extensively. 
Image compression has been instrumental in facilitating the transmission of images by space probes during interplanetary explorations, instantaneous transmission of images in modern communication media, and so on. 