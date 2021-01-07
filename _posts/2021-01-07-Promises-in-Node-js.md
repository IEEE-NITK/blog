| layout | title | author_github | date | image | description | tags | categories |
| :---   | :--   | :---          | :--- | :---  | :------     | :--  | :---       |
| post   | Promises in Node Js | SureshKamediya | 2021-01-07  09:14:00 | /assests/img/Suresh.jpg | An introduction to Promises in Node js to get rid of callbackhell and how to create promise.| `IEEE` `CompSoc` `Promises` `Development` | `CompSoc`|


# Promises in Node js

## Introduction

Before we start with promises, let’s find why we need this?
Javascript is Asynchronous In nature and so is the node. Asynchronous programming
executes code without having dependency and no order and hence improves system efficiency, but faster execution comes with a price and we end up having callback hell scenario.

Let’s visit the callback functions in Node.js. Callback functions are used for asynchronous events. Using callback functions in Node.js does have its disadvantages. Sometimes during the process of development, the nested use of callback functions can make the code messier and difficult to maintain.


_Let's take an example to understand it easily-_ 

```js
getfirst(function(a){ 
    getsecond(a, function(b){
 		getthird(b, function(c){
 			getfourth(c, function(d){
 				  ...
			}, failurecallback);
		}, failurecallback);
	}, failurecallback);
}, failurecallback);
```


As you can see, this can get out of hand. If you throw some if statements, for loops, functional calls, or comments you'' ll have some very hard-to-read code.

### **So, What are the promises?**

How thy can help us, let’s take a look-
Well, a promise is just an enhancement to callback functions in Node.js
Promises are one way to deal with asynchronous code, without getting stuck in callback hell.
You can call promise as a proxy for a value that will eventually become available.


#### **Callbacks to Promises-**

Now let's look at the above example with "Promises", since we can attach Callbacks rather than passing them, this time the code looks much cleaner and easier to read.

To use Promises within Node js, the promise module is required. To install the promise module, run the below command-
npm install promise
and then require promise in your code to make the "then" function available.


```js
getfirst()
  .then(function(a) {
    return getsecond(a);
}).then(function(b) {  
    return getthird(b);
}).then(function(c) {
	return getfourth(c);
}).then(function(d) {  
    console.log('Final response: ' + d);
}).catch(failureCallback);
```

The code just above shows how multiple callbacks can be chained one after another. Chaining is one of the best features of Promises.

We have discussed why to use promises, now I will show you how a create a simple promise-

Promises in Javascript

A Promise is an object, and it has 3 states-

    * Pending: Initial State, before the Promise succeeds or fails
    * Resolved: Completed Promise
    * Rejected: Failed Promise



Let's create the "promise" step by step-
First, we use a constructor to create a Promise object:

```js 
const myPromise = new Promise();
```

It takes two parameters, one of success(resolve) and one for fail(reject):
```js
const myPromise = new Promise((resolve, reject) => {  
         // condition
});
```


Finally, there will be a condition. If the condition is met, the Promise will be resolved, otherwise, it will be rejected:

```js
const myPromise = new Promise((resolve, reject) => {  
    let condition;  
    
    if(condition is met) {    
        resolve('Promise is resolved successfully.');  
    } else {    
        reject('Promise is rejected');  
    }
});
```

So we have created our first Promise. Now let's use it.
then( ) for resolved Promises:
If you revisit the picture at the beginning of this post, you'll see that there are 2 cases: One for resolved promises and one for rejected. If the Promise gets resolved (success case), then something will happen next (depends on what we do with the successful Promise).

**`myPromise.then()`**;

The then( ) method is called after the Promise is resolved. Then we can decide what to do with the resolved Promise.
For example, let’s log the message to the console that we got from the Promise:
```js
myPromise.then((message) => {  
    console.log(message);
});
```

**`catch() for rejected Promises`**:

However, the then() method is only for resolved Promises. What if the Promise fails? Then, we need to use the catch() method.
Likewise we attach the then() method. We can also directly attach the catch() method right after then():

```js
myPromise.then((message) => {
    console.log(message);
}).catch((message) => {
    console.log(message);
});
```

So if the promise gets rejected, it will jump to the catch( ) method and this time we will see a different message on the console.

## **Summary**
    • Using callback functions in Node.js does have its disadvantages. Sometimes during the process of development, the nested use of callback functions can make the code messier and difficult to maintain.
    • Most of the issues with nested callback functions can be mitigated with the use of promises and generators in node.js
    • A Promise is a value returned by an asynchronous function to indicate the completion of the processing carried out by the asynchronous function.
    • Promises can be nested within each other to make code look better and easier to maintain when an asynchronous function needs to be called after another asynchronous function.

_This post is just an introduction to promises in node js as I found that everyone has a simple doubt that why we need promises and how to get started with them. Hope it helps you. If you want to learn more go through the documentation on promises which are as follows-_

References-

https://nodejs.dev/learn/understanding-javascript-promises

https://www.geeksforgeeks.org/promises-in-node-js/

https://developer.ibm.com/languages/node-js/articles/promises-in-nodejs-an-alternative-to-callbacks/

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise








