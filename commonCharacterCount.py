#!/usr/bin/env python 
#-*- coding : utf-8 -*- 
'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''
def commonCharacterCount(s1, s2):
    common_char = set(s1).intersection(set(s2))
    count_char = []
    for item in common_char:
        count_char.append(min(s1.count(item),s2.count(item)))
    return sum(count_char)

if __name__ == "__main__":
    s1 = "aabcc" 
    s2 = "adcaa"
    print commonCharacterCount(s1, s2)


