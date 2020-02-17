# algorithm-selection-problem

This repository will gather different algorithms for the **selection problem** in a list. It will highlight the performance of the **Divide to Conquer** paradigm in the context of this problem.

## Introduction to the problem

This problem often follows the problem of sorting list mainly because one of its solutions: **Randomized Selection** hinges on the same method as the one of **Quick Sort**.

### Input

Given:
* a list of n integers: `L = [a1, ..., an]`
* i and integer of [1, n] 

### Goal 

We want to return the value of the ith order statistic (i.e. ith smallest element of L)

***Example***: One specific case of this problem is finding the **median**:
- the (n+1)/2th element in n i odd
- the n/2th element if n is even

## Solutions

### Reduction to sorting

A simple approach is to sort the array and take the ith element of the list. The complexity of this algorithm is that of the sorting algorithm.

If we take **merge_sort** as the sorting algorithm, the complexity will be in **O(nln(n))** in average.

However, as we can't sort a list any faster than in **O(nln(n))**, this complexity is an lower bound of the complexity we can achieve. See this [video](https://www.youtube.com/watch?v=aFveIyII5D4&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=39) for more explanation.



