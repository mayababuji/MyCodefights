#!/usr/bin/env/python
# -*-coding : utf-8 -*-
<<<<<<< HEAD
'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
For
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''
=======
"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.
"""

>>>>>>> 21f9d6ac126a25331fed7b68271620f143e23a1d

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
<<<<<<< HEAD

=======
>>>>>>> 21f9d6ac126a25331fed7b68271620f143e23a1d
