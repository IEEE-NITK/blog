---
layout: post  
title: "Simplifying State Management Using React Hooks"
date: 2023-05-09 7:30:00 
description: ‘We analyse the different ways by which we can manage state in react using differnt hooks’

tags:
- IEEE NITK
- React
- Web Development

categories:
- CompSoc

github_username: ahmedfahim21

---

# Simplifying State Management Using React Hooks

## **Introduction**

Before React Hooks, state management was typically done in class components using the `state` property and the `setState` method. However, with the introduction of hooks, managing the state in functional components has become much easier.

React Hooks are functions that allow you to use state and other React features in functional components. Hooks provide a way to reuse stateful logic between components, which makes it easier to manage state and reduces code duplication.

React provides a declarative way to manipulate the UI. Instead of manipulating individual pieces of the UI directly, you describe the different states that your component can be in, and switch between them in response to the user input.

## **How declarative UI compares to imperative**

When you design UI interactions, you probably think about how the UI *changes* in response to user actions. Consider a login screen:

* When you enter the username and the password, the “Login” button **becomes enabled.**
    
* When you press “Login”, both the login input fields and the button **become disabled,** and a spinner **appears.**
    
* If the network request succeeds, the form **gets hidden,** and it redirects you to the dashboard page.
    
* If the network request fails, an error message **appears,** and the login input fields **becomes enabled** again.
    

React was built to do this task effectively.

In React, you don’t directly manipulate the UI—meaning you don’t enable, disable, show, or hide components directly. Instead, you **declare what you want to show,** and React figures out how to update the UI.

Here are some of the most commonly used React Hooks for state management with their implementation to help you learn and understand better:

* ### useState
    

The `useState` hook allows you to manage state in a functional component. It takes an initial value as an argument and returns an array with two values: the current state and a function to update the state.

```javascript
import { useState } from 'react';

function Example() {
  const [isShowing, setIsShowing] = useState(false);

  return (
    <div>
      <button onClick={() => setIsShowing(!isShowing)}>
        {isShowing ? 'Hide' : 'Show'}
      </button>
      {isShowing && <div>Content to be shown or hidden</div>}
    </div>
  );
}
```

In the example above, the `useState` hook is used to manage a boolean value `isShowing` with an initial value of `false`. When the button is clicked, the `setIsShowing` function is called to update the state and toggle the boolean value.

* ### useReducer
    

The `useReducer` hook allows you to manage more complex state in a functional component. It takes a reducer function and an initial state as arguments and returns an array with the current state and a dispatch function to update the state.

```javascript
import { useReducer } from 'react';

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <div>
      Count: {state.count}
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
    </div>
  );
}
```

In the example above, the `useReducer` hook is used to manage a counter with an initial value of `0`. The `reducer` function takes the current state and an action object as arguments and returns a new state based on the action type. The `dispatch` function is used to send an action object to the reducer function to update the state.

* ### useContext
    

The `useContext` hook allows you to access global state in a functional component. It takes a context object created using the `createContext` function as an argument and returns the current context value.

```javascript
import React, { useContext } from "react";

const ThemeContext = React.createContext("light");

function Button() {
  const theme = useContext(ThemeContext);
  const buttonStyle = {
    backgroundColor: theme === "dark" ? "black" : "white",
    color: theme === "dark" ? "white" : "black",
    padding: "10px 20px",
    cursor: "pointer",
  };
  return <button style={buttonStyle}>Click me!</button>;
}

function App() {
  return (
    <div>
      <ThemeContext.Provider value="dark">
        <Button />
      </ThemeContext.Provider>
      <ThemeContext.Provider value="light">
        <Button />
      </ThemeContext.Provider>
    </div>
  );
}

export default App;
```

* ### useEffect
    

The `useEffect` hook allows you to perform side effects in a functional component. Side effects include things like fetching data, subscribing to events, or updating the document title. `useEffect` takes a function as an argument and runs it after the component is rendered.

```javascript
import { useState, useEffect } from 'react';

function Example() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <ul>
      {data.map(item => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
}
```

