---
layout: post
title: "Different ways to console.log for better clarity"
author_github: tim-nitk
date: 2021-01-5 06:11:00
image: '/assets/img/'
description: "Helps in effective debugging + spices up your boring JS console command line "
tags:
- IEEE NITK
- CompSoc
- Javascript
- Debugging
categories:
- Compsoc
github_username: 'tim-nitk'

---

# Here are 5 ways you can ninjafy your console logging skills

## **1. console.log( 'COLORED_TEXT' )**

You will have to use `%c` with each occurrence accompanied by an argument that expresses the styling that you desire

```javascript
console.log(
  '%c Object A instantiated %c before B !!  ',
  'background: white; color: red', 
  'background: red; color:white'
);

```

Note that you could use any CSS property under the sun into as an argument. In case of the above string this is how it renders out

![console color](https://dev-to-uploads.s3.amazonaws.com/i/ytw800vc5jjemxkmvjq1.png)


## **2. console.table( ARRAY_OF_OBJECTS )**

Use this when you want to print an **array of objects**
For example if you want to print this :

```javascript

const arrayOfBooks = [
  { title: 'Heart of Darkness', author: 'Joseph Conrad' },
  { title: 'A Walk in the Woods', author: 'Bill Bryson' },
  { title: 'Rich Dad Poor Dad', author: 'Robert Kiyosaki' }
];

```

then y'all know what `console.log(arrayOfBooks)` does

![console log](https://dev-to-uploads.s3.amazonaws.com/i/ji0931s47gdlqwt3c7nn.png)

But if you instead use  

```javascript 
console.table(arrayOfBooks)
```
you'll get the following output:

![console table](https://dev-to-uploads.s3.amazonaws.com/i/pjrv2rf8ngrvtvn0k95i.png)
 
Isn't it at least 300 times nicer and easier to infer what the array is ?

## **3. console.image( 'URL_OF_IMG' )**

![console image](https://camo.githubusercontent.com/835e3c41004fae89bb9061405d78cada32aa6783/687474703a2f2f692e696d6775722e636f6d2f68763670776b622e706e67)

**HOLD TIGHT FOLKS !** Before you leave to try this out yourself in the console let me tell you that this one is **NOT** natively available to Javascript in the browser

You will have to first load this JS resource from the CDN using the below script tag : 

```html

<script src='https://raw.githubusercontent.com/adriancooney/console.image/master/console.image.min.js'></script>

```

For more details on ☝️ , refer this link https://github.com/adriancooney/console.image. Obviously the project isn't maintained anymore (the last commit is like 6 years ago) becoz there isn't really anything more to `console.image` :) 

**BONUS : ** You get `console.meme` included in the CDN to make something like this :

![meme console](https://camo.githubusercontent.com/0f25ac62249194f32edbd54c912ae2952aa02f1a/687474703a2f2f692e696d6775722e636f6d2f4f646f564d44532e706e67)

And the format for that as per their Github Readme is:

```javascript
console.meme(upper text, lower text, meme type|url, width, height)
```

## **4. console.warn( YOUR_MESSAGE )**

You can use this to sort of indicate log messages that show the devs it's not really something that breaks the project but good to fix it in the future commits

```javascript

console.warn('Image Kirk_0932.jpg dimensions are slightly off and its causing a small part to be hidden from the user')

```

and here is a screenshot of how ⚠️ WARNING messages look like inside the console

![warning](https://dev-to-uploads.s3.amazonaws.com/i/a1km5vxno0i8rlemo873.png)


## **5. console.time() to Test Your API**

You can keep track of how much time api calls take to fetch data right in the console. You can use this to find out average time and if you think it *suxx,* you can bug your backend dev ;P

So pass in the same label `'API_TEST'` to `time` and `timeEnd` functions for it to work.

```javascript

console.time("API_TEST");

const fiftyTests = Array.from(
     { length: 50 }, 
     () => fetch('https://jsonplaceholder.typicode.com/todos/1'));

for(const prom of fiftyTests) {
  const resp = await prom;
  const json = await resp.json();
  console.count('Fetched ');
}

console.timeEnd("API_TEST");

```
Now you can see the time it takes to make api calls 50 times one - after - the - other printed in your console.

![console time](https://dev-to-uploads.s3.amazonaws.com/i/oyefq9cmajnmissrikur.png)

You can now divide it by 50 to get the average time the API takes to respond.

**⚠️ Don't use *Promise.all()* because it will simultaneously await all promises and tell you once everything has resolved which defeats our purpose**

 
