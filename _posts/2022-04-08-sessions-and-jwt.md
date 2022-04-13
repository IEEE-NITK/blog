---
layout: post
title: "Sessions and JWT"
author_github: famousfive1
date: 2022-04-08 17:30:30
image: '/assets/img/'
description: 'A simple explanation about sessions and JWT used in authorization'
tags:
- IEEE NITK
- Blog
- Web Dev
- JWT
- Sessions
categories:
- CompSoc
github_username: 'famousfive1'
---

# __Sessions and JWT__

## __Intro__

Suppose you are developing a web application. Chances are that you want the user to be able to create an account or sign in and then access certain restricted parts of the site, such as their profile page or the forums/comment section. The HTTP protocol is stateless, meaning that it retains no information about the previous state or requests made. Thus, you need some other mechanism to track whether a user is logged in or not. There are two main methods to achieve this: Sessions and JSON Web Tokens (JWT).

Before going into their details, there are two terms that are often misused or interchanged.
1. Authentication: the process of verifying a user and granting access.
2. Authorization: the process of making sure that a person has permission to access a requested resource.

Authentication is done before authorization. Authentication usually involves a user typing in his/her username and password. Whereas in authorization, the server makes sure that the user who is requesting access is actually who he/she is claiming to be and that he has permission to request.

Here, I am not going to explain the process of securely logging in a user and ensuring data security. That is a topic for another post.

## __Sessions__

Assume that you are a customer who has some issues and reach out to tech support. You tell the attendant your name and contact details to establish that you are a past customer and then explain your problem. The attendant notes down your problem, gives you a token/complaint number, and tells you to mention it to the technician who will help you.

What happened here is the basic idea behind sessions. It is a method to maintain the state of a user. In this case, the token number is a way to uniquely identify you. The server stores all the details. Whenever you go to the technician, you can give him your token number and he will be able to access your details and your complaint without you having to repeat yourself.

## __JWT__

The attendant above could also have chosen a different approach. Instead of providing you with a token number, he could have signed the paper containing all of your information and complaint and instructed you to hand it to the technician. The technician then would have all the details available to him on the paper.

This is the idea behind JWT. None of your data is actually stored with the attendant. Instead, its given to you on a signed piece of paper. The signing process here is of huge significance. It ensures that the paper you are handing to the technician is legit and that you didn't change or forge any details. If it wasn't signed by the attendant or if there is any suspicion of tampering, the technician could just reject it and ask you to start from the beginning again.

## __Technicalities__

What I have described here is only the core concepts behind the two major methods of dealing with statefulness in a stateless protocol like HTTP. Although there are some technicalities that have not been explained yet.

### __Sessions__

After authorization, the server needs to generate a session ID and send it to the client. This is usually done by setting it to a cookie. The server stores the session ID along with the user ID for further reference. This is stored either in a database or in an in-memory store like [Redis](https://redis.io/). The client then sends the session token on further requests to verify itself. Whenever there is a request, the server looks up the session ID and retrieves the data from the database. If a user logs out, then the session ID is removed from the storage.


OWASP provides a detailed article ([Link](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)) on sessions, which is a must-read for anyone thinking of implementing sessions. Even if you end up using third-party libraries, having this knowledge is essential. Here are some key points:

- Session IDs are supposed to be long, random strings of at least 128 bits.

- They must not reveal any information about the architecture of your server (such as default names used by frameworks) or about the user itself.

- They must be unpredictable (random enough) to prevent brute force attacks. Using a good cryptographically secure random number generator is a must.

- Usage of proper cookie flags for storing and transmitting the ID token is recommended.


### __JWT__

JWT stands for JSON Web Token. It is because the data is formatted as a JSON (JavaScript Object Notation) object. There are 3 parts to a typical JWT, each separated by a dot (`.`):

1. Header - contains the signing algorithm used

2. Payload - contains the actual data being transmitted

3. Signature - contains the header and payload signed together using a secret

OWASP also has a cheatsheet for JWT ([Link](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)).

When used only for authorization, you should use a signing algorithm such as [HMAC](https://en.wikipedia.org/wiki/HMAC) (JWT also supports public/private key encryption like [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) or [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) when two way communication is needed). When you use a token for authorization, it should only be modifiable by the server. Thus, the server needs to sign the token with a strong and secret key. Any time the content of the token is changed, it needs to be re-signed.

The secret used for signing should also be long and random.


## __Sessions Vs. JWT - Advantages and Disadvantages__

There is no benefit to using one over the other. Each has its own tradeoffs. Depending on the application, one might be suitable over the other. Usually, token-based authorization is preferred when there is no continuous session being maintained, such as in API services. Sessions is good for situations where the user stays logged in for some time while working.

That being said, here are some tradeoffs:

### _Sessions_

The client holds no sensitive data. Invalidation of a session is as simple as removing it from the storage.

Usually, servers are sitting behind a load balancer which splits the incoming traffic. In this case, a user's request may be sent to server 1 for logging in but be sent to server 2 for the next. To make sure that the session persists across the server instances, either the session ID must be stored in shared memory or the load balancer must make sure to send the user's request to the same server every time.


### _JWT_

The server doesn't have to maintain a state. All the necessary details are contained within the JWT itself. This also avoids the load balancer problem since the server doesn't have to remember anything.

Signing out or invalidating a user/﻿user's token is a bit hard. Separate storage needs to be maintained with the expired tokens, and each time a token is submitted, it needs to be checked for validity.

It is also a bit risky since some of the clients' details are stored on the token itself, which can be read by anyone. So, it requires more security measures.

On a side note, JWT has many other uses than just authorization.


## __Conclusion__

I hope this article gives a good introduction to sessions and JWT and helps you choose what authorization method you want to use. It can be a bit tricky to choose the right method. But both are equally capable. 


