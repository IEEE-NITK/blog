---
layout: post
title: "Elegant Algorithms using Randomization"
author_github: Dragonado
date: 2021-01-06 23:00:00
image: '/assets/img/'
description: 'Finding simple and fast solutions using randomized algorithms compared to deterministic algorithms'
tags:
- IEEE NITK
- CompSoc
- Algorithms
- Randomization
categories:
- CompSoc
github_username: 'Dragonado'
use_math: true
---
## **Elegant Algorithms using Randomization**

Randomized algorithms are those algorithms that make use of something random (for example a random permutation of an array, a random number generator, etc) to calculate the answer fast with certainty or it gives the approximate answer which on an average case is correct. 

Let us skip the philosophical/mathematical question of the ability of a computer to generate something truly random and assume that we have an RNG(random number generator) that provides a number between [a,b] with uniform distribution(for all practical purposes).

## **Why should we use Randomized algorithms?**

After all deterministic algorithms are so intuitive and predictable. We can understand their time complexities and predict the output quite easily. So what is the need for randomization?
We use randomization to come up with faster algorithms (on an average case) or to avoid highly complicated deterministic algorithms. In some cases randomized algorithms are the only feasible solution to some problems.

Let me show you the beauty of Randomization with a few examples:

## **Problem 1:** 

Problem Statement: Given an array of integers of length $N$ (where $N$ is even), you are given that there are $\frac{N}{2}$ integers that are distinct and $\frac{N}{2}$ integers that are the same (For example {$1,6,2,6,6,3$}, 3 distinct elements and 3 copies). Find the element that repeats $\frac{N}{2}$ times. 

<u>Deterministic Solution:</u> 
You can run two nested for loops and check for every $(i,j)$ if $arr[i] == arr[j]$ in which case $arr[i]$ would be the answer. The time complexity of this algorithm is $O(N^2)$ which is not very efficient. 
This can be improved  to $O(N)$with knowledge of hash-maps or hash-tables or even smart partitioning. But in any case it can be proved that any deterministic algorithm takes at least $O(N)$ time to solve this problem. That is because since our program is predictable we can give the array in such a way that it takes at least $\frac{N}{2}$ steps because the first $\frac{N}{2}$ integers are the unique ones. 

<u>Randomized Solution:</u> 
The solution is quite elegant and much more simpler AND faster than the deterministic one. The solution is, take any 2 **random** elements of the array. If they are equal then we have found our repeated element, if they are not equal then just repeat the process again. 
The algorithm is just:

``` c++
while(true){
	int i1 = random_number(0,n-1), i2 = random_number(0,n-1);
	if(i1 == i2) continue;
	if(arr[i1] == arr[i2]){
		cout << "Repeated element is: " << arr[i1] << endl;
		break;
	}
}
```

That's it. No hash-map or any advanced concepts. This quite literally the simplest and fastest algorithm to solve the problem. 
It's surely simple but why is it fast? I mean in theory this algorithm could run forever, imagine it just kept taking the distinct elements. But lets do some maths and find the probability with which our algorithm takes those distinct integers each time. 
Number of favourable pairs (pairs if chosen our program would end) = $(N/2)\cdot(N/2-1)$
Total number of pairs = $N^2$. 

So the probability that our program would end in the first iteration is,(say) $P$= $\frac{N \cdot(N-2)}{4 \cdot N^2}$ = $\frac{1}{4} - \frac{1}{2 \cdot N}$ 
which is greater than $\frac{1}{5}$ for all $N \geq 10$, so $P \geq \frac{1}{5}$ which implies that the probability that the program does not end on the first step (say) $Q$ = $1-P$, so $Q$ $\leq 4/5$

So we have found out that if we only performed one iteration there is a $80$% chance that we would not get our desired answer. Yikes that's extremely bad.  Well whats the probability that we don't get our answer after 2 steps? Its just $Q^2$ because there is no difference between the first and second iteration. and $Q^2 \leq 16/25$, so we have a $64$% chance that we don't get our answer within 2 steps. Well its still bad but at least its better. 

So let our program run for 100 iterations. Then $Q^{100} \leq 2\cdot 10^{-10}$ which is such a small number that for all practical purposes that this will never happen. So our algorithm is so fast that given an array of $2$ million integers any deterministic algorithms would take at least $1$ million steps to find the answer whereas the above one would require at most $100$ (for all practical purposes). 

There is a separate method for denoting and calculating time complexities of randomised algorithms. But they are not straightforward so for brevity's sake I will skip it.

## **Problem 2:** 

