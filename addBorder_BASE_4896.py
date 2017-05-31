#!/usr/bin/env/python
# -*-coding : utf-8 -*-


def addBorder(picture):
    

    picture = [''.join(('*',i,'*')) for i in picture]
    for item in picture:
        border = '*'*len(item)
    indx = [0,(len(picture)+1)]
    for item in indx:
    #print border
        picture.insert(item,border)
    return picture

if __name__ == '__main__':
    picture = ["a"]
    print addBorder(picture)

# for i in picture:
#     #print i
#     #print len(i)-2
#     border = '*' *(len(i))
#     #print border
#     
#     indx = [0,(len(picture)+1)]
#     #print picture
#     for item in indx: 
#         #print item
#         picture.insert(item,border)
# #picture.insert(2,border)
# #print picture