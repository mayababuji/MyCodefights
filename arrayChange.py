#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
You are given an array of integers. On each move you are allowed to increase exactly one 
of its element by one. Find the minimal number of moves required to obtain a strictly increasing 
sequence from the input.
'''
def arrayChange(inputArray):
    i = 1
    sum_total = 0
    while i < len(inputArray):
        if inputArray[i] <= inputArray[i-1]:
            sum_total += (inputArray[i-1] - inputArray[i]) + 1
            inputArray[i] += (inputArray[i-1] - inputArray[i]) + 1 
        i += 1
    print inputArray
    return sum_total


if __name__ =="__main__":
    a = [-1000, 0, -2, 0]
    print arrayChange(a)
