#!/usr/bin/env python
# -*- coding : utf -8 -*-
def arrayMaximalAdjacentDifference(inputArray):
    i = 1
    a = []
    while i <= len(inputArray)-1:
        b = abs(inputArray[i-1] - inputArray[i])
        a.append(b)
        #print a
        i +=1
    return max(a)
    #print type(a)
if __name__ == "__main__":
    inputArray = [1, 1, 1, 1]
    print arrayMaximalAdjacentDifference(inputArray)
    