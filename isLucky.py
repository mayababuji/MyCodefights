#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
Given a ticket number n, determine if it's lucky or not.
For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
'''
def isLucky(n):
    if n % 2 == 0:
        str_n = map(int, str(n)) 
        sm = sum(int(str_n[i]) for i in range(len(str_n)/2))
        sm2 = sum(str_n[:len(str_n)/2-1:-1])
        if sm == sm2:
            return True
        else:
            return False
    else:
        return False
if __name__ == '__main__':
    n = 134008
    print isLucky(n)
    
        
        
# n = 120012
# print n/2
# a = map(int, str(n)) 
# 
# #print a[:len(a)/2-1:-1]
# #print sum(a[:len(a)/2-1:-1])
# 
# #print range(len(a)/2)
# sm = sum(int(a[i]) for i in range(len(a)/2))
# sm2 = sum(a[:len(a)/2-1:-1])
# print sm 
# print sm2