In the example above, the `useEffect` hook is used to fetch data from an API using the `fetch` function. The data is then set using the `setData` function, which updates the state and triggers a re-render.

* ### useCallback
    

The `useCallback` hook allows you to memoize a function in a functional component. Memoization means that the function will only be re-created if its dependencies change. This can improve performance by reducing unnecessary re-renders.

```javascript
import { useState, useCallback } from 'react';

function Example() {
  const [count, setCount] = useState(0);

  const increment = useCallback(() => {
    setCount(count + 1);
  }, [count]);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
    </div>
  );
}
```

In the example above, the `useCallback` hook is used to memoize the `increment` function. The function is only re-created if the `count` state changes, which means it won't trigger unnecessary re-renders.

* ### useRef
    

`useRef` provides a way to create a mutable reference to a DOM element or a value that persists across renders. Unlike state, updating the `useRef` value does not trigger a re-render of the component.

The `useRef` hook takes an initial value as an argument and returns a reference object with a `current` property that can be used to access or update the value.

```javascript
import React, { useRef } from 'react';

function TextInput() {
  const inputRef = useRef(null);

  const handleClick = () => {
    console.log(inputRef.current.value);
  };

  return (
    <div>
      <input type="text" ref={inputRef} />
      <button onClick={handleClick}>Submit</button>
    </div>
  );
}
```

`useRef` to creates a reference to an input element and then accesses its value in an event handler to log the input value when the button is clicked.

* ### useTransition
    

The `useTransition` hook is a React hook that enables smooth transitions between different states of a component. It's particularly useful for handling asynchronous operations, such as data fetching or state updates that cause the component to re-render.

```javascript
import React, { useState, useTransition } from 'react';

export default function App({ users }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [filtered, setFiltered] = useState(users);
  const [isPending, startTransition] = useTransition();

  const handleChange = ({ target: { value } }) => {
    setSearchTerm(value);
    startTransition(() => {
      setFiltered(users.filter((item) => item.name.includes(value)));
    });
  };

  return (
    <div className="container">

      <div>
        {
          isPending ? (
            <div>Loading...</div>
          ) : (
            <p>
              {
                 users.length !== filtered.length 
                 ? `${filtered.length} matches` 
                 : null
              } 
            </p>
          )
        }
      </div>

      <input 
        onChange={handleChange} 
        value={searchTerm} 
        type="text"
        placeholder="Type a name" />

      {
        isPending ? (
          <div>Loading...</div>
        ) : (
          <div className="cards">
            {filtered.map((user) => (
              <div class="card">
                <div className="profile">
                  <img 
                    src={user.avatar} 
                    alt="Avatar" />
                </div>
                <div className="body">
                  <strong>{user.name}</strong>
                </div>
              </div>
            ))}
          </div>
        )}
    </div>
  );
}
```

The code example demonstrates how to use the `useTransition` hook in a React component to filter a list of users based on a search term. The `useTransition` hook is used to handle state transitions for the filtered list, providing a smoother user experience during transitions by showing a loading indicator. Overall, the code provides a good example of how to leverage the `useTransition` hook to create responsive and performant user interfaces when dealing with large lists of data.

* ### Custom Hooks
    

React comes with several built-in Hooks like `useState`, `useContext`, and `useEffect`. Sometimes, you’ll wish that there was a Hook for some more specific purpose.

Custom hooks in React are reusable pieces of code that allow you to extract and reuse stateful logic across multiple components. They are functions that use built-in hooks, or other custom hooks, to provide a specific behavior that can be shared across multiple components.

Custom hooks can simplify your code, making it easier to understand and maintain. They allow you to encapsulate complex logic into a single function that can be used in multiple components, reducing code duplication and improving reusability.

To create a custom hook, simply create a new function that uses one or more built-in hooks or other custom hooks, and returns some data or behavior that can be used by other components.

### **Conclusion**

In conclusion, React Hooks have simplified state management in functional components by allowing us to use stateful logic without having to use class components. The hooks mentioned in this blog post are just a few of the many hooks available in React, and each hook has its own unique use case. By mastering these hooks, you can write cleaner, more efficient code and build better React applications.



## Resources

- [Official React Documentation](https://react.dev/)