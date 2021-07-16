---
layout: post
title: "The Elliptic Curve Cryptography"
author_github: rak108
date: 2021-01-04 21:46:44
image: '/assets/img/rakshitavaradarajan.jpg'
description: 'An insight into the Powerful Public-Key Cryptography Algorithm using Elliptic Curves.'
tags:
- IEEE NITK
- Theoretical Computer Science
- ECC
- Cryptography
categories:
- CompSoc
github_username: 'rak108'
use_math: true
---

## Introduction

**Elliptic Curve Cryptography (ECC)** is one of today's most powerful but least understood public-key encryption methods which is found upon the mathematical concept of elliptic curves. Compared to other algorithms serving the same purpose, ECC allows for **smaller, faster and more efficient keys while providing the same amount of security**. Elliptic curves cryptosystems are applicable for encryption, digital signatures, pseudo-random generators and other tasks.

## Public-Key Cryptography

The previous paragraph mentions *public-key cryptography*. This concept (also known as asymmetric key encryption scheme) is a required foundation to understand the ECC concept. 

Modern Cryptography is based on the idea that rather than having a single key performing both encryption and decryption, a pair of keys can be used; one is the public key known to all and the other is the private key, which is kept secret. The keys are designed and generated in a way that they act complementary to one another. Using this system, the sender can encrypt their message using the receiver's public key, and only the receiver who has the respective private key can decrypt the messages. This efficient design was a great step in resolving the issue of compromise of a single shared key, while also enabling authentication of the encrypted messages by the public-key owner.

![Asymmetric Key Encryption Scheme](/blog/assets/img/ecc/PublicPrivateKeyEncryption.png)


The key-pairs are generated while taking into consideration **"Trapdoor Functions"**, which are functions that are easy to compute in one direction, but has a special piece of information or secret (called “trapdoor”) which is required in order to compute the inverse (or reverse the computation). For example, the fundamental concept of the very widely used RSA algorithm is that while it is easy to multiply two prime numbers, it is difficult to perform prime factorization on this product to obtain the component primes. The greater the difference of ease between computing the Trapdoor Function & the difficulty of reversing Trapdoor functions, the more computational effort will be required to derive the private key from the public key and thus, the more secure the cryptographic system. 

## Why ECC?

Algorithms such as RSA and Diffie-Hellman are not very sustainable in the long term. This is because factoring is not the hardest problem out there. Specialized algorithms, which were devised to solely tackle the problem of prime factorization while being faster and less computationally intensive than the naive approach, get more efficient as the size of the number being factored gets larger. Thus, as the numbers get larger, the difference between computing the product of primes & the difficulty of reversing this multiplication to find the component primes decreases.Thus, this calls for utilizing a better cryptosystem having a better trapdoor function.

Another issue is the increasing availability of resources to decrypt numbers result in the need to increase the size of the keys. This is not suitable in the case of mobile phones or low-powered devices that have a limited amount of computational power. All this pushes us in the direction of adopting a public-key system which has a better Trapdoor. **Cue ECC.**

Elliptic Curve Cryptography is one that is based on the algebraic structure of elliptic curves over finite fields. ECC is used for the same reasons as RSA, with the former having the advantages of providing equivalent security with 256-bit keys as a 3072-bit key of the latter (Latter key is 12 times greater in size!). Thus, ECC takes up only around 10% of the storage space and bandwidth as compared to RSA and thus is a perfect fit for resource-constrained systems such as mobile phones, low-powered devices and cryptocurrency networks. 


## The better Trapdoor Function

An elliptic curve is a planar algebraic curve defined by an equation of the form:
 
$${y^2} = {x^3 + Ax + B}$$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; where $${4A^3 + 27B^2 \ne 0}$$
 
It is a plane curve over a *finite field* (a field that contains a finite number of elements) which consists of the points satisfying the above equation along with a distinguished point at infinity. 
A field is a set of elements F on which two operators (addition and multiplication) are defined and satisfy basic rules (such as the operators following the distributive law). The real numbers along with the addition and multiplication operators form a field with an infinite set of elements, and on defining a field where the set of elements F is  finite it is called a finite field. An example of such a finite field is the field formed by elements composed of integers mod p when p is a prime number.

