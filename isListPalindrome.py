#!/usr/bin/env python
#-*_ coding : utf-8 -*-
'''
Given a singly linked list of integers, determine whether or not it's a palindrome.

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;
For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.
'''
 def isListPalindrome(l):
	return l == l[::-1]
 if __name__ == "__main__":
     l = [1, 2, 2, 3]
     print isListPalindrome(l)
     


