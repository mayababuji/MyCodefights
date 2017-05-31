#!/usr/bin/env python 
#-*- coding : utf-8 -*- 

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


