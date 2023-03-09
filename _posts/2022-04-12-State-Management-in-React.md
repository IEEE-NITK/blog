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

<hr/>

### Redux

Redux is a full fledged library, built for state management. It creates a javascript object called store, which keeps track of all the states used throughout the program

![Redux Cycle](/blog/assets/img/State-Management-in-React/react-redux-architecture.png)

#### State

In React, state refers to an object that represents the current state of a component. It is an internal data store that allows components to manage their own data and change the way they are displayed based on this data. Whenever the state of a component changes, React re-renders the component to reflect the new state.

The state object can be initialized in the constructor of a class component or by using the useState hook in a functional component. It should only be modified using the setState method or by calling the hook function returned by useState, to ensure that React is aware of the change and can trigger a re-render.

#### Hooks

React hooks are functions that allow functional components to use state and other React features that were previously only available to class components. They were introduced in React version 16.8 and have since become an essential part of React development.

Some commonly used hooks are: 

1. useState: Allows functional components to use state.
2. useEffect: Allows functional components to use lifecycle methods.
3. useContext: Allows functional components to use context.
4. useReducer: Allows functional components to use a reducer for more complex state management.
5. useCallback and useMemo: Optimizes performance by memoizing functions and values.

Hooks allow developers to write cleaner and more concise code, and make it easier to share logic between components. They are a powerful tool for building complex applications with React.

#### Store

The Redux store is a single source of truth for the state of an entire Redux application. It is an object that holds the complete state tree of your application, which can be accessed by calling getState(). The store also has several important methods, including dispatch() to dispatch actions, subscribe() to listen for state changes, and replaceReducer() to replace the current reducer function.

In Redux, the store is created using the createStore() function, which takes a reducer function as an argument. The store is then used to dispatch actions, which trigger changes in the application state.

#### Action

Actions are plain JavaScript objects that represent a change to the state of the application. They contain a type field that specifies the type of action being performed, as well as any additional data required to perform the action.

Actions are created using action creators, which are functions that return an action object. For example, an action creator for adding an item to a shopping cart might look like this:

```
function cartReducer(state = [], action) {
  switch (action.type) {
    case 'ADD_TO_CART':
      return [...state, action.payload]
    case 'REMOVE_FROM_CART':
      return state.filter(item => item.id !== action.payload.id)
    default:
      return state
  }
}
```

The type field is a string that describes the type of action being performed, while the payload field contains any additional data required to perform the action.

#### Reducer

Reducers are pure functions that take the current state and an action as arguments, and return a new state object that reflects the changes made by the action. The state object returned by a reducer is a new object, rather than a mutated version of the original object.

A reducer function typically uses a switch statement to handle different action types and return a new state object based on the action. For example, a reducer for managing a shopping cart might look like this:

```
function cartReducer(state = [], action) {
  switch (action.type) {
    case 'ADD_TO_CART':
      return [...state, action.payload]
    case 'REMOVE_FROM_CART':
      return state.filter(item => item.id !== action.payload.id)
    default:
      return state
  }
}
```

In this example, the reducer function takes the current state and an action as arguments, and returns a new state object based on the action. The ADD_TO_CART action adds a new item to the cart by creating a new array with the existing items and the new item. The REMOVE_FROM_CART action removes an item from the cart by filtering the existing items based on the ID of the item to be removed.

Reducers are combined using the combineReducers() function, which takes an object containing multiple reducer functions and returns a single reducer function that can handle all of the actions for the entire application state.

<hr/>

Apart from Redux, there are several other popular state management libraries for React that are worth exploring:

1. MobX: MobX is a simple, scalable and battle-tested state management library for React. It uses observables to track state changes and automatically re-renders components when the state changes. MobX is easy to learn and use and requires less boilerplate code than Redux.

2. Context API: Context API is a built-in feature in React that allows you to share state between components without using props. It provides a way to pass data through the component tree without having to manually pass props down the tree. Context API is useful for small to medium-sized applications and doesn't require any external libraries.

3. Redux Toolkit: Redux Toolkit is a set of utilities and conventions for Redux that make it easier to write and maintain Redux code. It includes a simplified API for creating Redux stores, as well as built-in support for common Redux use cases like asynchronous actions and immutable state updates.

Each of these libraries has its own advantages and disadvantages, and the choice of which one to use depends on the specific needs of your application. It's always a good idea to evaluate multiple libraries and choose the one that best fits your requirements.

Do explore the different state management libraries and hooks!