![An Elliptic Curve](/blog/assets/img/ecc/ec.png)

Elliptic curves have horizontal symmetry, and thus any point on the curve can be reflected over the x axis and the curve remains the same. Another interesting property is that any non-vertical line (different x coordinates) will intersect the curve in at most three places. When two different points on the curve have the same x coordinate and we draw a vertical line through them, we define the point at infinity to be the *third* point at which the line “intersects the curve”. We can imagine this point as lying infinitely far up the y axis, and all vertical lines intersect that point. The point at infinity has no coordinates, and its purpose is to deal with vertical lines. 

The trapdoor function is similar to a mathematical game of pool. Elliptic curves are free of cusps or self-intersections and thus are completely smooth (non-singular). A curve is said to be non-singular if all of it’s points are non singular. Non-singular point is one at which there is a well defined and unique tangent line, and thus a curve composed of completely this is called a non-singular curve. Now as a line between 2 points *always* intersects at a third point, this allows for quick hops around the curve which is computationally easy, and finally results in an endpoint that seemingly has no relation to the starting point, i.e, it is difficult to reverse the process of arriving at that point.

![Dotting](/blog/assets/img/ecc/method.gif)

Taking this example, let *A* be our origin point. If we take points *A* and *B* and draw the line passing through these two points, it will intersect the curve at the third point say *-C*. Now, by reflecting this point across the x-axis on the curve, we get the point *C*. Now, taking the line passing through the origin point *A* and *C* and repeat the process, say *'n'* times.

This move on 2 points is called the "dot" function. In relation to the above example,

> **A dot A = A**
>
> **A dot B = C**
>
> **A dot C = D** 

To ensure that the dot function produces a line that hits the curve close to the origin and does not go way off out to some extreme without intersecting at a third point, we can define a maximum 'X' value where the line will wrap back around and start from the beginning again.

**This is a great trapdoor function because as long as you know the origin point (*A*) and the number of hops done, it is easy to find the ending point (in our case, *D*). On the other hand, on only knowing the coordinates of the origin point and ending point, it is nearly impossible to find how many hops it took to get there.**

This is the concept used in ECC. An ECC system can be designed by selecting a curve equation, a prime number as a maximum, and a public point on the curve (the origin point or *A*). A private key is a number *pkey* (in our case, *n*). The public key is the public point *dotted* with itself *pkey* times. Elliptic curve discrete logarithm function refers to the computation of the private key from the public key in an ECC system.

Let us take the example of Alice and Bob communicating. Initially, they agree on using the same curve and a few other parameters. Then, they pick a random point G on the curve. Both Alice and Bob choose secret numbers *a* and *b* respectively. Alice dots the point G by itself *a* times, while Bob does the same *b* times. Both arrive at new points *A=a*G & *B=b*G, and now they exchange the points. Now both of them dot *A* and *B* with *b* and *a* respectively. In this manner, they both have generated the same shared secret key *S=ab*G, and now can securely communicate with the keys generated.

## Conclusion

Despite 30 years of intensive research, there has been no better algorithm found to solve the EC discrete logarithm problem than the current naive approach, and thus the difference between computing the Trapdoor function and reversing it is great. As it is more computationally intensive, it is a stronger system as compared to the other current ones.

**While RSA can probably still continue to be secure by increasing the key length, the trade-off is speed, as well as space. With ECC, using smaller keys that are generated quicker than RSA, the same security can be achieved which is especially a bonus on mobile phones and other less powerful devices.**

Indeed, it is the next generation of public key systems over first generation current systems like RSA based on prime factorization cryptography. Taking into consideration the extent of today's known mathematics, it provides a 10-fold increase in security and acts as the basis of much of the public key cryptography in today’s cryptocurrency world.


## References

- [Basic Intro to ECC](https://qvault.io/2020/09/17/very-basic-intro-to-elliptic-curve-cryptography/)
- [Implementing the Mathematical Curve](https://martin.kleppmann.com/papers/curve25519.pdf)
- [Elliptic Curve Theory](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)
- [How ECC works](https://www.allaboutcircuits.com/technical-articles/elliptic-curve-cryptography-in-embedded-systems/)