[Problem Statement](https://codeforces.com/problemset/problem/665/C)

The solution is greedy. 
Algorithm: Let $str$ be the string we have inputted and $N$ be the length of the string. Here is the solution below. Only the replace() function needs to be written.  

```c++
str.push_back('$'); // adding an extra special character to cover corner cases
int ans = 0;
for(int i = 0; i+1 < N; i++){
    if(str[i] == str[i+1]){
		str[i+1] = replace(str[i],str[i+2]); //coming with the replace() function is the hardest part
        ans++;
    }
}
cout << ans << endl;
```

<u>Deterministic Solution:</u>
Well that seems easy, let's come up with the replace() function that takes 2 alphabets as arguments and returns an alphabet that is not one of the two. Let the two alphabets be $a_1$ and $a_2$ An easy solution is to just return the alphabet  that comes after max($a_1$,$a_2$). So if $a_1 =$'d' and  $a_2 = $ 'x' then we would choose 'y'. 

But wait this wont work if one of them is 'z' as there is no alphabet after 'z'. Ok, to fix this we could choose the alphabet that comes before both of them but that would not work if one of them is 'a'. We can't choose the middle because $a_1$ and $a_2$ could be consecutive. 

All in all, there is definitely an efficient solution that returns us a valid alphabet but the code/logic would be a bit messy. 

<u>Randomized Solution:</u> 
Just choose a random alphabet. If the alphabet is equal to one of the two alphabets then choose again, else we are done and return the chosen alphabet. That's it!

```c++
char replace(char a1, char a2){
	char ch = a1;
	while(ch == a1 || ch == a2) ch = 'a' + random_number(0,25);
	return ch;
}
```

Just 3 lines of code. It definitely simplified the code and logic. What about running time? We can use the same logic we did for the first example and calculate the probability with which our program wont end in 10 steps. Spoiler: The probability is $(\frac{2}{26})^{10}$ which is even smaller than the previous example. 

[Link](https://codeforces.com/contest/1400/submission/103560014) to my submission

## **Problem 3:**

[Problem Statement](https://codeforces.com/contest/1400/problem/A)

<u>Deterministic Solution:</u> 
Since this a constructive problem there are multiple solutions all of which require some smart non-trivial observation.
For example one possible answer, is to just print the alternate characters of the given string. This is definitely a simple and fast algorithm, but you need to prove that the answer string you print will always match with at least one of the characters in each substring.  This might take some effort and time on your side to convince others and yourself that this algorithm works. Running time wise, this is the fastest solution. 

<u>Randomized Solution:</u> 
Choose a random binary string of length $N$. For each substring of length $N$ of the original string, check if at least one character matches with the chosen random string. If there exists some substring which has no matching character then we just choose another random binary string. If for each substring our string is valid then we output it. 
Make sure you understand the logic of the above algorithm properly, it can be quite tricky to understand the first time you read it. 

But it is obvious that the string produced by this algorithm is always correct . There is no need of proving to anyone of its correctness. But you need to convince yourself that its fast enough. 
Calculating the time complexity is a little more complicated but it can be done. it is of the order $O(N^2)$ and since $N \leq 50$ we can be sure that the algorithm will give the answer quite quickly. 

[Link](https://codeforces.com/contest/1400/submission/103560014) to my submission. 

All the algorithms discussed above fall under a class of randomized algorithms called [Las Vegas Algorithms](https://en.wikipedia.org/wiki/Las_Vegas_algorithm). These are such algorithms that will always give the correct answer but whose running time depends on the randomness of the variables.

There is another class of algorithms called [Monte Carlo algorithms](https://en.wikipedia.org/wiki/Monte_Carlo_algorithm), where the running time of such algorithms are fixed but the algorithm may or may not give the correct answer because the answer depends on the randomness of our variables. For example it may give the correct answer $80$% of the time. 

## Conclusion

Not all problems can be solved using randomization. But do keep a lookout on those that can optimised/simplified using randomness. This just scratches the surface of randomization. 

There are data structures that use randomness called [probabilistic data structures](https://en.wikipedia.org/wiki/Category:Probabilistic_data_structures)(Monte Carlo type) and other data structures like [Treaps](https://cp-algorithms.com/data_structures/treap.html) (Las Vegas type) that depend on randomness for its fast running time. [Quick Sort](https://en.wikipedia.org/wiki/Quicksort) is one of the fastest sorting algorithms because of the property of random numbers. There is also a class of algorithms called [Genetic Algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm)(Monte Carlo type) that simulate survival-of-the-fittest concept to find the optimal answer. 
So the scope of this topic is quite large and highly practical.

## References

* [Wikipedia](https://en.wikipedia.org/wiki/Randomized_algorithm)

* Computer Algorithms in C++, Computer Science Press, division of W.H. Freeman, New York, September 1996 (with S. Sahni and Sanguthevar Rajasekaran) 

