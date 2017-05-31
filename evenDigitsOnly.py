#!/usr/bin/env python
# -*- coding : utf-8 -*-
# n = 248622
# for i in str(n):
#     if int(i)%2 ==0:
#         print True
#from __builtin__ import int

# def evenDigitsOnly(n):
#     a = map(int,list(str(n)))
#     b = [] 
#     b = [i%2 for i in a]
#     return 1 not in b
# 
# def evenDigitsOnly(n):
#     if any(int(x) % 2 == 1 for x in list(str(n))):
#         return False
#    return True
        
# def evenDigitsOnly(n):
#     return all(int(x) % 2 == 0 for x in list(str(n))) 


def evenDigitsOnly(n):
    return all(int(x) %2 == 0 for x in str(n))

if __name__ == "__main__":
    n = 246
    print evenDigitsOnly(n)

    