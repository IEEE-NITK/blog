---
layout: post
title: "Introduction to Steganography"
author_github: Shash0501
date: 2023-03-31 00:00:00
image: '/assets/img/'
description: 'An introduction to Steganographic techniques'
tags:
- IEEE NITK
- CompSoc
categories:
- CompSoc
github_username: 'Shash0501'
---

# Steganography

You want to send a secret message to your friend, and you don't want anyone else to know about it. Then what you can do is encode your message using specific rules and make the message meaningless. However, a third person can still easily judge that some secret communication is happening.
This is where steganography comes into the picture, which enables us to hide data in plain sight and a third party person can't figure out if a secret communication is happening.
Formally 
Steganography is the art and science of embedding secret messages in cover messages so that no one suspects the message's existence apart from the sender and intended recipient. 

Depending on the nature of the cover object (actual object in which confidential data is embedded), steganography can be divided into five types:

- Text Steganography
- Image Steganography
- Video Steganography
- Audio Steganography
- Network Steganography

<br>

### Text Steganography 

Text Steganography is hiding information inside the text files. It involves things like changing the format of existing text, changing words within a text, generating random character sequences or using context-free grammar to generate readable texts.

### Image Steganography

Hiding the data by taking the cover object as the image is known as image steganography. In digital steganography, images are widely used cover sources because there are many bits present in the digital representation of an image. There are a lot of ways to hide information inside an image. The most famous approach being Least Significant Bit Insertion. 

### Audio Steganography

In audio steganography, the secret message is embedded into an audio signal which alters the binary sequence of the corresponding audio file. Hiding secret messages in digital sound is much more complex compared to the other steganographic techniques.

### Video Steganography

In Video Steganography, you can hide kind of data into digital video format. The advantage of this type is a large amount of data can be hidden inside and the fact that it is a moving stream of images and sounds. You can think of this as the combination of Image Steganography and Audio Steganography. Two main classes of Video Steganography include:
Embedding data in uncompressed raw video and compressing it later
Embedding data directly into the compressed data stream

### Network Steganography

Network Steganography is a technique that uses standard network protocols (the header field, the payload field or both) to hide a secret message. TCP/IP protocol suite has been a potential target for network steganography from the very beginning.



## CHARACTERISTICS OF STEGANOGRAPHIC TECHNIQUES

In steganography, the message to be hidden inside the cover–media must consider the following features.

**Perceptual Transparency**: Perceptual transparency is an essential feature of steganography. Each cover media has a certain information hiding capacity. If more information or data is hidden inside the cover, then it results in degradation of the cover–media. As a result, the stego–media and cover–media will appear to be different. If the attacker notices this distortion, then our steganographic technique fails, and there is the possibility that our original message can be extracted or damaged by the attacker.

**Hiding Capacity**: This feature deals with the size of information that can be hidden inside the cover file. A larger hiding capacity allows the use of a small cover and thus reduces the bandwidth required to transmit the stego–media. 

**Robustness**: Robustness is the ability of the hidden message to remain undamaged even if the stego–media undergoes transformation, sharpening, linear and non-linear filtering, scaling and blurring, cropping and various other techniques.

**Tamper–resistance**: This feature is very important of all the features. If the attacker successfully destroys the steganographic technique, then the tamper–resistance property makes it difficult for the attacker or pirates to alter or damage the original data.



### BASIC STEGANOGRAPHIC MODEL

![image 1](/blog/assets/img/introduction-to-steganography/1.png)

A basic steganographic model has a cover file(X) and secret message(M), which are input for the steganographic encoder. Steganographic Encoder function, f(X,M,K) hides the secret message into this cover file. The final output looks very similar to your cover file, with no visible changes. This completes encoding. We have to feed the Stego Object (Output) into a Steganographic Decoder to get back the secret message.

Let's take one example of steganography (image).



**LSB Steganography** ( Least Significant Bit Steganography ) 

We first need to have a basic idea about a digital 2D image to understand this.
Each image is made up of an array of pixels, and each pixel is one colour; however, each pixel groups together to form a new colour. I will consider the RGB colour model where red, green and blue light are combined to reproduce a broad array of colours and each colour is represented by using a binary code.

For a binary number, we have a most significant bit (Leftmost bit), and least significant bit (Rightmost bit) and changing the MSB will largely impact the binary number but changing the LSB doesn't have that big of an impact. And we use this property of a binary number in LSB steganography.

LSB Steganography is an image steganography technique in which messages are hidden inside an image by replacing each pixel's least significant bit with the bits of the message to be hidden. For example, suppose we have an RGB image with a size of 200 x 200 pixels. In that case, that means that we have 120,000 colour values to be used as cover values for the secret message (200:width x 200:height x 3:R, G, B). Then if we use only one bit per colour channel for hiding the message, we have a hiding capacity of 120,000 bits or 15,000 bytes. If we use 2 bits per colour channel for hiding the message, we have 30,000 bytes.


Suppose we want to insert the letter "A" into an image 
And the binary representation of A is 1000001
I would need 7 bytes to insert the value of "A", and hence I would need three pixels (9 bytes) to encode "A". 

![image 2](/blog/assets/img/introduction-to-steganography/2.png)

Even after changing the 7 bits of the original image, there would be a negligible difference in the image, and hence we are successful in hiding the message without altering the image.
The below code is a simple way to exactly replicate the above process.

## Encoding 

```python
def Encode(source, message, destination):
    img = Image.open(source, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n
    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)
    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")
    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1
        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(destination)
        print("Image Encoded Successfully")
```

## Decoding 

```python
def Decode(src):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n
    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])
    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]
    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Hidden Message:", message[:-5])
    else:
        print("No Hidden Message Found")
```