#!/usr/bin/env python
# -*- coding : utf -8 -*-
'''
Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
'''
def arrayMaximalAdjacentDifference(inputArray):
    i = 1
    a = []
    while i <= len(inputArray)-1:
        b = abs(inputArray[i-1] - inputArray[i])
        a.append(b)
        i +=1
    return max(a)
if __name__ == "__main__":
    inputArray = [1, 1, 1, 1]
    print arrayMaximalAdjacentDifference(inputArray)
    
