#!/usr/bin/env python
# -*- coding : utf-8 -*-


import numpy
image =[[36,0,18,9,9,45,27], 
 [27,0,54,9,0,63,90], 
 [81,63,72,45,18,27,0], 
 [0,0,9,81,27,18,45], 
 [45,45,27,27,90,81,72], 
 [45,18,9,0,9,18,45], 
 [27,81,36,63,63,72,81]]
b = []
a = numpy.array(image)
total_elem =  sum(1 for i in a.flat)
for i in range(len(image)):
    a =  sum(image[i])
    b.append(a)
print sum(b)/total_elem