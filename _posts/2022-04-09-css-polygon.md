---
layout: post
title: "CSS Polygons"
date: 2022-04-09 15:21:21
image: '/assets/img/'
description: 'An introduction to CSS Polygons'
tags:
- IEEE NITK
- CompSoc
- Web
categories:
- Diode  
github_username: 'mrakshith21'
---

<style>

  .shapes {
      
    margin: auto;
    width: 200px;
    height: 200px;
    background: red;
    cursor: pointer;
    color: White;
    clip-path: polygon(50% 0%, 50% 0%, 0% 100%, 0% 100%, 100% 100%, 100% 100%);
    animation: polygons 4s infinite;
  }

  @keyframes polygons {
    25% {
      clip-path: polygon(0% 0%, 0% 0%, 0% 100%, 0% 100%, 100% 100%, 100% 0%);
      background: pink;
    }
    50% {
      clip-path: polygon(50% 0%, 50% 0%, 0% 45%, 25% 100%, 75% 100%, 100% 45%);
      background: orange;
    }
    75% {
      clip-path: polygon(50% 0%, 0% 30%, 0% 70%, 50% 100%, 100% 70%, 100% 30%);
      background: cornflowerblue;
    }
  }

  .img-animation {
      width: 50%;
      animation: flippingShapes 3s infinite;
  }

  @keyframes flippingShapes {
      from {
          clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
      }
      
      50% {
          clip-path: polygon(50% 10%, 90% 50%, 50% 90%, 10% 50%);
      }

      to {
          clip-path: polygon(100% 0%, 100% 100%, 0% 100%, 0% 0%);
      }
  }

  .hover-effect{
    width : 70%;
    height : 100px;
    background-color : #42A5F5;
    color: #42A5F5;
    clip-path: circle(5% at 50% 50%);
    transition: all 1s;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: auto;
  }

  .hover-effect:hover{
    background-color: #1565C0;
    border-radius : 5px;
    color : white;
    clip-path: circle(100% at 50% 50%);
  }

</style>

## Motivation

The motivation for this blog is [In Pieces](http://www.species-in-pieces.com/#), an exhibition of CSS Polygons made by tinkering a single CSS property.

## Introduction

Unconventional shapes catch the eye. Imbibing shapes in your HTML pages can be a tough task using conventional CSS. But here's ```clip-path```, a simple yet powerful property to cover all shapes that you might envision.

Here are some polygons, designed using ```clip-path```. 

<div class="shapes">
        
</div>

## Clip path

```clip-path``` property clips a region such that only the content within the region is visible and the content outside becomes invisible.

I will be presenting 4 values of clip-path in this blog.

### Circle

![Circle](/blog/assets/img/polygon/Circle.png)

**The contrast in the second image above and in all images further are for demo
purpose. The contrasted region will be invisible in the actual rendering.**

```
img{
  clip-path: circle(30px at 50% 50%);
}
```

The general format for the circle clip-path is  
```clip-path: circle(radius at centerX centerY)```

- Here centerX and centerY are measured from the top left corner of the image.
- All the values radius, centerX and centerY can take units in px, rem, % and so on.


In essence, the above code clips a circle of radius 30px from the center of the image.

### Inset 

Inset is used to work with the edges of reactangles.
The edges will be pulled back by an inset specified. You can think of it being
similar to a padding in an image, just that the padded region becomes invisible.

![Inset](/blog/assets/img/polygon/Inset.png)

```
img{
  clip-path: inset(10px 20px 20px 20px);
}
```

The general format for inset is  
```clip-path: inset(inset_top inset_right inset_bottom inset_left)```

```clip-path``` also allows you to round the corners of an inset
by using ```round <border-radius>```


### Ellipse

This allows you to create oval-shaped or elliptical clippings.

![Ellipse](/blog/assets/img/polygon/Ellipse.png)

```
  img{
    clip-path: ellipse(40px 30px at center);
  }
```

The general format for an ellipse is  
```clip-path: ellipse(major_x_axis minor_y_axis at centerX centerY)```


### Polygon

It is the most intersesting of all values so far. With polygon you can 
control multiple end-points of the clipping.

![Circle](/blog/assets/img/polygon/Polygon.png)
```
  img{
    clip-path: polygon(50% 0%, 0% 50%, 50% 100%, 100% 50%);
    background-color: #1E88E5;
  }
```

Polygon takes as a parameter the vertices of the polygon to be clipped and their
coordinates with respect to the top left corner.
The x-coordinate is towards the right and the y-coordinate is towards the bottom.

The general format for a polygon is  
```clip-path: polygon(x1 y1, x2 y2, x3 y3, ...)```

<br>
## Use cases

### 1. Angled section

This is a common design used in many web pages, where the background
appears slightly slanted. It is quite easy to 
implement this using ```clip-path : polygon()```. You just need to tweak the
vertex at the bottom right and you're done.

![Angled section](/blog/assets/img/polygon/Angled.png)

```
  div{
    background-color: 
    clip-path: polygon(0% 0%, 0% 100%, 100% 70%, 100% 0%);
  }
```
<br>

### 2. Hover effects

You can create simple but pleasing effects on hover using clip-path.
Take for example, an expanding circle that reveals information to you.
Hover on the circle below to see yourself.

<div class="hover-effect">
  This text is displayed on hover
</div>
<br>

```
    .hover-effect{
      width : 70%;
      height : 100px;
      background-color : #42A5F5;
      color: #42A5F5;
      clip-path: circle(5% at 50% 50%);
      transition: all 1s;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: auto;
    }

    .hover-effect:hover{
      background-color: #1565C0;
      border-radius : 5px;
      color : white;
      clip-path: circle(100% at 50% 50%);
    }
```

<br>

### 3. Animations on images

Faces and emotions are not often very well expressed when they are
displayed as rectangular images. You can instead use clip-path to give
a feeling to those pictures. Add animations and the effect is even better.

<div >
      <img class="img-animation" src="/blog/assets/img/polygon/Cat.jpeg" alt="Animation">
</div>


Notice how the vertices of the polygon are changing with time. If you change
 the order of the vertices, the animation changes too!

```

  img {
      animation: flippingShapes 3s infinite;
  }

  @keyframes flippingShapes {
      from {
          clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%);
      }
      
      50% {
          clip-path: polygon(50% 10%, 90% 50%, 50% 90%, 10% 50%);
      }

      to {
          clip-path: polygon(100% 0%, 100% 100%, 0% 100%, 0% 0%);
      }
  }

```

<br>

## Points to remember while using clip-path

- The borders, outlines of the region that is invisible will also be invisible.
- Hover and mouse pointer effects are not applied on the invisible region.
- While using transitions with clip-path, make sure that the effect is aesthetically pleasing.

## References

1. [Understanding clip-path](https://ishadeed.com/article/clip-path/)
2. [In Pieces - a CSS polygon exhibition](http://www.species-in-pieces.com/#)
3. [Clip-path maker](https://bennettfeely.com/clippy/)
4. [Animations with clip-path](https://blog.logrocket.com/guide-to-css-animations-using-clip-path/)