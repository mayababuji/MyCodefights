#!/usr/bin/env python
# -*- coding : utf-8 -*-
'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''
from collections import Counter
def palindromeRearranging(inputString):
    count_char = Counter(inputString)
    pair = 0
    nt_pair = 0
    for k,v in count_char.items():
        if v %2 == 0:
            pair += 1
        else:
            nt_pair += 1
    if pair > 0 and nt_pair == 0:
        return True
    if pair % 2 == 0 and nt_pair ==1:
        return True
    if nt_pair > 1:
        return False
if __name__ == "__main__":
    strng = "zyyzzzzz"
    print palindromeRearranging(strng)

        
            
            
