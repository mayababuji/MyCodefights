#!/usr/bin/env python
# -*- coding : utf-8 -*-
'''
You have two integer arrays, a and b, and an integer target value v. 
Determine whether there is a pair of numbers, where one number is taken from a and the other from b,
 that can be added together to get a sum of v. Return true if such a pair exists, otherwise return false.
For a = [1, 2, 3], b = [10, 20, 30, 40], and v = 42, the output should be
sumOfTwo(a, b, v) = true.
'''
from timeit import itertools

 def sumOfTwo(a, b, v): 
	'''
	Method 1
	''' 
     dicta = {}
     dictb= {}
     for item in a:
         dicta[item] = 1
     print dicta
     for item in b:
         if (v-item) in dicta: 
             return True
     return False

 import itertools
'''
Method 2
'''
 list1=['a','b','c']
 list2=[1,2]
 zip(x,list2) for x in itertools.permutations(list1,len(list2))]



def sumOfTwo(a, b, v):
	'''
	Method 3
	'''
    combined = [zip(i,a) for i in itertools.permutations(b,len(a))]
    cc = map(sum,itertools.chain(*combined))
    if v in cc:
        return True
    else:
        return False


def sumOfTwo(a, b, v):
	'''
	Method 4
	'''
    #if len(a) == 0 or len(b) == 0:
    #    return False
    s = map(sum,itertools.product(a, b))
    #s = [sum(x) for x in list(itertools.product(a, b))]
    print s
    return v in s


def sumOfTwo(a, b, v): 
	'''
	Method 5
	'''
    x = [] 
    for i in range(len(a)):
        for j in range(len(b)):
            x.append(a[i] + b [j])
    return v in x
if __name__ == "__main__":
    a = [22, 26, 6, 22, 17, 11, 9, 22, 7, 12]
    b = [14, 25, 22, 27, 22, 30, 6, 26, 30, 27]
    v = 56
    print sumOfTwo(a, b, v)
    
