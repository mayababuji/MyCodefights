#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].


'''

def sortByHeight(a):
    sort_items = sorted([x for x in a if x !=-1])
    for indx,item in enumerate(a):
        if item == -1:
            continue
        a[indx] = sort_items[0]
        del sort_items[0]
    return a
 
if __name__ =='__main__':
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    print sortByHeight(a)

    
    
