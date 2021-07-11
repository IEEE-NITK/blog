---
layout: post
title: "State Management in Flutter"
author_github: ikjot-2605
date: 2021-06-04 00:00:00
image: '/assets/img/'
description: 'Did reading about state management from the plethora of blogs out there just confuse you? Let me set it straight once and for all...'
tags:
- Flutter
- State Management
- Development
- Good Practices
categories:
- CompSoc
github_username: 'ikjot-2605'
---
## Let's start by getting one thing clear.

### **What do you mean by "state"?**

Essentially, the state of the app, or a particular widget in the app, is *just information*, that is used to render the UI. This means that any change in the UI was caused by a change in the state of the application.

<center><img src = "/blog/assets/img/State-Management-In-Flutter/image1.png" height = 225 alt = "What is a State?"></center>
<hr>

## **Alright, but what is state management?**

State management is nothing but a means to handle the multiple states your application can have. But to go further here, we need to understand the difference between Ephemeral State and Application State.
<center><img src = "/blog/assets/img/State-Management-In-Flutter/image2.png" height = 225 alt = "State Management"></center>

<hr>

## **Ephemeral State vs Application State**
You can think of the Ephemeral state as the state that is localized to a particular, very small part/widget in the application. <br>For example, a password text field may have two states:

1. Hide Password
2. Show Password

As you can probably guess, the state that may be controlling this particular widget is extremely localized and can be handled easily with a setState() method.

**This is an ephemeral state.**

On the flip side, if you think of another more large-scale feature, such as implementing a dark mode, the state that will be working with this, will have a large-scale impact throughout the application, and hence it cannot be handled with a vanilla setState() method.

**This is an Application state, and this is where the concept of requiring a state management system comes in.**
<hr>

## **Okay, so how does state management help?**
We will answer this by looking at the pros and cons of using **setState()** and **Flutter BLoC**(a popular state management plugin)

## **<u>setState()</u>**

### **Pros of setState()**

1. Very easy and straightforward to understand.
2. A great way to handle the Ephemeral State.

**Per the docs**: Ephemeral State is sometimes called UI State or local State. It’s the State you can neatly contain in a single widget.

### **Cons of setState()**

1. Not a good way to handle things involving app State (Global State and parts of the State you want to persist between sessions).
2. Using setState() all over an app can become a maintenance nightmare very quickly because your State is scattered all over the place
3. Usually used within the same class as the UI code, mixing UI and business logic, which breaks clean code principles. In a tiny app, this is no big deal but it becomes a concern quickly when you have more than just a couple of screens. You can separate the logic with a little effort, but there are better ways to handle State Management once an app grows beyond a few pages.
4. From my personal experience, your app will quickly become laggy and slow if you use a lot of setState() method. This is because it **rebuilds the entire widget tree** each time it is called.

<hr>

## **<u>Flutter BLoC(Business Logic Component)</u>**

### <u>BLoC is an architectural state management pattern created and used by Google</u>

BLoC stands for Business Logic Components, and it’s much more of an architecture than setState(); it has even been compared to MVVM (Model, View, View Model). Unlike the others, BLoC makes use of Streams and it’s often used with Provider ( another state management plugin ), which is often used as a way of exposing the BLoC for the UI.

But what does it do? Anything you want. Maybe you fed it a String that said “Smith” and the logic in the BLoC was made to return a list of everyone in your contacts list with that last name. Maybe the BLoC gets fed the number of clock ticks that have passed since an animation started and the BLoC’s job is to calculate the position of your bouncing ball based on how long ago you pressed the button. You can make it do whatever you want, it’s an architecture, a method of handling State… what you do with it is entirely up to you.

<center><img src = "/blog/assets/img/State-Management-In-Flutter/image3.png" height = 500 alt = "BLoC Flow"></center>

### **Pros of BLoC**

1. Easy to separate UI from logic
2. Easy to test code
3. Easy to reuse code
4. Good Performance

### **Cons of BLoC**

1. Technically, you need to use streams in both directions, creating a lot of boilerplate. However, many people cheat this by using streams only from the backend to the UI, but when events occur they’re simply calling functions directly instead of feeding those events into a sink.
2. More boilerplate code, but it's worth it due to the extensive reusability. 

<hr>

## **Conclusion**

### In this article we discussed

 1. What is state?
 2. What is state management?
 3. What are the two types of state?
 4. Comparison of two popular yet very different techniques to implement state management.

### There are other options as well which are beyond the scope of this article like Redux, Flutter Hooks, etc.

<hr>
