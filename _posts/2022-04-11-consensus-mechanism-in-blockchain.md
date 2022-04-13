---
layout: post
title: "Consensus Mechanism in Blockchain"
author_github: Tejas000
date: 2022-04-11 00:00:00
image: '/assets/img/'
description: 'A Brief description of two important consensus mechanisms; proof-of-work and proof-of-stake'
tags:
- IEEE NITK
- CompSoc
- Blockchain
categories:
- compsoc
github_username: 'Tejas000'
use_math: true
---
# CONSENSUS MECHANISM

The Blockchain is an undeniably ingenious invention, By definition,**_ Blockchain_** is a continuously growing list of records, called blocks, which are linked and secured using cryptography. Each block typically contains a cryptographic hash of the previous block, a timestamp, and transaction data. By design, a blockchain is inherently resistant to modification of the data. It is “an open, distributed ledger that can record transactions between two parties efficiently and in a verifiable and permanent way”. This technology has led to various new inventions in the cryptocurrency marketplace such as Bitcoin, Ethereum, Ripple, and many others, all of these technologies use DLT (Distributed Ledger Technology) as their core foundation, For use as a distributed ledger, a blockchain is typically managed by a peer-to-peer network collectively adhering to a protocol for validating new blocks.

Thus, Blockchains in essence are distributed databases, the network's nodes must reach an agreement on the network's current state. This agreement is achieved using consensus mechanisms.


## NEED FOR CONSENSUS MECHANISM

In a centralized organization, all the decisions are taken by the leader or a board of decision-makers. This isn’t possible in a blockchain because a blockchain has no “leader”. For the blockchain to make decisions, they need to come to a consensus using “**consensus mechanisms**”. Consensus algorithms check the integrity of new blocks and past blocks

Distributed systems rely on large numbers of autonomous authorities to cooperate in the maintenance of a single network. These distinct nodes must have a computational mechanism by which to arrive at an agreement on what the most recent and accurate record of data is. 

Over the years different kinds of consensus mechanisms were devised based on different principles, let’s take a look at 2 of the most important mechanisms;


## PROOF OF WORK:

 The Blockchain network is shared by numerous users who do transactions. These transactions need to be further validated to add them to the block and then to the chain. This task is carried out by miners (The validators), The miners validate a set of transactions from the transaction pool, verify them, bundle them together in a block, and add this block to the current blockchain. But in order to prevent any forgery and double-spending and to agree upon the correct sequence of the blocks, we need a consensus mechanism. That’s where proof of work comes into the picture.

In proof of work, miners compete to add the next block (a set of transactions) in the chain by racing to solve an extremely difficult cryptographic puzzle. The miners calculate a complex mathematical puzzle, called the NONCE.

transactions are processed into blocks. Each block has a:

block difficulty – for example: 3,324,092,183,262,715

mixHash – for example: 0x44bca881b07a6a09f83b130798072441705d9a665c5ac8bdf2f39a3cdf3bee29

nonce – for example: 0xd3ee432b4fb3d26b

The proof-of-work protocol requires miners to go through an intense race of trial and error to find the nonce for a block. Only blocks with a valid nonce can be added to the chain. The miner that gets the valid nonce first gets to add the next block in the blockchain.

The proof-of-work protocol follows the longest chain rule.

_“ The majority decision is represented by the longest chain, which has the greatest proof-of-work effort invested in it. — [Satoshi Nakamoto](https://nakamotoinstitute.org/bitcoin/)”_

All the nodes trust the longest chain in a blockchain without trusting each other directly. The objective of proof-of-work is to extend the chain. The longest chain is most believable as the valid one because it's had the most computational work done. It's nearly impossible to create new blocks that erase transactions, create fake ones, or maintain a second chain. That's because a malicious miner would need to always solve the block nonce faster than everyone else.

To consistently create malicious yet valid blocks, you'd need over 51% of the network mining power to beat everyone else. You'd need a lot of computing power to be able to do this amount of "work". And the energy spent might even outweigh the gains you'd make in an attack.


## PROOF OF STAKE

POS uses a different approach compared to POW. The miner commits the currency ( stake) he has to the blockchain network to get an opportunity to mine. A chosen random miner with a stake validates the block transaction. If a miner cannot commit to the stake, the miner can join a stake pool to participate in the mining.

Unlike proof-of-work, validators don't need to use significant amounts of computational power because they're selected at random and aren't competing. They don't need to mine blocks; they just need to create blocks when chosen and validate proposed blocks when they're not. This validation is known as attesting. Validators get rewards for proposing new blocks and for attesting to ones they've seen.

If you attest to malicious blocks, you lose your stake.


## A COMPARISON

Energy consumption is one major difference between the two consensus mechanisms. Because proof-of-stake blockchains don’t require miners to spend electricity on duplicative processes (competing to solve the same puzzle), proof of stake allows networks to operate with substantially lower resource consumption.

Both consensus mechanisms have economic consequences that penalize network disruptions and malicious actors. In proof of work, the penalty for miners submitting invalid information, or blocks, is the sunk cost of computing power, energy, and time. In proof of stake, the validators’ staked crypto funds serve as an economic incentive to act in the network’s best interests. In the case that a validator accepts a bad block, a portion of their staked funds will be “slashed” as a penalty. The amount that a validator can be slashed depends on the network
