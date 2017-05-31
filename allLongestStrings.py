#!/usr/bin/env python
# -*- coding:utf -8 -*-
def allLongestStrings(inputArray):
    maxlength = max([len(item) for item in inputArray])
    inputArray = [it for it in inputArray if len(it) >= maxlength]
    return inputArray
