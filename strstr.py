#!/usr/bin/envpython
# -*- coding : utf-8 -*-
'''
Implement a function that takes two strings, s and x, 
as arguments and finds the first occurrence of the string x in s. 
The function should return an integer indicating the index in s of the first occurrence of x. 
If there are no occurrences of x in s, return -1.


'''
def strstr(s, x):

    if x in s:
        return s.index(x)
    else:
        return -1
    
if __name__ == "__main__":
    s = "a" 
    x = "a"
    print strstr(s, x)
