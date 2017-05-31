#!/usr/bin/env python
# -*- coding:utf -8 -*-
'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
'''
def allLongestStrings(inputArray):
    maxlength = max([len(item) for item in inputArray])
    inputArray = [it for it in inputArray if len(it) >= maxlength]
    return inputArray
