layout: post
title: "State Management in React"
date: 2022-04-12 13:00:00
image: '/assets/img/'
description: 'Purpose of State Management in React'
tags:
- IEEE NITK
- CompSoc
- React
- Web Development
categories:
- CompSoc
github_username: 'BenzeneAlcohol'
---


# State Management in React

Have you ever wondered how memory is managed in React? Why do we need state in the first place? Which state management system is the best? I will be explaining all of the above and more in this blog. 

Suppose you have a div in your website, whose content needs to be changed dynamically, according to user input. Now, at this point you know you need a place in memory store what the user enters, and display it back to the user. This is where state comes into picture.

If there is just a single div, in the same page, then it is really simple to render the user's input without any issues. But, once you have multiple pages and multiple components spanning accross the same website, that is when the issues start ticking. First issue that came to my mind was - How am I supposed to share this data with other components? In React, we follow the practice of having different components, each within a function, in different javascript files. Now, how are we supposed to share this data with other components?

This is where the complications begin. This is just one simple use case of state, there can be many other use cases, like within the same component, suppose you want to re render just one part of it on change of data. What do you do? Again, you use a state variable.


### E-Commerce Site
Just imagine this - You are building an e-commerce application. You know that whenever you add an item to the cart, the following things must change:

    1. Number of items in cart, displayed in the navbar
    2. The button of "Add to Cart" should change to "Increase Quantity"
    3. The item must get added to the cart.

And many more.

The catch here is that the cart variable is shared everywhere. It is shared by the navbar, it is shared in the logic of "Add Item" button, it is shared by the checkout page and all the pages connected to checkout.

So, we need a comprehensive mechanism with which we can share memory across different components and pages so that everything is interconnected properly.

To solve all these issues, we have "State Management" in React, in the form of hooks, redux and whatnot. State Management becomes messier the more the variables and components you have. Hence we have full fledged libraries like Redux, that help you maintain the state easily.

Let us discuss these in brief.

### Redux

Redux is a full fledged library, built for state management. It creates a javascript object called store, which keeps track of all the states used throughout the program

![Redux Cycle](/blog/assets/img/react-redux-architecture.png)

#### State

The state is a javascript object that represents the entire state of a redux application. It can be a simple object with a single value or a more complex object.

#### Store

A store is a javascript object that holds the application's state. There can be only one store in a web application.

#### Action

An action is an description of how the store should change the state.

#### Reducer

A reducer is a javascript function that will create a new state based on some action type.



There are other state management libraries as well, along with hooks which make things even simpler. Redux has some disadvantages. The most glaring one is the amount of boiler plate code that goes into setting up a redux store, is sometimes too daunting even for a professional.

Do explore the different state management libraries and hooks!