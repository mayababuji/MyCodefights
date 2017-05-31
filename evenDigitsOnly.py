#!/usr/bin/env python
# -*- coding : utf-8 -*-
'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.
'''
def evenDigitsOnly(n):
	'''
	Method 1
	'''
	a = map(int,list(str(n)))
     	b = [] 
     	b = [i%2 for i in a]
     	return 1 not in b

def evenDigitsOnly(n):
	'''
	Method 2
	'''
     if any(int(x) % 2 == 1 for x in list(str(n))):
         return False
    return True

def evenDigitsOnly(n):
	'''
	Method 3
	'''
     return all(int(x) % 2 == 0 for x in list(str(n))) 

def evenDigitsOnly(n):
	'''
	Method 4
	'''
    return all(int(x) %2 == 0 for x in str(n))

if __name__ == "__main__":
    n = 246
    print evenDigitsOnly(n)

    
