---
layout: post
title: "Intro to Blockchain"
date: 2025-05-27 00:05:00
image: '/assets/img/'
description: 'Intro to BlockChain'
tags:
- IEEE NITK
- CompSoc
- BlockChain
categories:
- CompSoc
github_username: 'anuragkumar2121'
---

## **Introduction**

![alt_text](/blog/assets/img/BlockChain/1.png)

A blockchain is a distributed software network that functions both as a digital ledger and a mechanism enabling the secure transfer of assets without an intermediary. Just as the internet is a technology that facilitates the digital flow of information, blockchain is a technology that facilitates the digital exchange of units of value. Anything from currencies to land titles to votes can be tokenized, stored, and exchanged on a blockchain network.


## **The root of it all… Bitcoin**

![alt_text](/blog/assets/img/BlockChain/2.png)

* In 2008, after the financial crisis, an anonymous programmer by the pseudonym Satoshi Nakamoto invented Bitcoin, a peer-to-peer electronic cash system based on a new form of database technology called blockchain.
* While traditional currencies are backed by trust in 3rd parties, like the bank, bitcoin is backed by mathematics. It helps in creating a trustless environment, because the mathematics itself creates the trust.
* It uses the concept of a distributed ledger system.

## **Distributed Ledger System**

![alt_text](/blog/assets/img/BlockChain/3.png)

* Each player in the bitcoin system maintains their own personal ledger with all the set of transactions till date. The transactions are immutable in nature, i.e, once written they cannot be changed.
* Whenever a new transaction is made, it is hashed via a special function called cryptographic hash function. This is a special function 
f(Message, Private Key) which returns the hash of the message using the private key of user.
* The cryptographic hash function is such that it is difficult to invert and thus going from the hashed output back to the message is incredibly difficult. For example, the CHF called SHA256 generates a 256 bit unique hash for each input, and therefore the probability of a hash corresponding to a message is 2-256  , which is practically 0.
* When this message is received by Alice, she can verify that it was indeed sent by Bob by using her public key using a function verify (Message, Hash, Public Key).

## **Nonce and Proof of Work**

![alt_text](/blog/assets/img/BlockChain/4.png)

Ok, so that’s it for theory, now let’s see where we can implement it. Let us consider the case of a system which requires lots of pin connection with a microcontroller, which is typically Arduino Uno. So sometimes we need to cascade two Arduinos due to pin shortage or sensor working or whatever the reason. To ensure the working of cascading, I2C comes into the picture.

A4 pin of Arduino Uno board is SDA and A5 is SCL, so we have to connect these pins of one Arduino to another. Also, as per I2C protocol, we need to define one Arduino as master and another one as a slave for which we can use Arduino IDE with ‘wire’ library for I2C.

In Bitcoin’s Proof of Work mining process, the goal is to solve a mathematical puzzle in order to discover the next block hash and receive Bitcoin rewards. Miners must find a nonce value that, when plugged into the hashing algorithm, generates a hash value that is lower than the target difficulty.

It can be said that the nonce is the missing piece of the puzzle needed to discover the next block and miners receive the block reward.  So basically, mining revolves around brute-forcing the nonce through a mathematical algorithm and finding that lucky number that will reward the miners for their efforts.



