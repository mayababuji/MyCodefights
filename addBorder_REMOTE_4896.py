#!/usr/bin/env/python
# -*-coding : utf-8 -*-
"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
"""


def addBorder(picture):
    

    picture = [''.join(('*',i,'*')) for i in picture]
    for item in picture:
        border = '*'*len(item)
    indx = [0,(len(picture)+1)]
    for item in indx:
        picture.insert(item,border)
    return picture

if __name__ == '__main__':
    picture = ["a"]
    print addBorder(picture)
