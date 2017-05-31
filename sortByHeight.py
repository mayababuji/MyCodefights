#!/usr/bin/env python
#-*- coding:utf-8 -*-


def sortByHeight(a):
    sort_items = sorted([x for x in a if x !=-1])
    print sort_items
    for indx,item in enumerate(a):
        if item == -1:
            continue
        a[indx] = sort_items[0]
        del sort_items[0]
    return a
 
if __name__ =='__main__':
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    print sortByHeight(a)

# def sortByHeight(a):
#     heigths = sorted([x for x in a if x >= 0])
#     inds = [i for i, x in enumerate(a) if x >= 0]
#     print inds
#     for i, ind in enumerate(inds):
#         a[ind] = heigths[i]
#     return a
# 
# 
# a = [-1, 150, 190, 170, -1, -1, 160, 180]
# 
# print(sortByHeight(a))
    
    
