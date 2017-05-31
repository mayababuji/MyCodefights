#!/usr/bin/env python
# -*- coding : utf-8 -*-
'''
 Write a solution with O(n2) time complexity, since this is
  what you would be asked to do during a real interview.

You have an array a composed of exactly n elements. Given a number x,
 determine whether or not a contains three elements for which the sum is exactly x.
'''
import itertools
from itertools import combinations
def tripletSum(a,x):
    sums = map(sum,itertools.combinations(a, 3))
    print sums
    if x in sums:
        return True
    else:
        return False
 
if __name__ == "__main__":       
    a =  [1, 1, 2, 5, 3]
    x = 8
    print tripletSum(a,x)