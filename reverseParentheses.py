#!/usr/bin/env python
#-*- coding : utf-8 -*-
def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
            #print start
            #print (s[:start])
        if s[i] == ")":
            end = i
            #print (end)
            print s[start+1:end:-1]
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

s = "a(bcdefghijkl(mno)p)q"
print reverseParentheses(s)