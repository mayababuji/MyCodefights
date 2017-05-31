#!/usr/bin/env python
# -*- coding : utf-8 -*-
'''
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
'''
 def arrayReplace(inputArray, elemToReplace, substitutionElem):
	'''
	Method 1
	'''
     for n,i in enumerate(inputArray):
         if i == elemToReplace:
             inputArray[n] =substitutionElem
     return inputArray

def arrayReplace(inputArray, elemToReplace, substitutionElem):
	'''
	Method 2
	'''
     return map(lambda n : substitutionElem if n == elemToReplace else n,inputArray)

def arrayReplace(inputArray, elemToReplace, substitutionElem):
	'''
	Method 3
	'''
    #inputArray = [n if n!= elemToReplace else substitutionElem for n in inputArray ]
    #return [n if n!= elemToReplace else substitutionElem for n in inputArray ]
    return [substitutionElem if i == elemToReplace else i for i in inputArray]
    
if __name__ == "__main__":
    inputArray = [1, 2, 1]
    elemToReplace = 1
    substitutionElem = 3
    print arrayReplace(inputArray, elemToReplace, substitutionElem)
    
    
